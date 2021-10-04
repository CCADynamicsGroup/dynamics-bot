# -*- coding: utf-8 -*-

from bottymcbotface import config, google, slack


def main(*args, **kwargs) -> None:
    new_slide_deck = google.create_new_deck()
    message = config.get_message(new_slide_deck["webViewLink"],
                                 config.ZOOM_LINK)
    slack.post_message(email_message=message)


if __name__ == "__main__":
    main()
