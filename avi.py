import os
with open("test.py","x"):
    pass
try:
    os.remove("test.py")
    print("yes")
finally:
    pass