dicto={"1":"hai","2":"sandeep","3":123}
print(dicto)
print(dicto["1"])

dicto["3"]=456
print(dicto)

del dicto["3"]
print(dicto)

for i in (dicto):
    print(i)
# Iterating over keys
# my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
# for key in my_dict:
#     print(key)

for i in dicto.values():
    print(i)

for i in dicto.items():
    print(i)

# Checking if a key exists
my_dict1 = {"key1": "value1", "key2": "value2", "key3": "value3"}
if "key2" in my_dict1:
    print("Key 'key2' exists")

kv=["a","b","c"]
vv=[1,2,3]
my_dict={k:v for k,v in zip(kv,vv)}
print(my_dict)

new_dict={**my_dict1,**my_dict}
print(new_dict)

#Using dictionary methods
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(my_dict.get("key2"))  # Using get() method
print(my_dict.keys())  # Using keys() method
print(my_dict.values())  # Using values() method

