import time
from Code.Largest_Of_Three_02 import lot


assert lot(10, 20, 30) == "30 \tis the Largest Number"
print("Test Case 1 Passed")

assert lot(100, 50, 75) == "100 \tis the Largest Number"
print("Test Case 2 Passed")

assert lot(5, 5, 5) == "5 \tis the Largest Number"
print("Test Case 3 Passed")

assert lot(-10, -20, -5) == "-5 \tis the Largest Number"
print("Test Case 4 Passed")

assert lot(0, 0, 0) == "0 \tis the Largest Number"
print("Test Case 5 Passed")


time.sleep(2)
print("All Test Cases Passed")
