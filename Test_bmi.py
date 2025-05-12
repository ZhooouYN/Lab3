import Lab2.bmi as bmi

def test_bmi_normal_weight():
   bmi_value = 20
   result = bmi.check_bmi(bmi_value)
   if (bmi_value >= 18.5 and bmi_value <= 25.0):
        print("you are very healthy")
        return(0)
   assert(result == 0)

def test_bmi_over_weight():
   bmi_value = 30
   result = bmi.check_bmi(bmi_value)
   if (bmi_value > 25.0):
        print("you are over weight")
        return(1)
   assert(result == 1)

def test_bmi_under_weight():
   bmi_value = 11
   result = bmi.check_bmi(bmi_value)
   if (bmi_value < 18.5):
        print("you are under weight")
        return(-1)
   assert(result == -1)
