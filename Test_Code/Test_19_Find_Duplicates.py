import time
from Code.Find_Duplicates_19 import fd


assert fd([1,2,3,2]) == "2"
print("Test Case 1 Passed")

assert fd([1,43,2,3,2,43]) == "2\n43"
print("Test Case 2 Passed")

assert fd([1,10,4]) == None
print("Test Case 3 Passed")

assert fd([2,4,2,6,8]) == "2"
print("Test Case 4 Passed")

assert fd([1,0,2,0,5]) == "0"
print("Test Case 5 Passed")




time.sleep(2)
print("All Test Cases Passed")
