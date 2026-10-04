import time
from Code.Missing_Number_18 import mn


assert mn([1,2,4,5]) == "3"
print("Test Case 1 Passed")

assert mn([1,2,3,4,5]) == "6"
print("Test Case 2 Passed")

assert mn([1,4,8]) == "-3"
print("Test Case 3 Passed")

assert mn([1,2,3,4,6]) == "5"
print("Test Case 4 Passed")

assert mn([1,3,4,5]) == "2"
print("Test Case 5 Passed")




time.sleep(2)
print("All Test Cases Passed")
