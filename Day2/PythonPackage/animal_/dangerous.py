from animal2 import Animal

class Mammals(Animal):
    def __init__(self):
        self.name = "Mammals"
        self.members = ["Lion", "Leopard", "Human"]

class Fish(Animal):
    def __init__(self):
        self.name = "Fish"
        self.members = ["Whale", "Shark", ]