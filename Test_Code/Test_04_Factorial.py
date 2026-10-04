import time
from Code.Factorial_04 import f


assert f(1) == "Factorial of 1 is 1"
print("Test Case 1 Passed")

assert f(5) == "Factorial of 5 is 120"
print("Test Case 2 Passed")

assert f(0) == "Factorial of 0 is 1"
print("Test Case 3 Passed")

assert f(10) == "Factorial of 10 is 3628800"
print("Test Case 4 Passed")

assert f(7) == "Factorial of 7 is 5040"
print("Test Case 5 Passed")


time.sleep(2)
print("All Test Cases Passed")
