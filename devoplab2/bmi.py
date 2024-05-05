def calculate_bmi(height, weight):
    bmi = weight/(height*height)
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    print("BMI = " + str(bmi))

    if bmi > 25.0:
        return 1
    elif 18.5 <= bmi <= 25.0:
        return 0
    else:
        return -1
    return
    

def main():
    calculate_bmi()


if __name__ == "__main__":
    main()

