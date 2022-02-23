class Animal(object):
    def printMembers(self):
        print("Printing members of the '{}' class\n\t".format(self.name), end="")
        print("\n\t".join(self.members))