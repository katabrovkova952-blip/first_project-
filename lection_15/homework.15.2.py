class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.gender}, {self.first_name} {self.last_name}, {self.age} years old."

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name} has {self.record_book} record book."

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))


class GroupError(Exception):
    pass


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupError("Максимум в групі 10 студентів")

        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.discard(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''

        for student in self.group:
            all_students += str(student) + "\n"

        return f"Number:{self.number}\n{all_students}"

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st4 = Student('Female', 20, 'Liza', 'Taylor', 'AN145')
st5 = Student('Male', 31, 'Steve', 'Дмитро', 'AN142')
st6 = Student('Female', 26, 'Liza', 'Taylor', 'AN145')
st7 = Student('Male', 38, 'Steve', 'Jobs', 'AN142')
st8 = Student('Female', 29, 'Liza', 'Taylor', 'AN145')
st9 = Student('Male', 45, 'Steve', 'Jobs', 'AN142')
st10 = Student('Female', 13, 'Liza', 'Зоря', 'AN145')
st11 = Student('Male', 32, 'Steve', 'Jobs', 'AN142')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
print(gr)
try:
    gr.add_student(st11)
except GroupError as e:
    print(e)


assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
assert gr.find_student('Jobs') == st1
