from lib.student_data import students
from lib.data_processing import display_students
# This module contains functions for filtering student data.

def filter_students_by_major(student_list, major):
    """
    Return a filtered list of students by major using a list comprehension.
    The function should:
    - Check if a student's major matches the given major (case insensitive).
    - Return a new list containing only students that match.
    """
    # TODO: Implement this function
    #list comprehension
    filtered_student = [student for student in student_list if student[2]==major]
    if filtered_student:
        print(f"\nStudents majoring in {major}")
        display_students(filtered_student)
    else:
        print(f"\nNo student majoring in {major}")

    return filtered_student

#filter_students_by_major(students, "Computer Science")