class RandomizedSet(object):

    def __init__(self):
        self.lst=[]
        self.index_map={}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.index_map:
             self.lst.append(val)
             self.index_map[val]=len(self.lst)-1
             return True

        else:
             return False 

        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.index_map:
            del self.index_map[val]
            self.lst.remove(val)
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