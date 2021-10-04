# -*- coding: utf-8 -*-

from . import google, slack, mail, config


def main(*args, **kwargs) -> None:
    new_file = google.create_new_deck()
    message = """
Hello! I created a new slide deck for this week's group meeting.

Add your slide here: {0}
""".strip().format(
        new_file["webViewLink"]
    )
    slack.post_message(message)

    # TODO: get email message
    message = config.get_email_template(url, config.ZOOM_LINK)

    return {
        "statusCode": "200",
        "body": '{"message": "success"}',
        "headers": {"Content-Type": "application/json"},
    }
