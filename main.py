students = [
    {"name" : "Hermione" , "house": "gryffindor", "patronus": "Otter"},
    {"name" : "Harry" , "house": "gryffindor", "patronus": "Stag"},
    {"name" : "Ron" , "house": "gryffindor", "patronus": "Jack Russell Terrier"},
    {"name" : "Draco" , "house": "slytherin", "patronus": None}

]

for student in students:
    print(student["name"] , "," , student["house"] , "," ,  student["patronus"])