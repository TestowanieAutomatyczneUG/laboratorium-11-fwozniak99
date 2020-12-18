import unittest
from ex3.friendships import Friendships


class TestFriendships(unittest.TestCase):

    def setUp(self):
        self.temp = Friendships()

    def test_make_friends(self):
        self.temp.makeFriends('filip', 'kacper')
        self.assertEqual(self.temp.friendships, {'filip': ['kacper'], 'kacper': ['filip']})

    def test_add_friend(self):
        self.temp.addFriend('filip', 'marcin')
        self.assertEqual(self.temp.friendships, {'filip': ['marcin']})

    def test_are_friends_true(self):
        self.temp.friendships = {'marcin': ['weronika', 'andrzej'], 'kamil': ['tyler']}
        self.assertTrue(self.temp.areFriends('marcin', 'weronika'))

    def test_are_friends_False(self):
        self.temp.friendships = {'marcin': ['weronika', 'andrzej'], 'kamil': ['tyler']}
        self.assertFalse(self.temp.areFriends('marcin', 'filip'))

    def test_get_friends_list(self):
        self.temp.friendships = {'marcin': ['weronika', 'andrzej'], 'kamil': ['tyler']}
        self.assertEqual(self.temp.getFriendsList('kamil'), ['tyler'])

    def test_make_friends_type_error(self):
        self.assertRaises(TypeError, self.temp.makeFriends, 1, 'kacper')

    def test_add_friend_type_error(self):
        self.assertRaises(TypeError, self.temp.addFriend, 1, 'kacper')

    def test_are_friends_type_error(self):
        self.assertRaises(TypeError, self.temp.areFriends, 1, 'kacper')

    def test_get_friends_list_type_error(self):
        self.assertRaises(TypeError, self.temp.getFriendsList, 1)

    def test_get_friends_list_value_error(self):
        self.temp.friendships = {'marcin': ['weronika', 'andrzej'], 'kamil': ['tyler']}
        self.assertRaises(ValueError, self.temp.getFriendsList, 'kacper')

    def tearDown(self):
        self.temp = None
