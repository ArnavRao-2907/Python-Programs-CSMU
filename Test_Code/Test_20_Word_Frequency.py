import time
from Code.Word_Frequency_20 import wf


assert wf("Hello World world") == " {'Hello': 1, 'World': 1, 'world': 1}"
print("Test Case 1 Passed")

assert wf("This is is 2 Code") == "{'This': 1, 'is': 2, '2': 1, 'Code': 1}"
print("Test Case 2 Passed")

assert wf("") == ""
print("Test Case 3 Passed")

assert wf("C S M U C O L L E G e") == "{'C': 2, 'S': 1, 'M': 1, 'U': 1, 'O': 1, 'L': 2, 'E': 1, 'G': 1, 'e': 1}"
print("Test Case 4 Passed")

assert wf("") == "{}"
print("Test Case 5 Passed")




time.sleep(2)
print("All Test Cases Passed")
