from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def exceptions(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        return Response({
            'data': None,
            'error': {
                'errorId': response.status_code,
                'isFriendly': True,
                'errMsg': response.data.get('detail', "An error occurred.")
            },
            'success': False
        }, status=response.status_code)

    return Response({
        'data': None,
        'error': {
            'errorId': 500,
            'isFriendly': False,
            'errMsg': "Interal server error."
        },
        'success': False
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)