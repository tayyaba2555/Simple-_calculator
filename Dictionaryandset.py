info = {
    "name" :"khantayyaba" ,
    "subjects" : ["python" , "javascript" , "html"],
    "topics" :("dict" , "set" , "tuple"),
    "age" : 21,
    "is adult" :True,
    12.99 :56,

}
print(info)

#loops inside loops
student = {
    "name" : "khan tayyaba idris",
    "subject" : {
        "phy" : 54,
        "graphics" :56,
        "mathematics" : 69,
    }
}
print(student["subject"]["graphics"])

#Dictionary method
# 1. my dictionay keys()
student = {

 "name" : "khan tayyaba" ,
 "age" :21,
 "subjects" : {
     "phy" : 45,
     "ds" : 89, 
     "dloc" : 75,
 }
}
print(list(student.keys()))
 # 2. myDict.values()

student = {
  "name" : " khan tayyaba",
  "subject marks" : {
      "phy" : 54, 
      "chem" : 45,
      "ds" : 46,
  }
 }
print(student.values())
print(list(student.values()))

# 3. myDict.item()
student = {
"name" : " khan tayyaba",
"subject marks" : {
    "phy" : 54, 
    "chem" : 45,
      "ds" : 46,
  }
 }
print(list(student.items()))

# 4. myDict.get ("key")
student = {
"name" : " khan tayyaba",
"subject marks" : {
    "phy" : 54, 
    "chem" : 45,
      "ds" : 46,
  }
 }
print(student.get("name"))

# 5. myDict.update()
student = {
    "name" : "tayyaba",
    "city number" : {
        "delhi" : 25,
        "mumbai" : 54,
        "agrah" : 87,
    }
}
new_dict = {"pune" : 25}
student.update()
print(student)

#python in set
collection = {} #empty dictionary
print(type(collection))
print(len(collection))

collection = set()
print(type(collection))

#set method
collection.add(1)
collection.add(2)
collection.add(2)
collection.add('apna college')
collection.remove(1)
collection.clear()
print(collection)

#set.pop
collection = {"hello" , "python" , "java" , "khantayyaba"}
print(collection.pop())
print(collection.pop())

#set.union
set1 = {1 , 2  , 3}
set2 = {2, 3, 4}
print(set1.union(set2))
print(set.intersection(set2))

#store following word meaning in a python dictionaryD

dictionary = {
    "cat" : " a small animal",
    "table": ["a piece of furniture" , "list of figure and facts"]
}
print(type(dictionary))

#you are given a list of students for students. assume one classroom is required for 1 subject. how many classrooms are needed by all students

subjects = {
    "python" , "java" , "C++" , "python" , "javascript" , "java" , "python" , "java" , "c++" ,"c"
}
print(subjects)

marks = {}
x = int(input("Enter marks of phy:" ,))
y = int(input("Enter marks of chem:" ,))
z = int(input("Enter marks of maths:" ,))

print(marks)
 #figure out a way to store as the seperate values in the set.
values = {9 , "9.0"}

print(values)





