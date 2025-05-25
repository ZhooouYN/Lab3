import employee_info as info

def test_get_employees_by_age_range():
    result = info.get_employees_by_age_range(33,40)
    assert(result ==[{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000}])

def test_calculate_average_salary():
    result = info.calculate_average_salary()
    assert (result == 60166.67)

def test_get_employees_by_dept():
    result = info.get_employees_by_dept("Engineering")
    assert result ==   [{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]