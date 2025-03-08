class Student:
    amount_of_student = 0
    print("Hi")

    def __init__(self, scholarship=50):
        self.height = 170
        print("I am alive!")
        Student.amount_of_student += 1
        self.scholarship = scholarship
        self.scholarship += 100

class Student:
    amount_of_student = 0

    def __init__(self, name_, scholarship=50):
        self.name = name_
        self.scholarship = scholarship
        self.height = 170
        Student.amount_of_student += 1

    def __str__(self):
        return f"Student(name={self.name}, scholarship={self.scholarship}, height={self.height})"

print("-" * 10 + "Tom" + "-" * 10)
tom = Student(name_="Tom", scholarship=100)
print(tom.amount_of_student)
print(f"scholarship tom - {tom.scholarship}")
print(tom)

print("-" * 10 + "Bill" + "-" * 10)
bill = Student(name_="Bill")
print(bill.amount_of_student)
print(f"scholarship bill - {bill.scholarship}")
print(bill)

print("\n" * 4)
print(f"height Tom - {tom.height}")
print(f"height Bill - {bill.height}")

tom.height += 10
print("-" * 30)
print(f"height Tom - {tom.height}")
print(f"height Bill - {bill.height}")

