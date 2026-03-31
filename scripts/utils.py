import json
import os
import requests
from datetime import datetime, timezone
from pathlib import Path

CONFIG_PATH = Path(__file__).parent.parent / "config.json"
STATE_PATH = Path(__file__).parent.parent / "sent_posts.json"

def get_image_url(entry):
    if hasattr(entry, 'media_thumbnail'):
        return entry.media_thumbnail[0]['url']
    if hasattr(entry, 'media_content'):
        return entry.media_content[0]['url']
    return None

def get_tags(entry):
    if hasattr(entry, 'tags'):
        return [tag.term for tag in entry.tags]
    return []

LIGHT_BG = "#f4f8fb"
LIGHT_CARD = "#ffffff"
LIGHT_BORDER = "#e5e7eb"
LIGHT_TEXT = "#1c2733"
LIGHT_TEXT_MUTED = "#4b5563"
LIGHT_PRIMARY = "#007bff"

DARK_BG = "#0a192f"
DARK_CARD = "#1f2937"
DARK_BORDER = "#374151"
DARK_TEXT = "#e5e7eb"
DARK_TEXT_MUTED = "#9ca3af"
DARK_PRIMARY = "#3b82f6"

SINGLE_POST_TEMPLATE = f"""<!-- buttondown-editor-mode: fancy -->
<div style="margin:0;padding:0;background:{LIGHT_BG};color:{LIGHT_TEXT};font-family:Inter,Segoe UI,Arial,sans-serif;">
  <div style="max-width:640px;margin:auto;padding:32px;">
    <div style="
      background:{LIGHT_CARD};
      padding:32px;
      border:1px solid {LIGHT_BORDER};
      border-radius:0 0 24px 24px;
      text-align:left;
      box-shadow:0px 4px 10px rgba(0,0,0,0.06);
    ">
      <h2 style="text-align:center;font-size:22px;color:{LIGHT_TEXT};margin:0;">
        {{title}}
      </h2>
      {{description}}
    </div>

    {{image}}

    <div style="
      background:{LIGHT_CARD};
      border:1px solid {LIGHT_BORDER};
      border-radius:0 0 24px 24px;
      padding:24px;
      box-shadow:0px 4px 10px rgba(0,0,0,0.06);
    ">
      <h2 style="color:{LIGHT_TEXT};margin-top:0;">Read the full post</h2>
      <p style="line-height:1.7;color:{LIGHT_TEXT};">
        You can read the full article here:
      </p>
      <p style="margin:24px 0;">
        <a href="{{link}}"
          style="
            display:inline-block;
            background:{LIGHT_PRIMARY};
            color:#ffffff;
            padding:12px 20px;
            border-radius:8px;
            text-decoration:none;
            font-weight:600;
            box-shadow:0px 4px 10px rgba(0,0,0,0.1);
          ">
          Read the Article →
        </a>
      </p>
    </div>
  </div>
</div>"""

def build_single_post_email(title, description, image_url, link):
    description_html = f'<p style="margin-top:12px;font-size:16px;color:{LIGHT_TEXT_MUTED};">{description}</p>' if description else ''
    
    image_html = f"""    <div style="margin:40px 0 0 0;">
      <img src="{image_url}"
        alt="{title}"
        style="
          width:100%;
          display:block;
          border-radius:24px 24px 0 0;
          border:1px solid {LIGHT_BORDER};
          border-top:none;
          box-shadow:0px 4px 10px rgba(0,0,0,0.06);
        " />
    </div>
    """ if image_url else ''
    
    return SINGLE_POST_TEMPLATE.format(
        title=title,
        description=description_html,
        image=image_html,
        link=link
    )

WEEKLY_TEMPLATE = f"""<!-- buttondown-editor-mode: fancy -->
<div style="margin:0;padding:0;background:{LIGHT_BG};color:{LIGHT_TEXT};font-family:Inter,Segoe UI,Arial,sans-serif;">
  <div style="max-width:640px;margin:auto;padding:32px;">

    <div style="
      background:{LIGHT_CARD};
      padding:32px;
      border:1px solid {LIGHT_BORDER};
      border-radius:0 0 24px 24px;
      box-shadow:0px 4px 10px rgba(0,0,0,0.06);
    ">
      <h1 style="margin:0;font-size:26px;color:{LIGHT_TEXT};">
        Weekly Digest - {{week_range}}
      </h1>
      <p style="margin-top:12px;font-size:16px;color:{LIGHT_TEXT_MUTED};">
        Here's everything I published this week.
      </p>
    </div>

    <div style="
      margin-top:40px;
      background:{LIGHT_CARD};
      padding:24px 32px;
      border:1px solid {LIGHT_BORDER};
      border-radius:24px;
      box-shadow:0px 4px 10px rgba(0,0,0,0.06);
    ">
      {{posts}}
    </div>

    <div style="
      margin-top:40px;
      background:{LIGHT_CARD};
      border:1px solid {LIGHT_BORDER};
      border-radius:24px 24px 0 0;
      padding:24px;
      text-align:center;
      color:{LIGHT_TEXT_MUTED};
      font-size:14px;
      box-shadow:0px 4px 10px rgba(0,0,0,0.06);
    ">
      <p style="color:{LIGHT_TEXT_MUTED};">Thanks for reading 💙</p>
      <p style="color:{LIGHT_TEXT_MUTED};">You're receiving this because you're subscribed to my blog updates.</p>
    </div>

  </div>
</div>"""

