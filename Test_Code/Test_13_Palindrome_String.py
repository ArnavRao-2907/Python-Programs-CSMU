import time
from Code.Palindrome_String_13 import ps


assert ps("Ara") == "The String is a Palindrome String"
print("Test Case 1 Passed")

assert ps("rarSrar") == "The String is a Palindrome String"
print("Test Case 2 Passed")

assert ps("12r") == "The String is not a Palindrome String"
print("Test Case 3 Passed")

assert ps("12321") == "The String is a Palindrome String"
print("Test Case 4 Passed")

assert ps("9o808o90") == "The String is not a Palindrome String"
print("Test Case 5 Passed")




time.sleep(2)
print("All Test Cases Passed")
