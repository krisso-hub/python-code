class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_pass(self):
        if self.marks > 50:
            return True
        else:
            return False

st1 = Student("John", 60)
print(st1.name)
print(st1.marks)
did_pass = st1.check_pass()
print(did_pass)
print('-----------')
st2 = Student("matt", 48)
print(st2.name)
print(st2.marks)
did_pass = st2.check_pass()
print(did_pass)