import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from utils import (
    build_single_post_email,
    build_weekly_email,
    build_monthly_email,
    build_yearly_email,
    send_email
)

SAMPLE_POSTS = [
    {
        "title": "TAGRFT - There's a GitHub Repo for That",
        "link": "https://nellowtcs.me/theres-a-github-repo-for-that",
        "excerpt": "A cool thing I made for finding that one weirdly specific GitHub repository you need!",
        "image": "https://nellowtcs.me/images/posts/tagrft.png"
    },
    {
        "title": "Raspberry Pi's Touchscreen Displays",
        "link": "https://nellowtcs.me/raspberry-pis-touchscreen-displays",
        "excerpt": "A quick guide to setting up and using touchscreen displays with your Raspberry Pi projects.",
        "image": "https://nellowtcs.me/images/posts/MPI5008-001.png"
    },
    {
        "title": "Making Progressive Web Apps Easily",
        "link": "https://nellowtcs.me/making-progressive-web-apps-easily",
        "excerpt": "How to convert your web app into a PWA with just a few simple steps.",
        "image": "https://nellowtcs.me/images/posts/pwa_example.png"
    },
    {
        "title": "ePub2Markdown: Fully Browser Converter",
        "link": "https://nellowtcs.me/epub2markdown-fully-browser-converter",
        "excerpt": "Convert your ePub files to Markdown right in your browser - no downloads required!",
        "image": "https://nellowtcs.me/images/posts/Screenshot%202025-09-04%202.38.48%20PM.png"
    },
    {
        "title": "Curvomorphism: A Quick Guide",
        "link": "https://nellowtcs.me/curvomorphism-quick-guide",
        "excerpt": "Learn the basics of curvomorphic design and how to apply it to your projects.",
        "image": "https://nellowtcs.me/images/posts/curvomorphism.png"
    }
]

def build_post_html(post, show_image=True):
    image_html = ""
    if show_image and post["image"]:
        image_html = f'<img src="{post["image"]}" alt="{post["title"]}" style="width:100%;display:block;border-radius:8px;margin:16px 0;" />'
    
    return f"""
      <div style="margin-bottom:32px;">
        {image_html}
        <h3 style="margin:0 0 8px 0;font-size:18px;color:#1c2733;">{post['title']}</h3>
        <p style="margin:0 0 12px 0;color:#4b5563;">{post['excerpt']}</p>
        <a href="{post['link']}" style="color:#007bff;text-decoration:none;font-weight:600;">Read ></a>
      </div>
    """

def test_single():
    post = SAMPLE_POSTS[0]
    body = build_single_post_email(
        title=post["title"],
        description=post["excerpt"],
        image_url=post["image"],
        link=post["link"]
    )
    return "New Post Email", body

def test_weekly():
    posts_html = ""
    for i, post in enumerate(SAMPLE_POSTS[:3]):
        if i > 0:
            posts_html += '<hr style="border:none;border-top:1px solid #e5e7eb;margin:24px 0;">'
        posts_html += build_post_html(post)
    
    body = build_weekly_email("Mar 23 - Mar 29, 2026", posts_html)
    return "Weekly Digest - Mar 23 - Mar 29, 2026", body

def test_monthly():
    posts_html = ""
    for i, post in enumerate(SAMPLE_POSTS[:4]):
        if i > 0:
            posts_html += '<hr style="border:none;border-top:1px solid #e5e7eb;margin:24px 0;">'
        posts_html += build_post_html(post)
    
    body = build_monthly_email("March", "2026", posts_html)
    return "Monthly Digest - March 2026", body

def test_yearly():
    posts_html = ""
    posts_html += '<h2 style="margin:0 0 16px 0;font-size:18px;color:#7c3aed;">Featured Posts</h2>'
    for i, post in enumerate(SAMPLE_POSTS[:2]):
        if i > 0:
            posts_html += '<hr style="border:none;border-top:1px solid #e5e7eb;margin:24px 0;">'
        posts_html += build_post_html(post)
    
    posts_html += '<h2 style="margin:32px 0 16px 0;font-size:18px;color:#1c2733;">All Posts</h2>'
    for i, post in enumerate(SAMPLE_POSTS[2:]):
        if i > 0:
            posts_html += '<hr style="border:none;border-top:1px solid #e5e7eb;margin:24px 0;">'
        posts_html += build_post_html(post)
    
    body = build_yearly_email("2026", posts_html)
    return "Yearly Digest - 2026", body

def main():
    api_key = os.environ.get("BUTTONDOWN_API_KEY")
    
    if not api_key:
        print("Error: BUTTONDOWN_API_KEY not set")
        print("Usage: BUTTONDOWN_API_KEY=your_key python test_emails.py [single|weekly|monthly|yearly|all]")
        sys.exit(1)
    
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    
    tests = {
        "single": test_single,
        "weekly": test_weekly,
        "monthly": test_monthly,
        "yearly": test_yearly,
        "all": None
    }
    
    if mode not in tests:
        print(f"Unknown mode: {mode}")
        print("Available: single, weekly, monthly, yearly, all")
        sys.exit(1)
    
    if mode == "all":
        for test_fn in [test_single, test_weekly, test_monthly, test_yearly]:
            subject, body = test_fn()
            print(f"Sending: {subject}")
            send_email(f"[TEST] {subject}", body, api_key)
            print(f"  OK")
    else:
        subject, body = tests[mode]()
        print(f"Sending: {subject}")
        send_email(f"[TEST] {subject}", body, api_key)
        print("  OK")

if __name__ == "__main__":
    main()
