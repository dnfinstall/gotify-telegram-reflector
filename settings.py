import os
from dataclasses import dataclass


@dataclass
class Settings:
    GOTIFY_URL = os.environ.get("GOTIFY_URL", default="127.0.0.1")
    GOTIFY_PORT = os.environ.get("GOTIFY_PORT", default=80)
    GOTIFY_WS_SEC = os.environ.get("GOTIFY_WS_SEC", default="True") == "True"
    GOTIFY_HTTP_SEC = os.environ.get("GOTIFY_HTTP_SEC", default="True") == "True"
    GOTIFY_DENY_APPS = os.environ.get("GOTIFY_DENY_APPS", default="")
    GOTIFY_CLIENT_TOKEN = os.environ.get("GOTIFY_CLIENT_TOKEN", default="")
    GOTIFY_CLIENT_APP = os.environ.get("GOTIFY_CLIENT_APP", default="")
    TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", default="")
    TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", default="")


config = Settings()
