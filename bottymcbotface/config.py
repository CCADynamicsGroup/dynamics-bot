# -*- coding: utf-8 -*-

__all__ = [
    "get_google_json",
    "get_slack_json",
    "get_message",
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


def get_other_config():
    if "OTHER_CONFIG" in os.environ:
        return json.loads(os.environ["OTHER_CONFIG"])
    with open("secrets/config.json", "r") as f:
        return json.load(f)


def get_message(slide_deck_url, zoom_link):
    return f"""
Hi all,

Today's CCA Dynamics meeting will be at 13:30 EDT in the 6th floor conference room, or at the usual Zoom link:
{zoom_link}

If you would like to share a figure, a research update, or make an announcement, please add a slide to today's slide deck:

{slide_deck_url}

CCA Dynamics Group website:
https://galacticdynamics.nyc/

To join the Google group:
https://groups.google.com/u/1/g/ccadynamics

""".strip()


GOOGLE_JSON = get_google_json()
SLACK_JSON = get_slack_json()
OTHER_CONFIG = get_other_config()
locals().update(OTHER_CONFIG)
