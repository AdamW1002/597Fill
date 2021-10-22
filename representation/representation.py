# Copyright Adam Weiss 10/20/21

# start off with a program definition
class Program:
    def __init__(self):
        self.operand_1 = None
        self.operand_2 = None
        self.operand_3 = None




# Const types
IntConst = int
StrConst = str


# Expr types
class Expr(Program):
    def __init__(self):
        super().__init__()


class Bool(Program):
    def __init__(self):
        super().__init__()


class Var(Expr):
    def __init__(self, label: str) -> None:
        super().__init__()
        self.operand_1 = label


class Const(Expr):
    def __init__(self, value: IntConst | StrConst) -> None:
        super().__init__()
        self.operand_1 = value


class Plus(Expr):
    def __init__(self, op1: Expr, op2: Expr) -> None:
        super().__init__()
        self.operand_1 = op1
        self.operand_2 = op2


class Minus(Expr):
    def __init__(self, op1: Expr, op2: Expr) -> None:
        super().__init__()
        self.operand_1 = op1
        self.operand_2 = op2


class Times(Expr):
    def __init__(self, op1: Expr, op2: Expr) -> None:
        super().__init__()
        self.operand_1 = op1
        self.operand_2 = op2


class If(Expr):

    def __init__(self, cond: Bool, when_true: Expr, when_false: Expr) -> None:
        super().__init__()
        self.operand_1 = cond
        self.operand_2 = when_true
        self.operand_3 = when_false


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
    def __init__(self, op1: Expr, op2: Expr) -> None:
        super().__init__()
        self.operand_1 = op1
        self.operand_2 = op2


class Not(Bool):
    def __int__(self, e: Expr) -> None:
        super().__init__()
        self.operand_1 = e
