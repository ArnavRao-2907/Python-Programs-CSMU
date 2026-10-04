import time
from Code.Even_Odd_01 import eo


assert eo(10) == "10 \tis an Even Number"
print("Test Case 1 Passed")

assert eo(18) == "18 \tis an Even Number"
print("Test Case 2 Passed")

assert eo(45) == "45 \tis an Odd Number"
print("Test Case 3 Passed")

assert eo(93) == "93 \tis an Odd Number"
print("Test Case 4 Passed")

assert eo(0) == "0 \tis an Even Number"
print("Test Case 5 Passed")


time.sleep(2)
print("All Test Cases Passed")