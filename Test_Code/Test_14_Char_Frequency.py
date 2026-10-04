import time
from Code.Char_Frequency_14 import cf


assert cf("xc") == "{'x': 1, 'c': 1}"
print("Test Case 1 Passed")

assert cf("Xx") == "{'X': 1, 'x': 1}"
print("Test Case 2 Passed")

assert cf("24hr") == "{'2': 1, '4': 1, 'h': 1, 'r': 1}"
print("Test Case 3 Passed")

assert cf("-") == "{'-': 1}"
print("Test Case 4 Passed")

assert cf("devops") == "{'d': 1, 'e': 1, 'v': 1, 'o': 1, 'p': 1, 's': 1}"
print("Test Case 5 Passed")




time.sleep(2)
print("All Test Cases Passed")
