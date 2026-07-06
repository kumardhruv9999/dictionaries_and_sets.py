#Dictionary
info = {
    "key" : "value",
    "age" : "19",
    "marks" : "97.58",
    "type" : True,
}

print(info)
print(info["marks"])
info["age"] = "20"
print(info)
info["surname"] = "thor"
print(info)

#Neated dictionary
student = {
    "name" : "dhruv",
    "subjects" : {
        "maths" : "95",
        "science" : "90",
        "physics" : "95",

    }
}
print(student["subjects"]["science"])

#Methods of dictionary
student = {
    "name" : "dhruv",
    "subjects" : {
        "maths" : "95",
        "science" : "90",
        "physics" : "95",

    }
}
print(student.keys())
print(student.values())
print(student.items())
print(len(student))

student.update({"name" : "titan"})
print(student)

#Set in python
collection = {1, 2, 2, 3, "hello", "world", "hello"}
print(collection)
print(type(collection))

#Union of sets
set1 = {1, 2, 3, 4}
set2 ={3, 4, 5, 6, 7, 8}
print(set1.union(set2))
print(set1.intersection(set2))

#Practice Questions
#Q1
dictionary = {
    "table" : ["a piece of furniture", "list of facts and figures"],
    "cat" : ["a small animal"]
}
print(dictionary)

#Q2
subjects = {
    "python", "java", "c++", "python",
    "javascript", "java", "c++", "c"
}
print(subjects)
print(len(subjects))

#Q3
dic = {}
print(dic.update({"maths" : "95"}))
print(dic.update({ "sci" : "90"}))
print(dic.update({"eng" : "99"}))

print(dic.update({"maths" : "85"}))
print(dic)

print("Dictionary & Sets completed")