import sys
from package1 import module1
print()
sys.stderr.flush()
from package1.module2 import function1
function1()
print()
sys.stderr.flush()
from package2 import class1
class1()
print()
sys.stderr.flush()
from package2.subpackage1.module5 import function2
function2()
print()
sys.stderr.flush()
from package2 import module3
print()
sys.stderr.flush()
