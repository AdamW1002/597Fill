# Copyright Adam Weiss 10/20/21


# Bool classes
from backup.Expr import Expr
from backup.program import Program


class Bool(Program):
    def __init__(self) -> None:
        super().__init__()


class Less(Bool):
    def __int__(self, e1: Expr, e2: Expr) -> None:
        super().__init__()
        self.operand_1 = e1
        self.operand_2 = e2


class Equal(Bool):
    def __int__(self, e1: Expr, e2: Expr) -> None:
        super().__init__()
        self.operand_1 = e1
        self.operand_2 = e2


class Greater(Bool):
    def __int__(self, e1: Expr, e2: Expr) -> None:
        super().__init__()
        self.operand_1 = e1
        self.operand_2 = e2


class Not(Bool):
    def __int__(self, e: Expr) -> None:
        super().__init__()
        self.operand_1 = e



