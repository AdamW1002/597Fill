# Copyright Adam Weiss 10/20/21

#IMPORT NOTE ON SEMANTICS, STRINGS ARE COMPARABLE
from representation.representation import Program, Var, Const, Minus, Plus, Mul, Less, Equal, If, Not, Greater, Less


def interpret(program: Program, lookup: dict) -> str | int:
    match program: #E exprs
        case Var():
            return lookup[program.operand_1] #look up the value of var, crash if not present
        case Const():
            return program.operand_1
        case Plus():
            return interpret(program.operand_1,lookup) + interpret(program.operand_2,lookup) #execute arithmethic
        case Minus():
            return interpret(program.operand_1,lookup) - interpret(program.operand_2,lookup)
        case Mul():
            return interpret(program.operand_1,lookup) * interpret(program.operand_2,lookup)
        case If():#standard if semantics
            if interpret(program.operand_1, lookup):
                return interpret(program.operand_2,lookup)
            else:
                return interpret(program.operand_3,lookup)
        case Less(): #B exprs
            return int(interpret(program.operand_1, lookup) < interpret(program.operand_2, lookup))
        case Equal():  # B exprs
            return int(interpret(program.operand_1, lookup) == interpret(program.operand_2, lookup))
        case Greater():  # B exprs
            return int(interpret(program.operand_1, lookup) > interpret(program.operand_2, lookup))
        case Not():
            return int(not interpret(program.operand_1, lookup))

        case _:
            return None


