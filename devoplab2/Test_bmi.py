from bmi import calculate_bmi

print("Test BMI")

def test_bmi_normal_weight():
    assert(calculate_bmi(weight=66.4, height=1.75) == 0)
def test_bmi_over_weight():
    assert(calculate_bmi(weight= 100.0 , height=1.50) == 1)
def test_bmi_under_weight():
    assert(calculate_bmi(weight=52.0, height=1.84) == -1)

