import os

RANCHER_HOST = os.getenv("RANCHER_HOST", "")
RANCHER_ACCESS_KEY = os.getenv("RANCHER_ACCESS_KEY", "")
RANCHER_SCRECT_KEY = os.getenv("RANCHER_SCRECT_KEY", "")

RANCHER_PROJECT_ID = os.getenv("RANCHER_PROJECT_ID", "")
RANCHER_SERVICE_ID = os.getenv("RANCHER_SERVICE_ID", "")

WEBHOOK_PASS = os.getenv("WEBHOOK_PASS", "web_pass")
GITLAB_PASS = os.getenv("GITLAB_PASS", "")