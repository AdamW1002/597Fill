# Copyright Adam Weiss 10/20/21
from representation.Expr import Var

x = Var("a")

match x:
    case (Var(operand_1="a")):
        print("fdsfas")
    case _:
        print("feeee")
