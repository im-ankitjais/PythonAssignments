student_names = {"Ankit": 99, "Simran": 100, "Aayush": 67.3, "Mishal": 88, "Shikhar": 78.8, "Gautam": 65.89, "Manish": 70, "Alice": 78}
user_name = input("Enter the student's name: ")
if user_name in student_names:
    print("{}'s marks: {}".format(user_name, student_names[user_name]))
else:
    print("Student not found.")