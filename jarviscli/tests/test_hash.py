import unittest
import os
from tests import PluginTest
from plugins.hash import hash_data


class HashDataTest(PluginTest):
    """
    Tests For Hash Data Plugin
    Created with help from ChatGPT
    """

    def setUp(self):
        self.test = self.load_plugin(hash_data)

    def test_hash_string(self):
        # Set predefined input values
        self.queue_input('string')
        self.queue_input('md5')
        self.queue_input('Hello, World!')

        # Run the plugin method
        self.test(self.jarvis_api, "")

        # Check the output
        expected_output = 'Hashed result: 65a8e27d8879283831b664bd8b7f0ad4'
        self.assertEqual(self.history_say().last_text(), expected_output)

    def test_hash_file_invalid_path(self):
        # Set predefined input values
        self.queue_input('file')
        self.queue_input('sha256')
        self.queue_input('nonexistent_file.txt')

        # Run the plugin method
        self.test(self.jarvis_api, "")

        # Check the output
        expected_output = 'Hashed result: Error: File not found or inaccessible.'
        self.assertEqual(self.history_say().last_text(), expected_output)

    def test_hash_file_valid_path(self):
        # Create a temporary test file
        with open("test_file.txt", "w") as file:
            file.write("This is a test file.")

        # Set predefined input values
        self.queue_input('file')
        self.queue_input('md5')
        self.queue_input('test_file.txt')

        # Run the plugin method
        self.test(self.jarvis_api, "")

        # Check the output
        expected_output = 'Hashed result: 3de8f8b0dc94b8c2230fab9ec0ba0506'
        self.assertEqual(self.history_say().last_text(), expected_output)

        # Clean up created file
        if os.path.isfile('test_file.txt'):
            os.remove('test_file.txt')


if __name__ == '__main__':
    unittest.main()