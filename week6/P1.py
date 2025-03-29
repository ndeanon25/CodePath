# In the Villager class below, each villager has a friends attribute, which is a list of other villagers they are friends with.

# Write a method get_mutuals() that takes one parameter, a Villager instance new_contact, 
# and returns a list with the name of all friends the current villager and new_contact have in common.

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        newlist =[]
        seen = self.friends
        newCon_Friends = new_contact.friends
        for friend in seen:
            if friend in newCon_Friends:
                newlist.append(friend.name)
        # mutuals = seen & newCon_Friends  friends in common
        # newlist = list[mutuals]
        return newlist



bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")

bob.friends = [stitches, raymond, fauna]
marshal.friends = [raymond, ankha, fauna]
print(bob.get_mutuals(marshal)) # raymond, fauna

ankha.friends = [marshal]
print(bob.get_mutuals(ankha))