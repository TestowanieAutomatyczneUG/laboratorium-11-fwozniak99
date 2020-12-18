import unittest
from unittest.mock import MagicMock
from ex3.friendshipStorage import FriendshipsStorage


class TestFriendshipStorage(unittest.TestCase):

    def setUp(self):
        self.temp = FriendshipsStorage()

    def test_make_friends_2(self):
        self.temp.friendship.makeFriends = MagicMock()
        self.temp.makeFriends('filip', 'kacper')
        self.temp.friendship.makeFriends.assert_called_once_with('filip', 'kacper')

    def test_are_friends_2(self):
        self.temp.friendship.areFriends = MagicMock()
        self.temp.friendship.areFriends.return_value = True
        self.assertTrue(self.temp.areFriends('filip', 'kacper'))

    def test_get_friends_list_2(self):
        self.temp.friendship.getFriendsList = MagicMock()
        self.temp.friendship.getFriendsList.return_value = ['filip', 'kacper']
        self.assertEqual(self.temp.getFriendsList('barbara'), ['filip', 'kacper'])

    def test_add_friend_2(self):
        self.temp.friendship.addFriend = MagicMock()
        self.temp.addFriend('naruto', 'sasuke')
        self.temp.friendship.addFriend.assert_called_with('naruto', 'sasuke')

    def test_make_friends_type_error_2(self):
        self.temp.friendship.makeFriends = MagicMock()
        self.temp.friendship.makeFriends.side_effect = TypeError("Must be a string!")
        self.assertRaises(TypeError, self.temp.makeFriends, 1, 'kacper')

    def test_make_friends_type_error_3(self):
        self.temp.friendship.makeFriends = MagicMock(side_effect=TypeError("Must be a string!"))
        self.assertRaises(TypeError, self.temp.makeFriends, 1, 'kacper')

    def test_get_friends_list_error_2(self):
        self.temp.friendship.getFriendsList = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, self.temp.getFriendsList, 'czx')

    def test_get_friends_list_error_3(self):
        self.temp.friendship.getFriendsList = MagicMock(side_effect=TypeError("Must be a string!"))
        self.assertRaises(TypeError, self.temp.getFriendsList, 1)

    def tearDown(self):
        self.temp = None
