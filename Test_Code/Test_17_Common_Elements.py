import time
from Code.Common_Elements_17 import ce


assert ce([4,5],[5,6]) == "The first list is: \t[4, 5]\nThe second list is: \t[5, 6]\nThe common elements in the two lists are: \t[5]"
print("Test Case 1 Passed")

assert ce([1],[2,3,4]) == "The first list is: \t[1]\nThe second list is: \t[2, 3, 4]\nThe common elements in the two lists are: \t[]"
print("Test Case 2 Passed")

assert ce([0,1],[0]) == "The first list is: \t[0, 1]\nThe second list is: \t[0]\nThe common elements in the two lists are: \t[0]"
print("Test Case 3 Passed")

assert ce([10, 13],[13, 10]) == "The first list is: \t[10, 13]\nThe second list is: \t[13, 10]\nThe common elements in the two lists are: \t[10, 13]"
print("Test Case 4 Passed")

assert ce([13,10],[10,13]) == "The first list is: \t[13, 10]\nThe second list is: \t[10,13]\nThe common elements in the two lists are: \t[13,10]"
print("Test Case 5 Passed")




time.sleep(2)
print("All Test Cases Passed")
