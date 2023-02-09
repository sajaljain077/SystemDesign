
# Nearest Grater to left
# arr = [1,3,2,4]

# stack = []
# op = []

# for i in range(len(arr)):
#     if len(stack) == 0:
#         op.append(-1)
#     elif len(stack) > 0 and arr[i] < stack[-1]:
#         op.append(stack[-1])
#     elif len(stack) > 0 and arr[i] >= stack[-1]:
#         while len(stack) > 0 and arr[i] >= stack[-1]:
#             stack.pop()
#         if len(stack) == 0:
#             op.append(-1)
#         else:
#             op.append(stack[-1])
#     stack.append(arr[i])
# # print(op)


# #Nearest smaller to left
# arr = [6,2,5,4,5,1,6]

# stack = []
# op = []

# for i in range(len(arr)):
#     if len(stack) == 0:
#         op.append(-1)
#     elif len(stack) > 0 and arr[i] > stack[-1]:
#         op.append(stack[-1])
#     elif len(stack) > 0 and  stack[-1] >= arr[i]:
#         while len(stack) > 0 and stack[-1] >= arr[i]:
#             stack.pop()
#         if len(stack) == 0:
#             op.append(-1)
#         else:
#             op.append(stack[-1])
#     stack.append(arr[i])
# # print(op)

# #Nearest smaller to right
# arr = [6,2,5,4,5,1,6]

# stack = []
# op = []

# for i in range(len(arr)-1, -1, -1):
#     if len(stack) == 0:
#         op.append(-1)
#     elif len(stack) > 0 and arr[i] > stack[-1]:
#         op.append(stack[-1])
#     elif len(stack) > 0 and  stack[-1] >= arr[i]:
#         while len(stack) > 0 and stack[-1] >= arr[i]:
#             stack.pop()
#         if len(stack) == 0:
#             op.append(-1)
#         else:
#             op.append(stack[-1])
#     stack.append(arr[i])

# # print(op[::-1])


# # Histogram question

# arr = [6,2,5,4,5,1,6]

# opLeft = []
# stackLeft = []
# for i in range(len(arr)):
#     if len(stackLeft) == 0:
#         opLeft.append(-1)
#     elif len(stackLeft) > 0 and stackLeft[-1][0] < arr[i]:
#         opLeft.append(stackLeft[-1][1])
#     elif len(stackLeft) > 0 and stackLeft[-1][0] >= arr[i]:
#         while len(stackLeft) > 0 and stackLeft[-1][0] >= arr[i]:
#             stackLeft.pop()
#         if len(stackLeft) == 0:
#             opLeft.append(-1)
#         else:
#             opLeft.append(stackLeft[-1][1])
#     stackLeft.append((arr[i], i))

# opRight = []
# stackRight = []

# for i in range(len(arr)-1, -1, -1):
#     if len(stackRight) == 0:
#         opRight.append(len(arr))
#     elif len(stackRight)>0 and stackRight[-1][0]< arr[i]:
#         opRight.append(stackRight[-1][1])
#     elif len(stackRight)>0 and stackRight[-1][0] >= arr[i]:
#         while len(stackRight) > 0 and stackRight[-1][0] >= arr[i]:
#             stackRight.pop()
#         if len(stackRight) == 0:
#             opRight.append(len(arr))
#         else:
#             opRight.append(stackRight[-1][1])
#     stackRight.append((arr[i], i))

# opRight = opRight[::-1]
# area = []

# for i in range(len(arr)):
#     area.append((opRight[i]-opLeft[i]-1)*arr[i])

# maximum of sub array
# arr = [2,5,1,8,2,9,1]
# i , j, k = 0, 0, 3
# sum = 0
# maxSum = 0
# while j < len(arr):
#     sum += arr[j]
#     if j-i+1 < k:
#         j+=1
#     elif j-i+1 == k:
#         maxSum = max(sum, maxSum)
#         sum-=arr[i]
#         i+=1
#         j+=1

