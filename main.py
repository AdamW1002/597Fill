#Copyright Adam Weiss 10/20/21
import mutatation
from IOtests import test_on_several
from representation.representation import Const, Plus, Var

prog = Plus(Const(5), Const(3))
prog2 = mutatation.mutate(prog,0)
prog3 = Plus(Var("i0"), Const(2))

test_1 = [([2, 2], 4), ([2, 3], 5)]
x = test_on_several(prog3, test_1)

score = 0
for success,_ in x:
    score += success * 1
score /= len(x)

print(score)