import faculty
import storage


def create_student(name):
    print('add student clicked', name)

    # creating a person/student/...etc
    s = faculty.Student('S Name', 'Birthday', 'NID', 's number', 'dep')
    # saving object/ updating object
    storage.save(s)

    # get all saved objects of a type
    storage.get(faculty.Person)  # replace .Person with the required type
    # get saved object by national id
    storage.get_one(faculty.Teacher, 'teachers NID')
    pass
