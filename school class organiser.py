# --- School Class Organizer ---

# STEP 1 - Create a list of classmaes
classmates = ["Aarav" , "Priya", "Rahul", "Sneha" , "Dev"]
print("Class list:" , classmates)

# STEP 2 - Acess the list
print("total students:", len(classmates))
print("First student:", classmates[0])
print("Last student:", classmates[-1])
print("First three:", classmates[:3])

# STEP 3 -MODIFY the list
classmates.append("Meera")
print("\nAfter adding Meera:", classmates)
print("\nAfter removing Dev:" , classmates)
classmates.sort()
print("Sorted alphabetically:" , classmates)
classmates.reverse()
print("Reversed:" , classmates)


# STEP 4 -create a teacher dictionary
teacher = {"name": "Mr. Sharma" , "subject" : "Python" , "experience" : 5}
print("\nTeacher profile:" , teacher)

# STEP 5 - Dictionary operations
print("subject:", teacher["subject"])
print("Experience:" , teacher.get("Experience" , "Not found"))
teacher["experience"] = 6
teacher ["email"] = "sharma@school.com"
teacher.pop("experience")
print("Updated teacher profile:" , teacher)

# STEP 6 - Convert lists to a student directory
roll_numbers = [1 ,2 ,3, 4 ,5]
names = ["Aarav" , "Priya", "Rahul" "Sneha" , "Meera"]
student_directory = dict(zip(roll_numbers, names))
print("n\Student Directory:" , student_directory)
print("student at Roll 3:", student_directory[3])