# -*- coding: utf-8 -*-

from . import google, slack, config


def main(*args, **kwargs) -> None:
    new_file = google.create_new_deck()

    message = config.get_message(new_file["webViewLink"], config.ZOOM_LINK)

    slack.post_message(message)

    return {
        "statusCode": "200",
        "body": '{"message": "success"}',
        "headers": {"Content-Type": "application/json"},
    }
