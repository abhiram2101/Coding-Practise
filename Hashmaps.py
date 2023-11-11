"""
class Hasmap :
    def __init__(self) :
        self.size =10
        #self.key = key
        #self.value = value
        self.hashmap = [[] for _ in range(0,self.size)]
        print(self.hashmap)
    def hashfun(self,key) :
        hashkey = hash(key) % self.size
        return hashkey
    def set(self, key , value ) :
        pushkey = self.hashfun(key)
        key_exists = False
        slot = self.hashmap[pushkey]
        for i , kv in enumerate(slot) :
            k,v = kv
            if key == k :
                key_exists = True
                break
        if key_exists :
            slot[i] = ((key,value))
        else :
            slot.append((key,value))
    def get(self, key) :
        pushkey = self.hashfun(key)
        slot = self.hashmap[pushkey]
        for kv in slot:
            k,v = kv
            if key == k :
                return v
            else:
                raise KeyError("key doesnot exists")
            
H = Hasmap()
H.set("value1",10)
H.set("value2",20)
H.set("value3",30)
H.set("value4",40)
H.set("value5",50)
print(H.hashmap)
print(H.get("value5"))



#<-- hash map for storing using ASCII values -->

class Hashmapp :
    def __init__(self) :
        self.size = 10
        #self.key = key
        #self.value = value
        self.hashmap = [[] for i in range(self.size)]
        #print(self.hashmap)
    def hashfun(self, key) :
        #hashed_key = hash(key)
        h=0
        for char in key :
            h+= ord(char)
        return h%self.size
    def setitem(self,key, value) :
        index = self.hashfun(key)
        self.hashmap[index] = [(key,value)]
    def getitem(self,key) :
        index = self.hashfun(key)
        for (k,v) in self.hashmap[index] :
            if key == k :
                return v
        else :
            raise KeyError('key not found!')
A = Hashmapp()
A.setitem("abhi",21)
print(A.hashmap)
A.setitem("abhi",25)# the value at key "abhi" gets updated
A.setitem("mani",22)
A.setitem("kumari",45)
print(A.hashmap)
print(A.getitem("abhi"))
print(A.getitem("mani"))
print(A.getitem("kumari"))
#print(A.getitem("Abhi")) # this key is not present A is capital

"""
# <-- closed addressing or chaining using linked list or list in python

class Hashmapp :
    def __init__(self) :
        self.size = 20
        #self.key = key
        #self.value = value
        self.hashmap = [[] for i in range(self.size)]
        #print(self.hashmap)
    def hashfun(self, key) :
        #hashed_key = hash(int(key))
        if type(key) == int :
            hashed_key = hash(key)
            return hashed_key%self.size
        else :
            h=0
            for char in key :
                h+= ord(char)
            return h%self.size
    def setitem(self,key, value) :
        index = self.hashfun(key)
        found = False
        for idx,element in enumerate(self.hashmap[index]) :
            #idx =1
#base case if the hashed index is same them add it like linked list
            
            if len(element) == 2 and element[0] == key :
                self.hashmap[index][idx] = ((key,value))
                #element[1] =value
                found = True
                break
        if not found :
            self.hashmap[index].append((key,value))
        return self.hashmap
    def getitem(self,key) :
        index = self.hashfun(key)
        for element in self.hashmap[index] :
            if element[0] == key :
                return element[1]
    def delitem(self,key) :
        index = self.hashfun(key)
        for ele,ele1 in enumerate(self.hashmap[index]) :
            if ele1[0] == key :
                del self.hashmap[index][ele]
        #return self.hashmap
"""
A = Hashmapp()
print(A.hashmap)

A.setitem("abhi",21000)
A.setitem("suresh",25000)
A.setitem("ramesh",27000)
print(A.hashmap)
print(A.getitem("abhi"))
print(A.getitem("suresh"))
print(A.getitem("ramesh"))
#print(A.delitem("abhi"))
print(A.hashmap)
print(A.getitem("abhi"))
A.setitem("abhi",21)
print(A.hashmap)
A.setitem("abhi",25)# the value at key "abhi" gets updated
A.setitem("mani",22)
A.setitem("kumari",45)
print(A.hashmap)
print(A.getitem("abhi"))
#print(A.getitem("mani"))
#print(A.getitem("kumari"))
#print(A.getitem("bhi")) # this key is not present A is capital
#print(A.hashmap)
#print(A.delitem("abhi"))
print(A.setitem("key1","value1"))
#print(A.getitem("key1"))
#print(A.delitem("key1"))
print(A.getitem("key1"))
print(A.setitem("key1",100))
print(A.getitem("key1"))
print(A.setitem("key3",600))
print(A.setitem("key3",800))
print(A.setitem("key7",600))
print(A.getitem("abhi"))
print(A.getitem("key7"))
print(A.getitem("kumari"))
print(A.hashmap)
print(A.setitem(400,64))
print(A.setitem(420,640))
print(A.hashmap)
print(A.getitem("key3"))
print(A.delitem("key3"))
print(A.getitem("key3"))

            elif len(element) == 2 and element[0] == key and element[1] != value:
                idx =self.hashfun(key)
                self.hashmap[idx].append((key,value))
                
            else :
                return None
"""
dict1 = {1,2,3,4}
dict2  = {(x,x*x ) for x in dict1}
print(dict2)



