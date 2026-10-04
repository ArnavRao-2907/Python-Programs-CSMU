import time
from Code.Pos_Neg_Zero_03 import pnz


assert pnz(10) == "10 \tis a Positive Number"
print("Test Case 1 Passed")

assert pnz(-5) == "-5 \tis a Negative Number"
print("Test Case 2 Passed")

assert pnz(0) == "0 \tis Zero"
print("Test Case 3 Passed")

assert pnz(100) == "100 \tis a Positive Number"
print("Test Case 4 Passed")

assert pnz(-45) =="-45 \tis a Positive Number"
print("Test Case 5 Passed")



time.sleep(2)
print("All Test Cases Passed")
