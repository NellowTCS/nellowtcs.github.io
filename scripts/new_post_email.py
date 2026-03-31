import feedparser
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from utils import load_config, load_state, save_state, send_email, get_image_url, build_single_post_email

def main():
    config = load_config()
    state = load_state()
    api_key = os.environ.get("BUTTONDOWN_API_KEY")
    
    if not api_key:
        print("Error: BUTTONDOWN_API_KEY not set")
        sys.exit(1)
    
    changed_files_raw = os.environ.get("CHANGED_FILES", "")
    changed_paths = [p for p in changed_files_raw.split(",") if p]

    # derive slugs from changed paths, but only include paths that exist
    # in the checked-out repo (this ignores deletions)
    changed_slugs = set()
    for p in changed_paths:
        p_path = Path(p)
        if not p_path.exists():
            # deleted file, skip
            continue
        parts = p_path.parts
        try:
            idx = parts.index("(blog-article)")
            slug_from_path = parts[idx + 1]
        except ValueError:
            slug_from_path = p_path.stem
        changed_slugs.add(slug_from_path)

    feed_entries = {str(entry.link).rstrip('/').split('/')[-1]: entry for entry in feedparser.parse(config["rss_url"]).entries}

    def parse_frontmatter(md_path: Path):
        text = md_path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            return {}
        end = text.find("\n---", 3)
        if end == -1:
            return {}
        raw = text[3:end].strip()
        data = {}
        for line in raw.splitlines():
            if not line.strip() or line.strip().startswith("#"):
                continue
            if ":" not in line:
                continue
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"').strip("'")
        return data

    new_posts = []
    for slug in changed_slugs:
        if slug in state["sent_posts"]:
            continue

        entry = feed_entries.get(slug)
        if entry:
            new_posts.append({
                "title": entry.title,
                "link": str(entry.link),
                "slug": slug,
                "excerpt": getattr(entry, 'description', '') or '',
                "image": get_image_url(entry)
            })
            continue

        # Blog may not have published to RSS yet. Try source file frontmatter.
        blog_md = Path("src/routes/(blog-article)") / slug / "+page.md"
        if not blog_md.exists():
            continue

        fm = parse_frontmatter(blog_md)
        if not fm:
            continue

        if fm.get("hidden", "false").lower() == "true":
            continue

        title = fm.get("title", slug)
        excerpt = fm.get("excerpt", "")
        link = f"{config.get('blog_base_url', '').rstrip('/')}/blog/{slug}"
        image_url = fm.get("coverImage", "")

        new_posts.append({
            "title": title,
            "link": link,
            "slug": slug,
            "excerpt": excerpt,
            "image": image_url
        })
    
    if not new_posts:
        print("No new posts to announce")
        return
    
    for post in new_posts:
        body = build_single_post_email(
            title=post["title"],
            description=post["excerpt"],
            image_url=post["image"],
            link=post["link"]
        )
        
        subject = f"New post: {post['title']}"
        send_email(subject, body, api_key)
        
        state["sent_posts"].append(post["slug"])
    
    state["last_new_post"] = datetime.now(timezone.utc).isoformat()
    save_state(state)
    
    print(f"Sent announcements for {len(new_posts)} posts")

if __name__ == "__main__":
    main()
