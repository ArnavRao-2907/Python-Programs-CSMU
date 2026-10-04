import time
from Code.Second_Largest_15 import sl


assert sl([10, 20, 30, 40, 50]) == "The second largest number in the list is:\t 40"
print("Test Case 1 Passed")

assert sl([1, 2, 3, 4, 5]) == "The second largest number in the list is:\t 4"
print("Test Case 2 Passed")

assert sl([5, 4, 3, 2, 1]) == "The second largest number in the list is:\t 4"
print("Test Case 3 Passed")

assert sl([10, 10, 10, 10, 10]) == "The second largest number in the list is:\t 10"
print("Test Case 4 Passed")

assert sl([10, 93, 93, 18, 45]) == "The second largest number in the list is:\t 45"


time.sleep(2)
print("All Test Cases Passed")


