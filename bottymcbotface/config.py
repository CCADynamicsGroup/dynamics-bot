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

Tomorrow's CCA Galactic Dynamics Community Meeting will be 14:00–15:30 Eastern in the 5th floor classroom.

We will kick off the meeting with very short introductions, then hear from (( NAME 1 )) and (( NAME 2 )) in the first half of the meeting.

For the second half of the meeting, everyone is invited to share a figure, a research update, a paper (from someone else!), an announcement, fun news, etc. If you plan to share something, please add a slide to this slide deck:

{slide_deck_url}

If you have not been added to the visitor list for the CCA, please email Adrian (aprice-whelan@flatironinstitute.org) by 15:00 today or you may not be able to enter the building!

CCA Dynamics Group website:
https://galacticdynamics.nyc/

To join the Google group:
https://groups.google.com/u/1/g/ccadynamics

""".strip()


GOOGLE_JSON = get_google_json()
SLACK_JSON = get_slack_json()
OTHER_CONFIG = get_other_config()
locals().update(OTHER_CONFIG)
