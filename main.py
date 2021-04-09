
from gaus import Gaus


g = Gaus()
g.elimination()
g.backSub()
print()
print("should be:")
g.checkResult()
