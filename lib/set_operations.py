# This module contains operations related to sets.
from student_data import students

def unique_majors(student_list):
    """
    Return a set of unique student majors using set comprehension.
    Extract the major field from each student record.
    """
    # TODO: Implement this function
    ##set comprehension
    return {student[2] for student in student_list}

print(unique_majors(students))



    # majors = set()
    # for student in student_list:
    #     majors.add(student[2])
    # #print(majors)
    # return majors

# majors = unique_majors(students)
# print(majors)
        

