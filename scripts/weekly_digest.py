import feedparser
import sys
import os
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from utils import load_config, load_state, save_state, send_email, get_week_start, build_weekly_email

def main():
    config = load_config()
    state = load_state()
    api_key = os.environ.get("BUTTONDOWN_API_KEY")
    
    if not api_key:
        print("Error: BUTTONDOWN_API_KEY not set")
        sys.exit(1)
    
    feed = feedparser.parse(config["rss_url"])
    week_start = get_week_start()
    now = datetime.now(timezone.utc)
    
    new_posts = []
    for entry in feed.entries:
        pub_date = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
        link = str(entry.link)
        slug = link.split("/")[-1].rstrip("/")
        
        if pub_date >= week_start and slug not in state["sent_posts"]:
            new_posts.append({
                "title": entry.title,
                "link": link,
                "excerpt": getattr(entry, 'description', '') or '',
                "slug": slug
            })
    
    if not new_posts:
        print("No new posts this week")
        return
    
    week_range = f"{week_start.strftime('%b %d')} - {now.strftime('%b %d, %Y')}"
    
    posts_html = ""
    for i, post in enumerate(new_posts):
        if i > 0:
            posts_html += '<hr style="border:none;border-top:1px solid #e5e7eb;margin:24px 0;">'
        posts_html += f"""
      <div style="margin-bottom:32px;">
        <h2 style="margin:0;font-size:20px;color:#1c2733;">{post['title']}</h2>
        <p style="margin:8px 0 12px 0;color:#4b5563;">{post['excerpt'][:150]}...</p>
        <a href="{post['link']}" style="color:#007bff;text-decoration:none;font-weight:600;">Read →</a>
      </div>
        """
    
    body = build_weekly_email(week_range, posts_html)
    
    subject = f"Weekly Digest — {now.strftime('%Y-%m-%d')}"
    
    send_email(subject, body, api_key)
    
    for post in new_posts:
        state["sent_posts"].append(post["slug"])
    
    state["last_weekly"] = now.isoformat()
    save_state(state)
    
    print(f"Sent {len(new_posts)} posts")

if __name__ == "__main__":
    main()
