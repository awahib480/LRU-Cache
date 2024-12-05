class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, maxsize):
        self.dict = {}  #to get the value of key from linked list
        self.size = maxsize
        self.miss = 0
        self.access = 0
        self.head = None  #most recently used
        self.tail = None  #least recently used

    def get(self, key):
        self.access += 1
        if key in self.dict:
            node = self.dict[key]
            temp = node.val
            self._moveToHead(node)
            return temp
        else:
            self.miss += 1
            return -1  #if not found

    def put(self, key, value):
        self.access += 1
        if key in self.dict:  #update the value of key
            node = self.dict[key]
            node.val = value
            self._moveToHead(node)  #marks as recently used
        else:
            self.miss += 1
            node = ListNode(key, value)
            if len(self.dict) == self.size:
                lru_key = self.tail.key
                self._removeNode(self.tail)  #remove node from list
                del self.dict[lru_key]  #evicts LRU
            self._addToHead(node)  #recently used
            self.dict[key] = node  #adds new pair in dict

    def missRate(self):
        if self.access == 0:
            print(f"Access: 0\nMisses: 0\nMiss Rate: 0.00%\n")
            return
        print("Accesses:", self.access)
        print("Misses:", self.miss)
        print(f'Miss Rate: {(self.miss/self.access)*100:.2f}%\n')


    #Helper functions
    def _moveToHead(self, node):
        self._removeNode(node)
        self._addToHead(node)

    def _removeNode(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next  #if head node
        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev  #if tail node

    def _addToHead(self, node):
        node.next = self.head
        node.prev = None
        if self.head is not None:
            self.head.prev = node
        else:
            self.tail = node  #if empty list
        self.head = node  #update head pointer



#Task
cache = LRUCache(50)  #Initialize a cache of size 50
for i in range(50):  #Put 0-49 keys
    cache.put(i,i)
cache.missRate()

for i in range(50):  #Retrieve odd keys
    if i%2 != 0:
        cache.get(i)
cache.missRate()

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for i in prime:
    cache.put(i,i)  #Put prime number keys from 0-100
cache.missRate()  #Calculate final miss rate



# cache = LRUCache(5)
# cache.put(1,1)
# cache.put(2,2)
# cache.get(3)
# cache.missRate()
# cache.put(3,3)
# cache.put(4,4)
# cache.put(5,5)
# cache.put(6,6)
# cache.missRate()
# cache.get(2)
# cache.missRate()
