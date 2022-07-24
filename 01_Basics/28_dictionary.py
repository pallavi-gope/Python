# Dictionary : Dictionary is a collection of key value pair.
# Properties of dictionary -
#1. It is unordered
#2. It is mutable
#3. It is indexed
#4. Cannot contain duplicate keys

#creating a dictionary
d1 = {
    "fast" : "In a quick manner",
    "slow" : "In a slow manner",
    "l1" : [1, 2, 5],
    "d2" : {
        "e1" : "Hello",
        "e2" : "World"
    }
}

#accessing the dictionary values with their key
print(d1["l1"])
print(d1["d2"])
print(d1["d2"]["e2"])

for i in d1["l1"]:
    print(i)

