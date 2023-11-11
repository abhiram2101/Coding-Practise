"""
d = {}
size = 3
for i in range(size) :
    org = input("org :")
    rep = input("rep : ")
    d[org] = rep
print(d)
i =input()
if i in d.keys() :
    print(d.get(i))
print(len(d))


#import dict
d = {"A","T","C","G"}
dna = {key:[val,("T" if val == "A"
                 else "K" if val == "C"
                 else "I")]
                 for (key,val) in enumerate(d)}
print(dna)

<---   --->
d = {}
size=int(input("enter size :"))
for KEY in range(size) :
    KEY=input("enter {} th element".format(KEY))
    d[KEY] =None
#print(d)
d1 = {key:[val,("T" if val == "A"
               else "K"if val == "T"
               else "Z" if val == "C"
               else "D")] for (key,val) in enumerate(d)}
print(d)
print(d1)


#There is no elif loop in python dict but only nested if in dict comprihension else you can use loops in functins and define them in dict.

<--         -->

d= {"name" , "age" , "roll"}
details = [{key :None for key in d}]
#print(details)
#insert details into the dict using dict comprehension
sum_det = {key:[val,("abhi" if key=="name"
                     else 21 if key == "age"
                     else 580)] for (key,val) in enumerate(details)}  
print(details)
print(sum_det)
#for z in sum_det.items() :
    #print(z[1])

#<---- adding values to the keys in existing dict   ----->

d= {"name" , "age" , "roll"}
#insert details into the dict using dict comprehension
details = {key: ("abhi" if key == "name"
                 else 21 if key == "age"
                 else 580) for key in d}  
print(d)
print(details)
print(details.get("age"))
print(type(details))
inp = input()
print(details.get(inp))
print(details.keys())
print(details.values())



key_dict = {}
size=int(input("enter size :"))
for KEY in range(size) :
    KEY=input("enter {} th element".format(KEY))
    key_dict[KEY] = None
#print(key_dict)
value_dict = {key:("T" if key == "A"
               else "K"if key == "T"
               else "Z" if key == "C"
               else "D") for key in key_dict }
print(key_dict)
print("after adding vlaues to the key" , value_dict)
print(value_dict.get("T"))


#<--   -- >
#append list 2 into list 1
#now  insert these 2 using dict comprehension
lis1 = ["name" , "age" , "roll"]
lis2 = ["abhi", 21 , 580 ]
new_dict = [{key :(lis2[0] if key == "name"
                   else lis2[1] if key == "age"
                   else 580 )for key in lis1 }]
print(new_dict)

"""








host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
print(host_addresses.keys())













