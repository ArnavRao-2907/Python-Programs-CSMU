import time
from Code.Reverse_String_12 import rs


assert rs("xyz") == "Reverse of the String is: \tzyx"
print("Test Case 1 Passed")

assert rs("Ladu") == "Reverse of the String is: \tudaL"
print("Test Case 2 Passed")

assert rs("1234") == "Reverse of the String is: \t4321"
print("Test Case 3 Passed")

assert rs("Abc") == "Reverse of the String is: \tcbA"
print("Test Case 4 Passed")

assert rs("null") == "Reverse of the String is: \tllun"
print("Test Case 5 Passed")




time.sleep(2)
print("All Test Cases Passed")
