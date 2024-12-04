import random

class RandomizedSet(object):

    def __init__(self):
        self.lst = []
        self.index_map = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.index_map:
            self.lst.append(val)
            self.index_map[val] = len(self.lst) - 1
            return True
        else:
            return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.index_map:
            # Swap the element with the last one to remove it efficiently
            last_element = self.lst[-1]
            index_to_remove = self.index_map[val]
            self.lst[index_to_remove] = last_element
            self.index_map[last_element] = index_to_remove
            self.lst.pop()
            del self.index_map[val]
            return True
        return False

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.lst)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
