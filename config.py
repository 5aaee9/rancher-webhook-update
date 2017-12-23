import os

def parseBoolen(readStr):
    return readStr == "true"

RANCHER_HOST = os.getenv("RANCHER_HOST", "")
RANCHER_ACCESS_KEY = os.getenv("RANCHER_ACCESS_KEY", "")
RANCHER_SCRECT_KEY = os.getenv("RANCHER_SCRECT_KEY", "")

RANCHER_PROJECT_ID = os.getenv("RANCHER_PROJECT_ID", "")
RANCHER_SERVICE_ID = os.getenv("RANCHER_SERVICE_ID", "")

WEBHOOK_PASS = os.getenv("WEBHOOK_PASS", "web_pass")
GITLAB_PASS = os.getenv("GITLAB_PASS", "")

ENABLE_TELEGRAM = parseBoolen(os.getenv("ENABLE_TELEGRAM", "true"))
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")