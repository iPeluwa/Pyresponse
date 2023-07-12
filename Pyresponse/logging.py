import logging
import rollbar
import sentry_sdk
from config import SENTRY_DSN, ROLLBAR_ACCESS_TOKEN, ROLLBAR_ENVIRONMENT


def configure_logging():
    # Configure Rollbar
    rollbar.init(ROLLBAR_ACCESS_TOKEN, environment=ROLLBAR_ENVIRONMENT)

    # Set up the logging handler for Rollbar
    rollbar_handler = rollbar.LogHandler()
    rollbar_handler.setLevel(logging.ERROR)

    # Configure Sentry
    sentry_sdk.init(dsn=SENTRY_DSN)

    # Set up the logging handler for Sentry
    sentry_handler = sentry_sdk.integrations.logging.EventHandler()
    sentry_handler.setLevel(logging.ERROR)

    # Set up the logger
    logger = logging.getLogger(__name__)
    logger.addHandler(rollbar_handler)
    logger.addHandler(sentry_handler)
