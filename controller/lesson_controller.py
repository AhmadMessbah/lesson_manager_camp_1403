

from controller.validator import name_validator, teacher_validator,description_validator
from model.da.lesson_da import LessonDa


def save(name_lesson,teacher_name,description):
    try:
        if name_validator(name_lesson) and teacher_validator(teacher_name) and description_validator(description):
            da = LessonDa()
            da.save(name_lesson,teacher_name,description)
            return True, "Saved"
        else:
            return False, "Error : Invalid Data"
    except Exception as e:
        return False, f"Error : {e}"


def edit(id, name_lesson,teacher_name,description):
    try:
        if name_validator(name_lesson) and teacher_validator(teacher_name) and description_validator(description):
            da = LessonDa()
            da.edit(id, name_lesson,teacher_name,description)
            return True, "Edited"
        else:
            return False, "Error : Invalid Data"
    except Exception as e:
        return False, f"Error : {e}"

def remove(id):
    try:
        da = LessonDa()
        da.remove(id)
        return True, "Removed"
    except Exception as e:
        return False, f"Error : {e}"

def find_all():
    try:
        da = LessonDa()
        return True, da.find_all()
    except Exception as e:
        return False, f"Error : {e}"

def find_by_id(id):
    try:
        da = LessonDa()
        return True, da.find_by_id(id)
    except Exception as e:
        return False, f"Error : {e}"