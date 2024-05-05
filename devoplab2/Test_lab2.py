from Lab2 import calc_average_temperature, calc_min_max_temperature, calc_median_temperature

print("Test_Lab2")

def test_calc_average_temperature():
    # Test case 1
    assert calc_average_temperature([5, 10, 15, 20]) == 12.5
    # Test case 2
    assert calc_average_temperature([0, 0, 0, 0]) == 0
    # Test case 3
    assert calc_average_temperature([-10, 0, 10]) == 0

def test_calc_min_max_temperature():
    # Test case 1
    assert calc_min_max_temperature([5, 10, 15, 20]) == (20, 5)
    # Test case 2
    assert calc_min_max_temperature([0, 0, 0, 0]) == (0, 0)
    # Test case 3
    assert calc_min_max_temperature([-10, 0, 10]) == (10, -10)

def test_calc_median_temperature():
    # Test case 1
    assert calc_median_temperature([5, 10, 15, 20]) == 12.5
    # Test case 2
    assert calc_median_temperature([0, 0, 0, 0]) == 0
    # Test case 3
    assert calc_median_temperature([-10, 0, 10]) == 0
