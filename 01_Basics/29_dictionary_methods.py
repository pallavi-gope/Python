#Dictionary methods
d1 = {
    "fast" : "In a quick manner",
    "slow" : "In a slow manner",
    "l1" : [1, 2, 5],
    "d2" : {
        "e1" : "Hello",
        "e2" : "World"
    }
}
#1. keys() : shows the keys of the dictionary
print("Keys : ", d1.keys())
print(type(d1.keys())) #default type id dict_keys
print(list(d1.keys())) #can convert into list

#2. values() : shows the values of the dictionary
print("Values : ", d1.values())

#3. items() : show (key, values) of all the contents of the dirctionary
print("Items : ", d1.items())

#4. update(key:value) : adds the new key and values
update_dict = {
    "python" : "programming language"
}
d1.update(update_dict)
print("Updated Dictionary : ", d1)

#5. get(key) : get the value of the particular key.
# differnece between get() and [] syntax ?
print(d1.get("fast")) #returns "None" for wrong key
print(d1["fast"]) #throughs error for wrong key (Keyerror)