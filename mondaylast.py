students = [
  {"name":"chandan","marks":10},
  {"name":"darshan", "marks":100},
  {"name":"narendra","marks":50}
  ]
students.sort(key= lambda x: x["marks"] ,reverse= True)
print(students)