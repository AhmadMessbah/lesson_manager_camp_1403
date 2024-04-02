import re


def name_validator(name):
    return bool(re.match(r"^[a-zA-Z\s]{3,30}$", name))

def family_validator(family):
    return bool(re.match(r"^[a-zA-Z\s]{3,30}$", family))

def grade_validator(grade):
    return bool(re.match(r"^[a-zA-Z\s]{3,30}$", grade))

def teacher_validator(teacher):
    return bool(re.match(r"^[a-zA-Z\s]{3,40}$", teacher))

def description_validator(description):
    return bool(re.match(r"^[a-zA-Z0-9\s]{2,100}$", description))
