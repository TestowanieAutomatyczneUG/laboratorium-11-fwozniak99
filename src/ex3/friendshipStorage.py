from ex3.friendships import Friendships


class FriendshipsStorage:
    def __init__(self):
        self.friendship = Friendships()

    def makeFriends(self, person1, person2):
        self.friendship.makeFriends(person1, person2)

    def addFriend(self, person, friend):
        self.friendship.addFriend(person, friend)

    def areFriends(self, person1, person2):
        return self.friendship.areFriends(person1, person2)

    def getFriendsList(self, person):
        return self.friendship.getFriendsList(person)
