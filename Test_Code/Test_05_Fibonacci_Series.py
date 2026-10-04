import time
from Code.Fibonacci_Series_05 import fs


assert fs(5) == "Fibonacci Series of 5 terms is: 1, 1, 2, 3, 5"
print("Test Case 1 Passed")

assert fs(10) == "Fibonacci Series of 10 terms is: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55"
print("Test Case 2 Passed")

assert fs(3) == "Fibonacci Series of 3 terms is: 1, 1, 2"
print("Test Case 3 Passed")

assert fs(7) == "Fibonacci Series of 7 terms is: 1, 1, 2, 3, 5, 8, 13"
print("Test Case 4 Passed")

assert fs(15) == "Fibonacci Series of 15 terms is: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610"
print("Test Case 5 Passed")


time.sleep(2)
print("All Test Cases Passed")
