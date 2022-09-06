# -*- coding: utf-8 -*-

__all__ = ["post_message"]

import requests

from . import config

MESSAGE_TEMPLATE = """<@U025P7E2F8T>

*Email to:* ccadynamics@googlegroups.com

*Email subject:* CCA Galactic Dynamics Community Meeting tomorrow

*Email body / Slack message:*
{body}
"""


def post_message(email_message):
    secrets = config.SLACK_JSON
    message = MESSAGE_TEMPLATE.format(body=email_message)
    r = requests.post(secrets["webhook_url"], json=dict(text=message))
    r.raise_for_status()
