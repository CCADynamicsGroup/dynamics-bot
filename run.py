# -*- coding: utf-8 -*-

from bottymcbotface import config, google, slack


def main(*args, **kwargs) -> None:
    # new_slide_deck = google.create_new_deck()
    # message = config.get_message(new_slide_deck["webViewLink"],
    message = config.get_message("test.url",
                                 config.ZOOM_LINK)
    print(message)

    # slack.post_message(message)


if __name__ == "__main__":
    main()
