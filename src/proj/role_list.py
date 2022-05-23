import re

file = """
from rolepermissions.roles import AbstractUserRole

class Doctor(AbstractUserRole):
available_permissions = {
'create_medical_record': True,
}

class Nurse(AbstractUserRole):
available_permissions = {
'edit_patient_file': True,
}

class General(AbstractUserRole):
available_permissions = {
'edit_patient_file': True,
}
"""

result = re.findall(r"class\s([\w]+)", file)
print(result)
