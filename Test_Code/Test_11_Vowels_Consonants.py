import time
from Code.Vowels_Consonants_11 import vc


assert vc("1ec") == "Number of Vowels: \t1\nNumber of Consonants: \t2"
print("Test Case 1 Passed")

assert vc("AeiOu") == "Number of Vowels: \t5\nNumber of Consonants: \t0"
print("Test Case 2 Passed")

assert vc("Z3Em") == "Number of Vowels: \t1\nNumber of Consonants: \t3"
print("Test Case 3 Passed")

assert vc("1234567890") == "Number of Vowels: \t0\nNumber of Consonants: \t10"
print("Test Case 4 Passed")

assert vc("Brmn") == "Number of Vowels: \t0\nNumber of Consonants: \t4"
print("Test Case 5 Passed")




time.sleep(2)
print("All Test Cases Passed")
