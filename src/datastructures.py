"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name,
            "age": 30,
            "lucky_numbers": [7, 14, 21]
        },
        {
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        },
        {
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": last_name,
            "age": 5,
            "lucky_numbers": [1]
        },

        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        ## you have to implement this method
        ## append the member to the list of _members
        self._members.append(member)
        return None

    def delete_member(self, id):
        ## you have to implement this method
        ## loop the list and delete the member with the given id
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return member
        return False


    def update_member(self, id, member):
        ## you have to implement this method
        ## loop the list and replace the member with the given id
        for index, mem in enumerate(self._members):
            if mem["id"] == id:
                self._members[index] = member
        return None

    def get_member(self, id):
        ## you have to implement this method
        ## loop all the members and return the one with the given id
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members


