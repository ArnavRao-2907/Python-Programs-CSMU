import time
from Code.Sum_Of_Digits_10 import sod


assert sod(91) == "Sum of Digits is: \t10"
print("Test Case 1 Passed")

assert sod(93) == "Sum of Digits is: \t12"
print("Test Case 2 Passed")

assert sod(45) == "Sum of Digits is: \t9"
print("Test Case 3 Passed")

assert sod(18) == "Sum of Digits is: \t9"
print("Test Case 4 Passed")

assert sod(10) == "Sum of Digits is: \t1"
print("Test Case 5 Passed")




time.sleep(2)
print("All Test Cases Passed")
