import unittest
from unittest import mock
from unittest.mock import patch, mock_open, Mock
from ex1.file import Files


class TestFiles(unittest.TestCase):

    def setUp(self):
        self.temp = Files()

    def test_read(self):
        open_mock_file = mock_open(read_data='line1\nline2\nline3')
        file_path = 'file1.txt'

        with patch('builtins.open', open_mock_file):
            self.assertEqual(self.temp.read(file_path), 'line1\nline2\nline3')

    def test_read_called_once_with(self):
        open_mock_file = mock_open(read_data='123')
        file_path = 'file2.txt'

        with patch('builtins.open', open_mock_file):
            self.temp.read(file_path)
            open_mock_file.assert_called_once_with(file_path, 'r+')

    def test_overwrite(self):
        open_mock_file = mock_open(read_data='text')
        file_path = 'file3.txt'

        with patch('builtins.open', open_mock_file):
            self.temp.overwrite(file_path, "new text")
            open_mock_file.assert_called_once_with(file_path, 'w+')

    @mock.patch('ex1.file.os.path')
    @mock.patch('ex1.file.os')
    def test_remove_file(self, mock_os, mock_path):
        mock_path.exists.return_value = True

        self.temp.remove_file("file4.txt")

        mock_os.remove.assert_called_with("file4.txt")

    @mock.patch('ex1.file.os')
    def test_remove_file_exception(self, mock_os):
        mock_os.path = Mock()
        mock_os.path.exists.return_value = False

        self.assertRaises(FileNotFoundError, self.temp.remove_file, "file5.txt")

    def tearDown(self):
        self.temp = None

