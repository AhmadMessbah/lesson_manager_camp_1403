import re

from controller.validator import name_validator, family_validator,grade_validator
from model.da.person_da import PersonDa


def save(name,family,grade):
    try:
        if name_validator(name) and family_validator(family) and grade_validator(grade):
            da = PersonDa()
            da.save(name,family,grade)
            return True, "Saved"
        else:
            return False, "Error : Invalid Data"
    except Exception as e:
        return False, f"Error : {e}"


def edit(id, name,family,grade):
    try:
        if name_validator(name) and name_validator(family) and grade_validator(grade):
            da = PersonDa()
            da.edit(id, name,family,grade)
            return True, "Edited"
        else:
            return False, "Error : Invalid Data"
    except Exception as e:
        return False, f"Error : {e}"

def remove(id):
    try:
        da = PersonDa()
        da.remove(id)
        return True, "Removed"
    except Exception as e:
        return False, f"Error : {e}"

def find_all():
    try:
        da = PersonDa()
        return True, da.find_all()
    except Exception as e:
        return False, f"Error : {e}"

def find_by_id(id):
    try:
        da = PersonDa()
        return True, da.find_by_id(id)
    except Exception as e:
        return False, f"Error : {e}"
