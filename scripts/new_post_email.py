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
    
    changed_files = os.environ.get("CHANGED_FILES", "")
    
    new_posts = []
    for entry in feedparser.parse(config["rss_url"]).entries:
        link = str(entry.link)
        slug = link.split("/")[-1].rstrip("/")
        if slug in changed_files and slug not in state["sent_posts"]:
            new_posts.append({
                "title": entry.title,
                "link": link,
                "slug": slug,
                "excerpt": getattr(entry, 'description', '') or '',
                "image": get_image_url(entry)
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
