def calculate_bmi(height, weight):
    bmi = weight/(height*height)
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    print("BMI = " + str(bmi))

    if bmi > 25.0:
        print("Overweight")
    elif 18.5 <= bmi <= 25.0:
        print("Normal")
    else:
        print("Underweight")

calculate_bmi(weight=66.4, height=1.70)

