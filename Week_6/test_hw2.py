import unittest
import hw2

from unittest.mock import patch

class LoggingTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    # @patch('hw2.log_error')
    # def test_format_command_exception(self, mock_log_error):
    #     mock_log_error.side_effect = ValueError
    #     with self.assertRaises(ValueError):
    #         hw2.log_error("Log message to write")
    #         mock_log_error.assert_called_once()

    @patch('hw2.log_error')
    def test_format_command(self, mock_log_error):
        
        query_template = 'SELECT indian {alias} FROM {env}codebase '
        query_context = {"alias": "Python", "env": "dev_"}
        self.assertEqual(
            hw2.get_command_with_context(query_template, query_context),
            'SELECT indian Python FROM dev_codebase'
        )

        query_template = 'SELECT spanish {alias} FROM {env}codebase '
        query_context = {"alias": "Java", "env": "prod_", "source": "Python"}
        self.assertEqual(
            hw2.get_command_with_context(query_template, query_context),
            'SELECT spanish Java FROM prod_codebase'
        )

        query_template = 'SELECT spanish {source} FROM {env}codebase '
        query_context = {"alias": "Java", "env": "prod_", "source": "Python"}
        self.assertNotEqual(
            hw2.get_command_with_context(query_template, query_context),
            'SELECT spanish Java FROM prod_codebase'
        )

    @patch('hw2.log_error')
    def test_invalid_context(self, mock_log_error):
        query_template = 'SELECT indian {alias} FROM {env}codebase '
        query_context = {"source": "Python", "env": "dev_"}
        hw2.get_command_with_context(query_template, query_context)

        mock_log_error.assert_called_once()
        mock_log_error.assert_called_with("Error when try to formatting query: 'alias'")
    

if __name__ == '__main__':
    unittest.main()