def build_weekly_email(week_range, posts_html):
    return WEEKLY_TEMPLATE.format(week_range=week_range, posts=posts_html)

MONTHLY_TEMPLATE = f"""<!-- buttondown-editor-mode: fancy -->
<div style="margin:0;padding:0;background:{LIGHT_BG};color:{LIGHT_TEXT};font-family:Inter,Segoe UI,Arial,sans-serif;">
  <div style="max-width:640px;margin:auto;padding:32px;">

    <div style="
      background:{LIGHT_CARD};
      padding:32px;
      border:1px solid {LIGHT_BORDER};
      border-radius:0 0 24px 24px;
      box-shadow:0px 4px 10px rgba(0,0,0,0.06);
    ">
      <h1 style="margin:0;font-size:26px;color:{LIGHT_TEXT};">
        Monthly Digest - {{month_name}} {{year}}
      </h1>
      <p style="margin-top:12px;font-size:16px;color:{LIGHT_TEXT_MUTED};">
        Here's everything I published this month.
      </p>
    </div>

    <div style="
      margin-top:40px;
      background:{LIGHT_CARD};
      padding:24px 32px;
      border:1px solid {LIGHT_BORDER};
      border-radius:24px;
      box-shadow:0px 4px 10px rgba(0,0,0,0.06);
    ">
      {{posts}}
    </div>

    <div style="
      margin-top:40px;
      background:{LIGHT_CARD};
      border:1px solid {LIGHT_BORDER};
      border-radius:24px 24px 0 0;
      padding:24px;
      text-align:center;
      color:{LIGHT_TEXT_MUTED};
      font-size:14px;
      box-shadow:0px 4px 10px rgba(0,0,0,0.06);
    ">
      <p style="color:{LIGHT_TEXT_MUTED};">Thanks for reading 💙</p>
      <p style="color:{LIGHT_TEXT_MUTED};">You're receiving this because you're subscribed to my blog updates.</p>
    </div>

  </div>
</div>"""

def build_monthly_email(month_name, year, posts_html):
    return MONTHLY_TEMPLATE.format(month_name=month_name, year=year, posts=posts_html)

YEARLY_TEMPLATE = f"""<!-- buttondown-editor-mode: fancy -->
<div style="margin:0;padding:0;background:{LIGHT_BG};color:{LIGHT_TEXT};font-family:Inter,Segoe UI,Arial,sans-serif;">
  <div style="max-width:640px;margin:auto;padding:32px;">

    <div style="
      background:{LIGHT_CARD};
      padding:32px;
      border:1px solid {LIGHT_BORDER};
      border-radius:0 0 24px 24px;
      box-shadow:0px 4px 10px rgba(0,0,0,0.06);
    ">
      <h1 style="margin:0;font-size:26px;color:{LIGHT_TEXT};">
        Yearly Digest - {{year}}
      </h1>
      <p style="margin-top:12px;font-size:16px;color:{LIGHT_TEXT_MUTED};">
        Here's everything I published this year.
      </p>
    </div>

    <div style="
      margin-top:40px;
      background:{LIGHT_CARD};
      padding:24px 32px;
      border:1px solid {LIGHT_BORDER};
      border-radius:24px;
      box-shadow:0px 4px 10px rgba(0,0,0,0.06);
    ">
      {{posts}}
    </div>

    <div style="
      margin-top:40px;
      background:{LIGHT_CARD};
      border:1px solid {LIGHT_BORDER};
      border-radius:24px 24px 0 0;
      padding:24px;
      text-align:center;
      color:{LIGHT_TEXT_MUTED};
      font-size:14px;
      box-shadow:0px 4px 10px rgba(0,0,0,0.06);
    ">
      <p style="color:{LIGHT_TEXT_MUTED};">Thanks for reading 💙</p>
      <p style="color:{LIGHT_TEXT_MUTED};">You're receiving this because you're subscribed to my blog updates.</p>
    </div>

  </div>
</div>"""

def build_yearly_email(year, posts_html):
    return YEARLY_TEMPLATE.format(year=year, posts=posts_html)

def load_config():
    with open(CONFIG_PATH) as f:
        return json.load(f)

def load_state():
    if STATE_PATH.exists():
        with open(STATE_PATH) as f:
            return json.load(f)
    return {"sent_posts": [], "sent_monthly": [], "sent_yearly": []}

def save_state(state):
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)

def send_email(subject, body, api_key):
    config = load_config()
    response = requests.post(
        "https://api.buttondown.com/v1/emails",
        headers={
            "Authorization": f"Token {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "subject": subject,
            "body": body,
            "status": config.get("email_status", "draft")
        }
    )
    response.raise_for_status()
    return response.json()

def get_week_start():
    now = datetime.now(timezone.utc)
    days_since_sunday = now.weekday() + 1
    week_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    if days_since_sunday < 7:
        week_start = week_start.replace(day=week_start.day - days_since_sunday)
    else:
        week_start = week_start.replace(day=week_start.day - 7)
    return week_start

def get_month_start():
    now = datetime.now(timezone.utc)
    return now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

def get_year_start():
    now = datetime.now(timezone.utc)
    return now.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)

def format_date(dt):
    return dt.strftime("%Y-%m-%d")
