# -*- coding: utf-8 -*-

def main(*args, **kwargs) -> None:
    from bottymcbotface import config, google, slack
    new_slide_deck = google.create_new_deck()
    message = config.get_message(new_slide_deck["webViewLink"],
                                 config.ZOOM_LINK)
    slack.post_message(email_message=message)


if __name__ == "__main__":
    import datetime

    meeting_dates = []
    with open('DATES', 'r') as f:
        for line in f:
            if line.strip():
                meeting_dates.append(datetime.date.fromisoformat(line.strip()))

    tomorrow = datetime.datetime.now().date() + datetime.timedelta(days=1)
    if tomorrow in meeting_dates:
        main()
    else:
        print("Tomorrow is not a community meeting date - skipping...")
