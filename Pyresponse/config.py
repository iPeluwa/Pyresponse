import os
from dotenv import load_dotenv

load_dotenv()

ROLLBAR_ACCESS_TOKEN = os.getenv('ROLLBAR_ACCESS_TOKEN')
ROLLBAR_ENVIRONMENT = os.getenv('ROLLBAR_ENVIRONMENT')
SENTRY_DSN = os.getenv('SENTRY_DSN')
