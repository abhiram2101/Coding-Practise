"""
dict1 ={}
with open("poem.txt", "r") as f :
    for line in f :
        tokens = line.split(' ')
        for token in tokens :
            token = token.replace('/n', '')
            if token in dict1 :
                dict1[token] += 1
            else :
                dict1[token] = 1
print(dict1)
"""



