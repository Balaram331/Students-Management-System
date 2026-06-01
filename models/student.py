class Student:
    def __init__(self, name, age, student_class, phone, email):
        self.name = name
        self.age= age
        self.student_class = student_class
        self.phone = phone
        self.email = email


    def display_student(self):
        print("Student Information")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Class: {self.student_class}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        

    def convert_to_tuple(self):
        return(self.name,
               self.age,
               self.student_class,
               self.phone,
               self.email
        )