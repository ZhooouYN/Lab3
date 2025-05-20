import Lab2.bmi as bmi


def test_bmi_normal_weight():
   bmi_value = 20
   result = bmi.check_bmi(bmi_value)

   assert(result == 0)

def test_bmi_over_weight():
   bmi_value = 30
   result = bmi.check_bmi(bmi_value)

   assert(result == 1)

def test_bmi_under_weight():
   bmi_value = 11
   result = bmi.check_bmi(bmi_value)

   assert(result == -1)

def test_calculate_bmi():
   bmi_value= bmi.calculate_bmi(1.7, 50)

   assert(bmi_value==17.3)
