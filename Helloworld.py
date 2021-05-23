from logging import exception
import numpy as np
import pandas as pd

nump = np.random.rand(3, 3)
my_first_series = pd.DataFrame(nump)
my_series = pd.DataFrame(nump, index=["first", "second", "third"])

print(my_series)


print(f"Hello world")


students = [
    {
        'name': 'manohar',
        'age': 29
    },
{
        'name': 'manohar1',
        'age': 30
    },
{
        'name': 'manohar2',
        'age': 31
    },
{
        'name': 'manohar3',
        'age': 32
    },
]

a = 1
b = 'as'


def get_students():

    students = ['Mark', 'James', 'Manu']

    def get_students_titlecase():
         students_titlecase = []
         for student in students:
            students_titlecase.append('Mr.'+student)
         return  students_titlecase

    student_titlecase_names = get_students_titlecase()
    print(student_titlecase_names)


def newmethod():

    try:

        tuples = (3, 5, 1, 'mark')

        myname = input('Enter your name')

        print(myname)

        print(tuples[1])

        print(a + b)

        for student in students:
            print(f"Student name is {student['name']} and age is {student['age']}")

        for student in students.keys():
            print(f"Student keys {student} ")

        for student in students.values():
            print(f"Student values {student}")

    except TypeError as ty:
        print(f'type error {ty}')
    except AttributeError as er:
        print(f'attribute error {er}')


if __name__ == "__main__":
                # newmethod()
                get_students()

        # from builtins import Exception
        #
        # students = ["a", "b"]
        #
        #
        # def get_students():
        #     try:
        #         for student in students:
        #             print(f"Names are {student}")
        #     except Exception as error:
        #         print("Something wrong " + error)
        #
        #
        # get_students()

