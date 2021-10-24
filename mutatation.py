# Copyright Adam Weiss 10/24/21
from math import exp
import random

from representation.representation import Program, Const

a = .9  # hyperparamter that affects mutation depth


def mutate(program: Program | int | str, depth: int) -> Program:
    mutation_chance = max(a * (1 - exp(1 - depth)),
                          0) + 0.1  # experimental curve, the .01 is so mutation can occur at level 1

    will_mutate = random.random() < mutation_chance

    if not (type(program) is str or type(program) is int):
        mutation_chance = mutation_chance or (
                program.operand_1 is None and program.operand_2 is None and program.operand_3 is None)
    # handle primitives
    if type(program) is int:
        if will_mutate:
            return program + random.randint(-3, 3)  # change the int some
        else:
            return program

    elif type(program) is str:
        return program  # TODO mutate here

    match (program.operand_1, program.operand_2, program.operand_3):
        case (None, None, None):
            return Const(0)  # when we mutate a leaf in the AST make it point to a 0 constant as a "base case"
        case (x, None, None):

            if will_mutate:
                new_operand = mutate(x, depth + 1)
                program.operand_1 = new_operand
                return x
            else:
                return mutate(x, depth + 1)
        case (x, y, None):
            if random.random() < .5:  # 50/50 on which one we do
                if will_mutate:
                    new_operand = mutate(x, depth + 1)
                    program.operand_1 = new_operand
                    return x
                else:
                    return mutate(x, depth + 1)
            else:
                if will_mutate:
                    new_operand = mutate(y, depth + 1)
                    program.operand_1 = new_operand
                    return y
                else:
                    return mutate(y, depth + 1)