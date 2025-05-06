import Lab2.bmi as bmi

def test_bmi_normal_weight():
   assert(bmi == 0)
def test_bmi_over_weight():
   assert(bmi == 1)
def test_bmi_under_weight():
   assert(bmi == 1)
