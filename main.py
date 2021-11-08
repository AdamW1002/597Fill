# Copyright Adam Weiss 10/20/21
import math
import random

import generator
import interpreter

from IOtests import test_on_several
from generator import stitch
from representation import representation
from representation.representation import Const, Plus, Var, Times

prog = Plus(Const(5), representation.Const(3))
# prog2 = mutatation.mutate(prog,0,2)
prog3 = Plus(Var("i0"), Const(2))
#x = prog
#old_score = 10

#test_1 = [([2, 2], 4), ([2, 3], 6)]
test_2 = [([1,2,3], 5), ([2,2,2],8), ([3,4,5], 60)]
prog_4 = generator.stitch(Plus(Const(1), Const(2)), Const(3))

#x = {Times(Const(1), Const(1)), Var("i0"), Var("i1"),  Const(0), Plus(Const(1), Const(1))}


#

def solve_examples(IO_pairs: list) -> None:
    x = {Times(Const(1), Const(1)), Var("i0"), Var("i1"),  Const(0), Plus(Const(1), Const(1))}
    interpreter_check_pair = IO_pairs[0][0]  # first input from first test
    for i in range(10):
        print("x is " + str(len(x)))
        new_x = set()
        x_candidates = generator.enumerate(x)
        for y in x_candidates:
            try:
                #       print("x evaluates to {} ", interpreter.interpret(y, interpreter_check_pair))
                result = test_on_several(y, IO_pairs)
                if result[1]:
                    print(result)

            except Exception:
                pass
            else:
                new_x.add(y)
        x = new_x


solve_examples(test_2)
'''for y in x:
    print("___________________")
    try:
        print(interpreter.interpret(y, {"i0": 3, "i1": 4}))
    except Exception:
        print("oopsie")
    # print(y)
    print("___________________")'''
# print(mutatation.make_AST(0, 2))
# for i in range(50): #metropolis hastings
#    print(str(x))
#    y = mutatation.mutate(x,0,2)
#    u = random.random()
#
#    result = test_on_several(y,test_1)
#    score = 0
#    for success,_ in result:
#        score += success * 1
#    score /= len(result)
#
#    if(score == 1):
#        print("done")
#        break
#    elif  u < math.exp(old_score-score):
#        x = y
#    old_score = score
#
