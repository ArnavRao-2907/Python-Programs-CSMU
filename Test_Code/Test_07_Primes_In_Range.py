import time
from Code.Primes_In_Range_07 import pir


assert pir(10,20) == "Prime Numbers in the Range of 10 to 20 are:\n11, 13, 17, 19"
print("Test Case 1 Passed")

assert pir(1,10) == "Prime Numbers in the Range of 1 to 10 are:\n2, 3, 5,7"
print("Test Case 2 Passed")

assert pir(1,5) == "Prime Numbers in the Range of 1 to 5 are:\n2, 3, 5"
print("Test Case 3 Passed")

assert pir(100,105) == "Prime Numbers in the Range of 100 to 105 are:\n101, 103"
print("Test Case 4 Passed")

assert pir(21,35) == "Prime Numbers in the Range of 21 to 35 are:\n23, 29, 31"
print("Test Case 5 Passed")


time.sleep(2)
print("All Test Cases Passed")
