import feedparser
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from utils import load_config, load_state, save_state, send_email, get_year_start, build_yearly_email

def main():
    config = load_config()
    state = load_state()
    api_key = os.environ.get("BUTTONDOWN_API_KEY")
    
    if not api_key:
        print("Error: BUTTONDOWN_API_KEY not set")
        sys.exit(1)
    
    now = datetime.now(timezone.utc)
    current_year = str(now.year)
    
    if current_year in state.get("sent_yearly", []):
        print("Yearly roundup already sent this year")
        return
    
    feed = feedparser.parse(config["rss_url"])
    year_start = get_year_start()
    
    all_posts = []
    featured_posts = []
    
    for entry in feed.entries:
        pub_date = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
        link = str(entry.link)
        slug = link.split("/")[-1].rstrip("/")
        tags = [tag.term for tag in entry.tags] if hasattr(entry, 'tags') else []
        
        if pub_date >= year_start:
            post = {
                "title": entry.title,
                "link": link,
                "slug": slug,
                "excerpt": getattr(entry, 'description', '') or ''
            }
            all_posts.append(post)
            
            if 'featured' in [t.lower() for t in tags]:
                featured_posts.append(post)
    
    if not all_posts:
        print("No posts this year")
        return
    
    posts_html = ""
    
    if featured_posts:
        posts_html += '<h2 style="margin:0 0 16px 0;font-size:18px;color:#7c3aed;">Featured Posts</h2>'
        for i, post in enumerate(featured_posts):
            if i > 0:
                posts_html += '<hr style="border:none;border-top:1px solid #e5e7eb;margin:24px 0;">'
            posts_html += f"""
      <div style="margin-bottom:24px;">
        <h3 style="margin:0 0 8px 0;font-size:18px;color:#1c2733;">{post['title']}</h3>
        <p style="margin:0 0 12px 0;color:#4b5563;">{post['excerpt'][:150]}...</p>
        <a href="{post['link']}" style="color:#007bff;text-decoration:none;font-weight:600;">Read →</a>
      </div>
            """
        
        posts_html += '<h2 style="margin:32px 0 16px 0;font-size:18px;color:#1c2733;">All Posts</h2>'
    
    for i, post in enumerate(all_posts):
        if i > 0 or featured_posts:
            posts_html += '<hr style="border:none;border-top:1px solid #e5e7eb;margin:24px 0;">'
        posts_html += f"""
      <div style="margin-bottom:24px;">
        <h3 style="margin:0 0 8px 0;font-size:18px;color:#1c2733;">{post['title']}</h3>
        <p style="margin:0 0 12px 0;color:#4b5563;">{post['excerpt'][:150]}...</p>
        <a href="{post['link']}" style="color:#007bff;text-decoration:none;font-weight:600;">Read →</a>
      </div>
        """
    
    body = build_yearly_email(current_year, posts_html)
    
    subject = f"Year in Review: {current_year}"
    send_email(subject, body, api_key)
    
    for post in all_posts:
        if post["slug"] not in state["sent_posts"]:
            state["sent_posts"].append(post["slug"])
    
    if "sent_yearly" not in state:
        state["sent_yearly"] = []
    state["sent_yearly"].append(current_year)
    state["last_yearly"] = now.isoformat()
    save_state(state)
    
    print(f"Sent yearly roundup with {len(all_posts)} posts ({len(featured_posts)} featured)")

if __name__ == "__main__":
    main()
