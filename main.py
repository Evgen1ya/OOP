class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grade = 0

    def rate_hw(self,  lecturer, course, grades):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in student.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grades]
            else:
                lecturer.grades[course] = [grades]
        else:
            return 'Ошибка'

    def __str__(self):
        for value in self.grades.values():
            self.grade = round(sum(value) / len(value), 2)
        student_name = f'''
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {self.grade}
        Курсы в процессе изучения: {self.courses_in_progress}
        Завершенные курсы: {self.finished_courses}'''
        return student_name

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        else:
            for value in self.grades.values():
                self.grade = int(sum(value) / len(value))
                return self.grade < other.grade

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []
        self.grade = 0

    def __str__(self):
        for value in self.grades.values():
            self.grade = round(sum(value) / len(value), 2)
        lecturer_name = f'''
           Имя: {self.name}
           Фамилия: {self.surname}
           Средняя оценка за лекции: {self.grade}'''
        return lecturer_name

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.grade < other.grade

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grades):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grades]
            else:
                student.grades[course] = [grades]
        else:
            return 'Ошибка'

    def __str__(self):
        reviewer_name = f'''
        Имя: {self.name}
        Фамилия: {self.surname}'''
        return reviewer_name



student = Student ("Kate", "Lee", "f")
student_2 = Student ("Mia", "Leen", "f")
student.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Python']

reviewer = Reviewer("Jam", "Kim")
reviewer_2 = Reviewer("Lana", "Kim")
reviewer.courses_attached += ['Python']
reviewer_2.courses_attached += ['Python']

lecturer = Lecturer("Ann", "Kim")
lecturer_2 = Lecturer("Jack", "Kron")
lecturer.courses_attached += ['Python']
lecturer_2.courses_attached += ['Python']

student.rate_hw(lecturer, 'Python', 10)
student.rate_hw(lecturer, 'Python', 10)
student.rate_hw(lecturer, 'Python', 10)

student.rate_hw(lecturer_2, 'Python', 10)
student.rate_hw(lecturer_2, 'Python', 10)
student.rate_hw(lecturer_2, 'Python', 9)

reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'Python', 9)

reviewer.rate_hw(student_2, 'Python', 8)
reviewer.rate_hw(student_2, 'Python', 10)
reviewer.rate_hw(student_2, 'Python', 9)

print(student.grades)
print(student_2.grades)

print(lecturer.grades)
print(lecturer_2.grades)

print(student)
print(lecturer)
print(reviewer)

print(student_2 < student)
print(lecturer < lecturer_2)


all_students = {'Python': {"Kate Lee": [10, 10, 9], "Mia Leen": [10, 8, 9]}}
def mid_grade(all_students):
    all_grades = 0
    for value in all_students.values():
        for grade in value.values():
            all_grades += sum(grade) / len(grade)
        return round(all_grades, 2) / 2


all_lecturers = {'Python': {"Ann Kim": [10, 10, 10], "Jack Kron": [10, 10, 9]}}
def mid_grade(all_lecturers):
    all_grades = 0
    for value in all_lecturers.values():
        for grade in value.values():
            all_grades += sum(grade) / len(grade)
        return round(all_grades, 2) / 2

print(mid_grade(all_students))
print(mid_grade(all_lecturers))

