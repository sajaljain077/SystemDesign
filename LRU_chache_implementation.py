# """ implementation LRU using ordered dictonary """
from collections import OrderedDict

class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key:int):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
    
    def put(self, key:int, value:int):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# # LRUObj = LRU(2)
# # param1 = LRUObj.get(1)
# # LRUObj.put(1,1)
# # LRUObj.put(2,1)
# # LRUObj.put(3,1)
# # LRUObj.put(3,1)



# """ implementation of LRU from scratch using Doubly linked list and dictonary """
# import pdb

class Node:
    #this is goig to be our doubly linkeed list
    #LRU to MRU
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev, self.next = None, None

class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} # here we are going to map the key to the node

        #here we inintilazing some node Here left will be LRU and right will be MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    #remove from the start 
    def remove(self, node):
        print("i am inside of the remove")
        
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        

    #we will always insert it right
    def insert(self, node):
        print("i am inside of the insert")
        
        prev, nxt = self.right.prev, self.right
        prev.next =  nxt.prev = node
        node.next = nxt
        node.prev = prev  
              

    def get(self, key:int):
        if key in self.cache:
            #TODO here we need to change the order inside the linked list
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value  
        return -1
    
    def put(self, key:int, value:int):
        if key in self.cache:
            print("i am inside of the loop where we are cheking the value inside the cache")
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        
        self.insert(self.cache[key])
        
        if len(self.cache)> self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            


# lruObj = LRU(2)
# print(lruObj.cache)
# lruObj.get(1)
# lruObj.put(1,1)
# lruObj.put(2,2)
# 
# lruObj.get(1)
# 
# lruObj.get(2)
# 
# lruObj.put(3,3)
# 
# lruObj.put(4,4)
# 
# lruObj.get(3)
# 
# lruObj.get(4)
# 



from abc import ABC, abstractmethod

class Student(ABC):

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def sirname(self):
        pass

class Sajal(Student):
    def name(self):
        print("this is Sajal object")
    def sirname(self):
        pass

obj = Sajal()
obj.name()