import time
from Code.Prime_Number_06 import pn


assert pn(5) == "5 is a Prime Number\nNmber of factors of: 5 is \t2"
print("Test Case 1 Passed")

assert pn(1) == "1 is not a Prime Number, and is a Co-Prime Number\nNumber of factors of: 1 is \t1"
print("Test Case 2 Passed")

assert pn(32) == "32 is not a Prime Number, and is a Composite Number\nNumber of factors of: 32 is \t6"
print("Test Case 3 Passed")

assert pn(0) == "0 is neither a Prime or Composite nor Co-Prime Number\nNumber of factors of: 0 is \tinfinite"
print("Test Case 4 Passed")

assert pn(45) == "45 is not a Prime Number, and is a Composite Number\nNumber of factors of: 32 is \t6"
print("Test Case 5 Passed")



time.sleep(2)
print("All Test Cases Passed")
