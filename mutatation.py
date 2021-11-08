# Copyright Adam Weiss 10/24/21
from math import exp
import random

from representation.representation import Program, Const, Plus, Minus, Times, Var, IntConst, symbolicInt

const_counter = 0
var_counter = 0

def fresh_var_name() -> str():
    global var_counter
    name = "x{}".format(var_counter)
    var_counter += 1
    return name


def fresh_const_name() -> str:
    global  const_counter
    name = "x{}".format(const_counter)
    const_counter += 1
    return name

a = 1.2  # hyperparamter that affects mutation depth

#start off with some valid programs
starting_ints = [Const(i) for i in range(0,1)]



def make_AST(depth : int, vars : int) -> Program:
    if depth == 0: #just a leaf
        const_vs_var = random.random()
        if const_vs_var < .5:
            return Var(fresh_const_name()) #for ... reasons I treat constants as vars then infer the value using z3
        else:
            return  Var("i{}".format(random.randrange(0,vars)))


#def mutate(program: Program | int | str, depth: int, vars: int) -> Program:
#    if type(program) is Var:
#        print("fdsfa")
#    mutation_chance = max(a * (1 - exp(1 - depth)),
#                          0) + 0.1  # experimental curve, the .01 is so mutation can occur at level 1
#
#    will_mutate = random.random() < mutation_chance
#
#    if not (type(program) is str or type(program) is int):
#        mutation_chance = mutation_chance or (
#                program.operand_1 is None and program.operand_2 is None and program.operand_3 is None)
#    # handle primitives
#    if type(program) is int:
#        if will_mutate:
#            value_or_structure = .5  # do we change value or structure
#            if random.random() < value_or_structure:
#                return program + random.randint(-3, 3)  # change the int some
#            else:
#              return Var("i{}".format(random.randrange(0,vars)))
#        else:
#            return program
#
#    elif type(program) is str:
#        return program  # TODO mutate here
#
#    match (program.operand_1, program.operand_2, program.operand_3):
#        case (None, None, None):
#
#            return Const(0)  # when we mutate a leaf in the AST make it point to a 0 constant as a "base case"
#
#        case (x, None, None):
#
#            if will_mutate:
#                new_var = random.random()
#                if new_var > .33:
#                    return Var("i{}".format(random.randrange(0,vars)))
#                else:
#                    if random.random() < .5:
#                        new_operand = mutate(x, depth + 1, vars)
#                        program.operand_1 = new_operand
#                        return x
#                    else:
#                        prog
#            else:
#                return mutate(x, depth + 1, vars)
#        case (x, y, None):
#            operator_or_child = .5  # do we change the operator e.g. + -> - or change a value e.g. 5+3 -> 4+3
#            if random.random() < operator_or_child:  # if doing an operator
#                choice = random.random()
#                new_operation = None
#                if choice < .25:
#                    new_operation = Plus(x, y)  # TODO add if
#                elif choice < .5:
#                    new_operation = Minus(x, y)
#                elif choice < 1:
#                    new_operation = Times(x, y)
#
#                return new_operation
#            else:
#
#                if random.random() < .5:  # 50/50 on which one we do
#                    if will_mutate:
#                        new_operand = mutate(x, depth + 1, vars)
#                        program.operand_1 = new_operand
#                        return x
#                    else:
#                        return mutate(x, depth + 1, vars)
#                else:
#                    if will_mutate:
#                        new_operand = mutate(y, depth + 1, vars)
#                        program.operand_2 = new_operand
#                        return y
#                    else:
#                        return mutate(y, depth + 1, vars)
#