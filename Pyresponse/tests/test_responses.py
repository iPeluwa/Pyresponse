"""
Unit tests for response module in PyResponse package.
"""

import unittest
from Pyresponse.response import create_success_response, create_error_response
from Pyresponse.logging import configure_logging


class ResponseFunctionsTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Set up logging for tests.
        """
        configure_logging()

    def test_create_success_response(self):
        """
        Test create_success_response function.
        """
        data = {'key': 'value'}
        message = 'Success message'
        status_code = 200
        expected_response = {
            'success': True,
            'message': message,
            'data': data
        }

        response = create_success_response(
            data=data, message=message, status_code=status_code)

        self.assertEqual(response.status_code, status_code)
        self.assertEqual(response.data, expected_response)

    def test_create_error_response(self):
        """
        Test create_error_response function.
        """
        message = 'Error message'
        status_code = 400
        expected_response = {
            'success': False,
            'message': message,
            'data': []
        }

        response = create_error_response(
            message=message, status_code=status_code)

        self.assertEqual(response.status_code, status_code)
        self.assertEqual(response.data, expected_response)


if __name__ == '__main__':
    unittest.main()
