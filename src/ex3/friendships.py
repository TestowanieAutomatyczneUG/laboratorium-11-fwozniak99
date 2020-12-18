class Friendships:
    def __init__(self):
        self.friendships = {}

    def makeFriends(self, person1, person2):
        if type(person1) is str and type(person2) is str:
            self.addFriend(person1, person2)
            self.addFriend(person2, person1)
        else:
            raise TypeError("Must be a string")

    def getFriendsList(self, person):
        if type(person) is not str:
            raise TypeError("Must be a string")
        elif person in self.friendships:
            return self.friendships[person]
        else:
            raise ValueError("There's no info about this person")

    def areFriends(self, person1, person2):
        if type(person1) is not str or type(person2) is not str:
            raise TypeError("Must be a string")
        if person1 in self.friendships and person2 in self.friendships[person1]:
            return True
        else:
            return False

    def addFriend(self, person, friend):
        if type(person) is not str or type(friend) is not str:
            raise TypeError("Must be a string")
        if person not in self.friendships:
            self.friendships[person] = [friend]
        else:
            self.friendships[person].append(friend)
