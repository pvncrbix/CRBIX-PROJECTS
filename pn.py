class InvalidEmployeeNameException(Exception):
    def _init_(self, message):
        super()._init_(message)
def validate_employee_name(name):
    if not name.strip():
        raise InvalidEmployeeNameException("Employee name cannot be empty.")
    if not name.replace(" ", "").isalpha():
        raise InvalidEmployeeNameException(
            "Employee name must contain only alphabets and spaces."
        )
    if len(name.strip()) < 3:
        raise InvalidEmployeeNameException(
            "Employee name must have at least 3 characters."
        )
try:
    emp_name = input("Enter employee name: ")
    validate_employee_name(emp_name)
    print("Employee name is valid.")
except InvalidEmployeeNameException as e:
    print("Invalid Employee Name")
    print(e)

