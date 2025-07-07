from random import choice


class RandomizedSet:
    def __init__(self):
        self.elements = list()
        self.indices = dict()

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.indices[val] = len(self.elements)
        self.elements.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        i = self.indices[val]
        self.elements[i], self.elements[len(self.elements) - 1] =\
            self.elements[len(self.elements) - 1], self.elements[i]
        self.indices[self.elements[i]] = i
        del self.indices[self.elements.pop()]
        return True

    def getRandom(self) -> int:
        return choice(self.elements)
