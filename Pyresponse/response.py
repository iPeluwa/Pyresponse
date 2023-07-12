from rest_framework import status
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)


def create_success_response(data=None, message=None, status_code=None, serializer=None, **kwargs):
    response_data = {
        'success': True,
        'message': message,
        'data': data or []
    }
    response_data.update(kwargs)

    logger.info('Success Response: %s', response_data)

    return Response(response_data, status=status_code)


def create_error_response(message=None, data=None, status_code=None, serializer=None, **kwargs):
    response_data = {
        'success': False,
        'message': message,
        'data': data or []
    }
    response_data.update(kwargs)

    logger.error('Error Response: %s', response_data)

    return Response(response_data, status=status_code)
