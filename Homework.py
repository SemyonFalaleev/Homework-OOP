class Student:
    '''Класс Student пердназначен для создания профиля студента и хранения
    информации о его оценках , пройденных курса и курсах на которых
    он обучаеться в данный момент
    '''
    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_course = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\
        \nСредняя оценка за домашние задания: {self._average_rating()}\
        \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\
        \nЗавершенные курсы: {', '.join(self.finished_course)}"
    
    def __lt__(self, other):
        return self._average_rating() < other._average_rating()
    
    def __eq__(self, other):
        return self._average_rating() == other._average_rating()
    
    def __ne__(self, other):
        return self._average_rating() != other._average_rating()
    
    def __le__(self, other):
        return self._average_rating() <= other._average_rating()
    
    def _average_rating(self):
        return (sum((sum(self.grades.values(), start=[])))
                /len((sum(self.grades.values(), start=[]))))
    
    def rate_lectorer(self, mentor, cours, grade):
        '''Добавляет оценку(число grade) к обекту класса Mentor в словрь
        grades по ключу cours
        На вход принимает объект Mentor, строку cours, число grade
        '''
        if (isinstance(mentor, Lectorer) and cours in
        mentor.attached_courses and cours in self.courses_in_progress):
            mentor.grades.setdefault(cours, [])
            mentor.grades[cours].append(grade)
        else:
            print("Ошибка")

class Mentor:
    '''Класс ментор это родительский класс , преднозначенный для хранения
    базовой информации о преподавателе : имя, фамилия, список курсов.
    '''
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.attached_courses = []

class Reviewer(Mentor):
    '''Класс Reviewer (родительский класс Mentor) хранит информацию 
    о преподавателе: имя, фамилия, список курсов. Даёт возможность
    выставлять оценки студентам с помощью метода rate.
    '''
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate(self, student, cours, grade):
        '''Добавляет оценку(число grade) к обекту класса Student в словрь
        grades по ключу cours
        На вход принимает объект Student, строку cours, число grade
        '''
        if (isinstance(student, Student) and cours in
        student.courses_in_progress and cours in self.attached_courses):
            student.grades.setdefault(cours, [])
            student.grades[cours].append(grade)
        else:
            print("Ошибка")

class Lectorer(Mentor):
    ''''Класс Lectorer (родительский класс Mentor) хранит информацию 
    о преподавателе: имя, фамилия, список курсов , оценки за лекции. 
    Операторы сравнения для этого класса , сравнивают средние оценки 
    за лекции'''
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\
        \nСредняя оценка за лекции: {self._average_rating()}"
    
    def __lt__(self, other):
        return self._average_rating() < other._average_rating()
    
    def __eq__(self, other):
        return self._average_rating() == other._average_rating()
    
    def __ne__(self, other):
        return self._average_rating() != other._average_rating()
    
    def __le__(self, other):
        return self._average_rating() <= other._average_rating()

    def _average_rating(self):
        return (sum((sum(self.grades.values(), start=[])))
                /len((sum(self.grades.values(), start=[]))))

def hometasks_cours_rating(students, cours):
    '''Функция для подсчета средней оценки за домашние задания по всем
    студентам в рамках конкретного курса
    Принимает в качестве аргументов: список из объектов класса Student,
    название курса.Возвращает число, если такого курса нет, 
    возвращает "Ошибка".
    '''
    grades_list = []
    [grades_list.extend(stu.grades[cours]) for stu in students if 
    stu.grades.get(cours, 0) != 0]
    if sum(grades_list) == 0:
        return "Ошибка"
    else:
        return sum(grades_list)/len(grades_list)

def lector_cours_rating(lektors, cours):
    '''Функция для подсчета средней оценки за лекции по всем
    лекторам в рамках конкретного курса
    Принимает в качестве аргументов: список список из объектов класса
    Lectorer, название курса
    Возвращает число, если такого курса нет, возвращает "Ошибка".
    '''

    grades_list = []
    [grades_list.extend(lektor.grades[cours]) for lektor in lektors 
    if lektor.grades.get(cours, 0) != 0]
    if sum(grades_list) == 0:
        return "Ошибка"
    else:
        return sum(grades_list)/len(grades_list)
student_1 = Student("Ivan", "Ivanov", "male")
student_2 = Student("Semen", "Falaleev", "male")
reviewer_1 = Reviewer("Oleg", "Buligin")
reviewer_2 = Reviewer("Evgeni", "Chernov")
lector_1 = Lectorer("Elena", "Nikerina")
lector_2 = Lectorer("Georgi", "Fadeev")

student_1.courses_in_progress.append("Python")
student_1.courses_in_progress.append("Java")
student_2.courses_in_progress.append("Python")
student_2.courses_in_progress.append("Java")
reviewer_1.attached_courses.append("Python")
reviewer_2.attached_courses.append("Python")
reviewer_1.attached_courses.append("Java")
reviewer_2.attached_courses.append("Java")
lector_1.attached_courses.append("Python")
lector_1.attached_courses.append("Java")
lector_2.attached_courses.append("Python")
lector_2.attached_courses.append("Java")

student_1.rate_lectorer(lector_1, "Python", 10)
student_1.rate_lectorer(lector_1, "Java", 5)
student_2.rate_lectorer(lector_1, "Java", 8)
student_2.rate_lectorer(lector_1, "Python", 10)
student_1.rate_lectorer(lector_2, "Java", 4)
student_1.rate_lectorer(lector_2, "Python", 9)
student_2.rate_lectorer(lector_2, "Java", 8)
student_2.rate_lectorer(lector_2, "Python", 10)

reviewer_1.rate(student_1, "Java", 8)
reviewer_2.rate(student_2, "Python", 6)
reviewer_1.rate(student_2, "Java", 8)
reviewer_2.rate(student_1, "Python", 8)

students_list = [student_1, student_2]
lektors_list = [lector_1, lector_2]

print(student_1)
print(lector_1)
print(reviewer_1)
print(lector_cours_rating(lektors_list, "Python"))
print(hometasks_cours_rating(students_list, "Java"))
print(lector_cours_rating(lektors_list, "Такого курса нет"))
print(student_1 > student_2)
print(lector_1 != lector_2)

      
