""" implementation LRU using ordered dictonary """
# from collections import OrderedDict

# class LRU:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.cache = OrderedDict()

#     def get(self, key:int):
#         if key not in self.cache:
#             return -1
#         else:
#             self.cache.move_to_end(key)
#             return self.cache[key]
    
#     def put(self, key:int, value:int):
#         self.cache[key] = value
#         self.cache.move_to_end(key)
#         if len(self.cache) > self.capacity:
#             self.cache.popitem(last=False)

# LRUObj = LRU(2)
# param1 = LRUObj.get(1)
# LRUObj.put(1,1)
# LRUObj.put(2,1)
# LRUObj.put(3,1)
# LRUObj.put(3,1)



""" implementation of LRU from scratch using Doubly linked list and dictonary """
import pdb

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
        pdb.set_trace()
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        pdb.set_trace()

    #we will always insert it right
    def insert(self, node):
        print("i am inside of the insert")
        pdb.set_trace()
        prev, nxt = self.right.prev, self.right
        prev.next =  nxt.prev = node
        node.next = nxt
        node.prev = prev  
        pdb.set_trace()      

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
        pdb.set_trace()
        self.insert(self.cache[key])
        pdb.set_trace()
        if len(self.cache)> self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            pdb.set_trace()


lruObj = LRU(2)
print(lruObj.cache)
lruObj.get(1)
lruObj.put(1,1)
lruObj.put(2,2)
pdb.set_trace()
lruObj.get(1)
pdb.set_trace()
lruObj.get(2)
pdb.set_trace()
lruObj.put(3,3)
pdb.set_trace()
lruObj.put(4,4)
pdb.set_trace()
lruObj.get(3)
pdb.set_trace()
lruObj.get(4)
pdb.set_trace()