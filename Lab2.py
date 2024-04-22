def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32): ")

def get_user_input():
    txt = input()
    x = txt.split(",")
    x = [float(i) for i in x]
    return x

def calc_average_temperature(x):
    length = len(x)
    y = sum(x)
    avg = y/length
    print("Average temp: "+ str(avg))

def calc_min_max_temperature(x):
    print("Max value: " + str(max(x)))
    print("Min val: " + str(min(x)))

def calc_median_temperature(x):
    n = len(x)
    x.sort()
    if n % 2 == 1:
        return x[n//2]
    return (x[n//2]+x[n//2 - 1])/2


def main():
    display_main_menu()
    x = get_user_input()
    calc_average_temperature(x)
    calc_min_max_temperature(x)
    calc_median_temperature(x)
    print("Median temp is " + str(calc_median_temperature(x)))

main()

    