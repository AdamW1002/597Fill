#Copyright Adam Weiss 10/20/21
import mutatation
from representation.representation import Const, Plus

prog = Plus(Const(5), Const(3))
prog2 = mutatation.mutate(prog,0)

print("")