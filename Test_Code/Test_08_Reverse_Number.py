import time
from Code.Reverse_Number_08 import rn


assert rn(123) == "Reverse of the Number is: \t321"
print("Test Case 1 Passed")

assert rn(12321) == "Reverse of the Number is: \t12321"
print("Test Case 2 Passed")

assert rn(45123) == "Reverse of the Number is: \t32154"
print("Test Case 3 Passed")

assert rn(120) == "Reverse of the Number is: \t21"
print("Test Case 4 Passed")

assert rn(89023) == "Reverse of the Number is: \t32098"
print("Test Case 5 Passed")


time.sleep(2)
print("All Test Cases Passed")
