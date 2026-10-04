import time
from Code.Remove_Duplicates_16 import rd


assert rd([1,2]) == " {1, 2}"
print("Test Case 1 Passed")

assert rd([3,6,5,6,5,6,3,3,5,6]) == " {3, 6, 5}"
print("Test Case 2 Passed")

assert rd([1]) == " {1}"
print("Test Case 3 Passed")

assert rd([45, 1]) == " {45, 1}"
print("Test Case 4 Passed")

assert rd([0, 11, 0]) == " {0, 11}"
print("Test Case 5 Passed")




time.sleep(2)
print("All Test Cases Passed")
