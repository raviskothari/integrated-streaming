import boto3
import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(os.environ.get('LOG_LEVEL', logging.INFO))


def handler(event, context):
    logger.info(f'Starting handler with event {event} and context {context}')
    # Add logic here
    logger.info(f'Completed processing, exiting with success')
    return 0
