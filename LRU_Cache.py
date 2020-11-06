# LRU_Cache.py
# Author Jerry Zhu
# This is my answer for BrainMaven's Task 1


from collections import OrderedDict
 
class LRU_Cache:
 
    # initialize an instance by define its maximum size
    # By the definition of "size", we have below 2 assumptions.
    # Assumption 1: the input of size is or can be transformed to type int, otherwise, it make no sense (say, size == 'Trump')
    # Assumption 2: if int(size) <= 0, it we will transform it to 0, because it may not make sense to have a LRU with size == -99
    # If above 2 assumptions can't be satisfied, code will raise ValueError
    
    def __init__(self, size):
        self.cache = OrderedDict()
        try:
            self.size = int(float(size)) if int(float(size)) > 0 else 0
        except ValueError:
            print('ValueError')
            raise
    
    # when using get method with input 'key', when key exist in cache, it will return corresponding value.
    # Also, get method with be considered use of the key, thus move the key to most recent visit
    # Assumption 3: if key not exist in cache, get method will return -1
    
    def get(self, key):
        # return -1 if key not exist in cache
        if key not in self.cache:
            return -1
        # move key-value pair to most recent
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
 
    # put method is used to add to existing LRU_Cache
    # And put operation will move the key to the end to show that it was recently used.
    # Also, we will check if the length of LRU_Cache exceed our maximum size
    # If exceed, we will remove the least recent used key-value pair.
    def put(self, key, value):
        # add new key-value pair and move to most recent used
        self.cache[key] = value
        self.cache.move_to_end(key)

        # remove least used key-value pair if cache exceed maximum size.
        if len(self.cache) > self.size:
            self.cache.popitem(last = False)
    
    # delete method will delete key if exist in cache.
    # And do no-op when key not exist in cache.
    def delete(self, key):
        # delete key if it exist in cache
        if key in self.cache:
            del self.cache[key]
        # no-op when key not exist in cache
        else:
            pass

    # reset method will remove all contents in cache
    def reset(self):
        self.cache = OrderedDict()
 
