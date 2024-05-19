import os


class Person():  #parent

  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname


class Teacher(Person):  #child

  def __init__(self, firstname, lastname, Salary):
    super().__init__(firstname, lastname)
    self.Salary = Salary

  def teacher_details(self):
    return f"{self.firstname} {self.lastname}, ${self.Salary}"

  def check_firstname_teacher(self):
    return self.firstname    

  def update_teacher(self, firstname, lastname, Salary):
    self.firstname = firstname
    self.lastname = lastname
    self.Salary = Salary

class Student(Person):  #child

  
  def __init__(self, firstname, lastname, StudentID):
    super().__init__(firstname, lastname)
    self.StudentID = StudentID

  def student_details(self):
    return f"{self.firstname}  {self.lastname}, ID:  {self.StudentID}"

  def check_firstname_student(self):
    return self.firstname
  
  def update_student(self, firstname, lastname, StudentID):
    self.firstname = firstname
    self.lastname = lastname
    self.StudentID  = StudentID
  

record = []
choice = 0
while choice != True:
  print("--School Database--")
  print("===================")
  print("1: Create a new record")
  print("2: Read (Display) all records")
  print("3: Update records")
  print("4: Delete records")
  print("5: Exit the program")

  choice = str(input("Your choice : ")).upper()
  print("\n")
  if choice == "1":
    os.system("clear")
    flag_role_error = True
    while flag_role_error:
      try:
        role = input("Input (T)eacher or (S)tudent or (E)xit): ")
        if role == "T":
          input_firstname = input("Input firstname : ")
          input_lastname = input("Input lastname : ")
          input_salary = input("Input salary : ")

          teacher = Teacher(input_firstname, input_lastname, input_salary)
          record.append(teacher)
          print("Teacher inputted successfully")
          print("\n")
        elif role == "S":
          input_firstname = input("Input firstname : ")
          input_lastname = input("Input lastname : ")
          input_studentID = input("Input studentID : ")

          student = Student(input_firstname, input_lastname, input_studentID)
          record.append(student)
          print("Teacher inputted successfully")
          print("\n")
        elif role == "E":
          os.system('clear')
          flag_role_error = False
          break

      except ValueError:
        print("Input T or S only!")
  if choice == '2':
    os.system("clear")
    if len(record) == 0:
      print("database empty :O")
      print("\n")
    else:
      for i in range(len(record)):
        if isinstance(record[i], Teacher):
          print(Teacher.teacher_details(record[i]))
        elif isinstance(record[i], Student):
          print(Student.student_details(record[i]))
  
  
  if choice == '3':
    os.system("clear")
    if len(record) == 0:
      print("database empty :O")
      print("\n")
    else:
      firstname = input("what is the firstname of record to update: ")
      for i in range(len(record)):
        if isinstance(record[i], Teacher):
            if Teacher.check_firstname_teacher(record[i]) == firstname:
              input_firstname = input("Input firstname : ")
              input_lastname = input("Input lastname : ")
              input_salary = input("Input salary : ")
              
              Teacher.update_teacher(record[i], input_firstname, input_lastname, input_salary)
              print("Teacher data updated successfully")
              print("\n")

            else:
              print("Data does not exist")
              print("\n")

        elif isinstance(record[i], Student):
            if Student.check_firstname_student(record[i]) == firstname:
              input_firstname = input("Input firstname : ")
              input_lastname = input("Input lastname : ")
              input_studentID = input("Input studentID : ")
        
              Student.update_student(record[i], input_firstname, input_lastname, input_studentID)
              print("Student data updated successfully")
              print("\n")

            else:
              print("Data does not exist")
              print("\n")
  if choice == '4':
    os.system("clear")
    if len(record) == 0:
      print("database empty :O")
      print("\n")
    else:
      firstname = input("what is the firstname of record to delete: ")
      for i in range(len(record)):
        if isinstance(record[i], Teacher):
            if Teacher.check_firstname_teacher(record[i]) == firstname:
              del record[i]
              print("Teacher deleted successfully")
              print("\n")
        elif isinstance(record[i], Student):
            if Student.check_firstname_student(record[i]) == firstname:
              del record[i]
              print("Student deleted successfully")
              print("\n")
        else:
          print(f"Data with that {firstname} doesnt exist")
          print("\n")

  
  if choice == "5":
    print("Closing the program...")
    break
  else:
    print('Only input from 1-5 ')
    
