from test_employee import employee_details
def test_employee_details():
    expected output = (
        "Employee Name": "Alice\n"
        "Employee ID": "E1001\n"
        "Department": "IT\n"
        salary": "55000"
    )

assert employee_details("Alice", "E1001", "IT", 55000) == expected_output