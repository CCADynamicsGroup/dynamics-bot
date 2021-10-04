# -*- coding: utf-8 -*-

__all__ = [
    "PRESENTATION_TITLE",
    "SHARED_DRIVE_NAME",
    "TEMPLATE_NAME",
    "SHARE_WITH_EMAIL",
    "get_google_json",
    "get_slack_json",
    "get_email_template",
]

import os
import json


def get_google_json():
    if "GOOGLE_INFO" in os.environ:
        return json.loads(os.environ["GOOGLE_INFO"])
    with open("secrets/google.json", "r") as f:
        return json.load(f)


def get_slack_json():
    if "SLACK_INFO" in os.environ:
        return json.loads(os.environ["SLACK_INFO"])
    with open("secrets/slack.json", "r") as f:
        return json.load(f)


def get_email_template(slide_deck_url, zoom_link):
    return f"""
Hi all,

Today's CCA Dynamics meeting will be at 14:00 EDT in the 6th floor conference room, or at the usual Zoom link:
{zoom_link}

If you would like to share a figure, a research update, or make an announcement, please add a slide to today's slide deck:

{slide_deck_url}

best,
- Adrian
""".strip()


GOOGLE_JSON = get_google_json()
SLACK_JSON = get_slack_json()

PRESENTATION_TITLE = os.environ.get(
    "PRESENTATION_TITLE", "Dynamics Group Meeting"
)
SHARED_DRIVE_NAME = os.environ.get(
    "SHARED_DRIVE_NAME", "CCA Dynamics Group"
)
TEMPLATE_NAME = os.environ.get("TEMPLATE_NAME", "__template__")
SHARE_WITH_EMAIL = os.environ.get(
    "SHARE_WITH_EMAIL", "astro-data-group@googlegroups.com"
)
ZOOM_LINK = os.environ.get("ZOOM_LINK", None)