# first negative window
# arr = [12,-1,-7,8,-15,30,16,28]
# k = 3
# i = 0
# j = 0
# neg = []
# op = []
# while i < len(arr):
#     print(neg)
#     if arr[i] < 0:
#         neg.append(arr[i])
#     if i-j+1 < k:
#         i += 1
#     elif i-j+1 ==  k:
#         if len(neg) == 0:
#             op.append(0)
#         else:
#             if neg[0] == arr[j]:
#                 op.append(neg.pop(0))
#             else:
#                 op.append(neg[0])
#         j+=1
#         i+=1
# print(op)
        
# s = "aabaabaa"
# p = "aaba"

# pCount, sCount = {}, {}
# for i in range(len(p)):
#     pCount[p[i]] = 1 + pCount.get(p[i], 0)
#     sCount[s[i]] = 1 + sCount.get(s[i], 0)
# res = [0] if pCount == sCount else []
# l = 0
# for r in range(len(p), len(s)):
#     sCount[s[r]] += 1 + sCount.get(s[r], 0)
#     sCount[s[l]] -= 1
#     if sCount[s[l]] == 0:
#         sCount.pop(s[l])
#     if sCount == pCount:
#         res.append(l)
#     l+=1
# print(res)

# for i in range(len(arr)-k):
#     for k in range(i, i+k):
#         if arr[k]<0:
#             print(arr[k])
#             break



# arr = [12,-1,-7,8,-15,30,16,28]
# k = 3
# i = 0
# j = 0
# neg = []
# op = []
# while i < len(arr):
#     print(i, j)
#     if arr[i] < 0:
#         neg.append(arr[i])
#     if i-j+1<k:
#         i+=1
#     elif i-j+1 == k:
#         if len(neg)==0:
#             op.append(0)
#         else:
#             if arr[j] == neg[0]:
#                 op.append(neg.pop(0))
#             else:
#                 op.append(neg[0])
#         i+=1
#         j+=1
# print(op)



# class Queue:
#    def __init__(self):
#       self.queue = list()
#    def addtoq(self,dataval):
# # Insert method to add element
#     if dataval not in self.queue:
#         self.queue.insert(0,dataval)
#         return True
#     return False

#    def size(self):
#       return len(self.queue)

# TheQueue = Queue()
# TheQueue.addtoq("Mon")
# TheQueue.addtoq("Tue")
# TheQueue.addtoq("Tue")
# print(TheQueue.size()) 

# class Stack:
#    def __init__(self):
#       self.stack = []

#    def add(self, dataval):
# # Use list append method to add element
#       if dataval not in self.stack:
#          self.stack.append(dataval)
#          return True
#       else:
#          return False
# # Use peek to look at the top of the stack
#    def peek(self):     
# 	   return self.stack[-1]

# AStack = Stack()
# AStack.add("Mon")
# AStack.add("Tue")
# AStack.peek()
# print(AStack.peek())
# AStack.add("Wed")
# AStack.add("Mon")
# print(AStack.peek())






# i, j, summ, maxsum = 0, 0, 0, 0
# target = 5
# arr = [4,1,1,1,2,3,5]

# while i < len(arr):
#     summ+=arr[i]
#     if summ < target:
#         i+=1
#     elif summ == target:
#         maxsum = max(maxsum, i-j+1)
#         i+=1
#     elif summ > target:
#         while summ > target:
#             summ -= arr[j]
#             j+=1
#             if summ == target:
#                 maxsum = max(maxsum, i-j+1)
#         i+=1

s = 'aabacbebebe'
k = 3 
ocnt = {}
j = 0
i = 0
maxsize = 0
while i < len(s):
    ocnt[s[i]] = 1 + ocnt.get(s[i], 0)
    if len(ocnt) < k:
        i+=1
    elif len(ocnt) == k:
        maxsize = max(maxsize, i-j+1)
        i += 1
    elif len(ocnt) > k:
        while len(ocnt) > k:
            ocnt[s[j]] -= 1
            if ocnt[s[j]] == 0:
                ocnt.pop(s[j])
            j+=1
        if len(ocnt) == k:
            maxsize = max(maxsize, i-j+1)
        i+=1
print(maxsize)
