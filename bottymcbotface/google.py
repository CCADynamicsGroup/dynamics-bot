# -*- coding: utf-8 -*-

__all__ = ["create_new_deck"]

from datetime import datetime, timedelta

from google.oauth2 import service_account
from googleapiclient.discovery import build

from . import config

SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/presentations",
]


def get_date_slug():
    # Increment 1 day: meetings are on Thursday!
    return (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")


def get_filename():
    return "{0} {1}".format(config.PRESENTATION_TITLE, get_date_slug())


def get_creds():
    return service_account.Credentials.from_service_account_info(
        config.GOOGLE_JSON, scopes=SCOPES
    )


def get_drive_service():
    return build("drive", "v3", credentials=get_creds())


def get_slides_service():
    return build("slides", "v1", credentials=get_creds())


def copy_template_file(drive_service):
    # First, find the template file
    result = drive_service.files().list(
        includeItemsFromAllDrives=True,
        supportsAllDrives=True,
        q="name = '{0}'".format(config.TEMPLATE_NAME),
    ).execute()

    files = result.get("files", [])
    if not len(files) or files[0].get("name") != config.TEMPLATE_NAME:
        raise RuntimeError("can't find template file")
    file = files[0]

    # Then copy it
    new_file = drive_service.files().copy(
        fileId=file["id"],
        fields="id,webViewLink",
        supportsAllDrives=True,
        body=dict(name=get_filename()),
    ).execute()

    # Share with the Google group
    drive_service.permissions().create(
        fileId=new_file["id"],
        supportsAllDrives=True,
        sendNotificationEmail=False,
        body=dict(
            role="writer",
            type="group",
            emailAddress=config.SHARE_WITH_EMAIL,
        ),
    ).execute()

    return new_file


def update_date(presentation_file):
    requests = [
        {
            "replaceAllText": {
                "containsText": {"text": "{{today}}", "matchCase": True},
                "replaceText": get_date_slug(),
            }
        },
    ]
    (
        get_slides_service()
        .presentations()
        .batchUpdate(
            presentationId=presentation_file["id"],
            body=dict(requests=requests),
        )
        .execute()
    )


def create_new_deck():
    drive_service = get_drive_service()
    new_file = copy_template_file(drive_service)
    update_date(new_file)
    return new_file
