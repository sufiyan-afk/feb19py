
           # dictionary methods  that are majorly used in programming
# myDict.keys()                   # returns all keys 
# myDict.values()                 # returns all values
# myDict.items()                  # returns all (key,value) pair as a tuple
# myDict.get("keys")             # returns the key according to value
# myDict.update(newDict)          # inserts the specified items to the dictionary


student = {
    "name":"Sufiyan",
    "age":24,
    "roll no": 49,
    "subject": {
        "frontend":["HTML","CSS","Javascript","React.js"],
        "backend":["Python","Django","RestAPi"],
        "database": "MySQL"
    }
}


student.keys()
print(student)

print(list(student))
print(list(student["subject"]))

# k = student.values()
# print(k)

print(list(student.values()))

# print(student["name2"])   # it will return error
print(student.get("name2"))   # no error --> none


#print(student.pop("name"))     # this will give return value as sufiyan 

student.pop("name")
print(student)                 #this 2 steps will remove the key and will not return anything

