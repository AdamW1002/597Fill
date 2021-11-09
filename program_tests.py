#Copyright Adam Weiss 10/20/21
from interpreter import interpret
from representation.representation import Var, Mul, Minus, Const, Greater, If

x = Var("x")
print(interpret(x, {"x" : "y"}))

y = Minus(Const(5), Var("x"))
print(interpret(y, {"x" : 3}))

u = Mul(Const(3), Const(4))
w = Greater(Const(2), Const(1))

z = If(Greater(Const(1) , Const(0) ), Var("x"), Const("foo"))
print(interpret(z, {"x" : 3}))
match x:
    case (Var(operand_1="a")):
        print("fdsfas")
    case _:
        print("feeee")
