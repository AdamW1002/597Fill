# Copyright Adam Weiss 10/20/21
import math
import random

import IOtests
import generator
import interpreter

from IOtests import test_on_several
from generator import stitch
from representation import representation
from representation.representation import Const, Plus, Var, Mul, Minus

prog = Plus(Const(5), representation.Const(3))
# prog2 = mutatation.mutate(prog,0,2)
prog3 = Plus(Var("i0"), Const(2))
# x = prog
# old_score = 10

test_1 = [([2, 2], 4), ([3, 5], 15)]
test_2 = [(['hi', 2, 3], 'hi' * 6), (['uwu', 2, 2], 'uwu' * 4), (["nyaaa", 4, 5], "nyaaa" * 20)]
test_3 = [(["hello", 4, 2], "hellohello"), (["world", 1, 0], "world"), (["hi", 3, 3], "")]
test_4 = [(["a", "b", "b"], "aaabb"), (["aa", "b", "d"], (3 * "aa") + "b" + "d")]
'''prog_4 = generator.stitch(Plus(Const(1), Const(2)), Const(3), [])
prog_5 = generator.stitch(Plus(Const(1), Const(2)), Const(3), [])

prog_6 = generator.stitch(Mul(Const(1), Const(2)), Var("x"), [])
'''
prog_base = Plus(Const(1), Const(2))
prog_result = generator.enumerate({prog_base, Var('i0'), Var('i1'), Var('i2')}, test_2)
prog_result = generator.enumerate(prog_result, test_2)
prog_result = generator.enumerate(prog_result, test_2)

z = generator.pre_process({Plus(Const(0), Const(1)), Var("i0"), Var("i1")})


#

def solve_examples(IO_pairs: list, bottoms: set) -> None:
    interpreter_check_pair = IO_pairs[0]  # first input from first test
    bottoms = generator.pre_process(bottoms)
    for i in range(10):
        print("there are {} bottoms before semantic pruning".format(len(bottoms)))
        if len(bottoms) > 200:  # semantic pruning
            new_bottoms = set()
            outputs_to_inputs = dict()
            for program in bottoms:  # map outputs to which programs generate them
                semantics = tuple(map(lambda x: IOtests.test_on_example(program, x)[1], IO_pairs))
                if semantics in outputs_to_inputs.keys():
                    outputs_to_inputs[semantics] = outputs_to_inputs[semantics] + [program]
                else:
                    outputs_to_inputs[semantics] = [program]

            for output in outputs_to_inputs:  # prune out semantically similar candidates
                candidates = outputs_to_inputs[output]
                candidates.sort(key=lambda x: len(str(x)))  # take smallest programs

                new_bottoms = new_bottoms.union(set( candidates[0: min(max(3, int(len(bottoms)/50)), len(candidates)) ]  ))
            bottoms = new_bottoms


            print("after semantic pruning there are {} bottoms".format(len(bottoms)))
        if len(bottoms) > 400:
            bottom_list = list(bottoms)
            bottom_list.sort(key=lambda prog: len(str(prog)))
            bottoms = set(bottom_list[0:int(len(bottoms) * .2)])  # take only the first part
            print("pruned search space to {}".format(len(bottoms)))
        bottom_candidates = generator.enumerate(bottoms, interpreter_check_pair)
        print("evaluating {} candidates, x length is {}".format(len(bottom_candidates), len(bottoms)))
        if i == 2:  # dbg
            pass

        successes = [] #extract succesful programs

        for y in bottom_candidates:

            result = test_on_several(y, IO_pairs)
            if result[1]:
                successes.append(y)

            # print(result)

            bottoms.add(y)
        if (len(successes) > 0):  # return simplest answer
            successes.sort(key=lambda prog: len(str(prog)))
            return successes[0]

        print("finished evaluating candidates")
    return  None

#print(solve_examples(test_1, {Plus(Const(0), Const(0)), Mul(Const(1), Const(1)), Var("i0"), Var("i1")}))
#print(solve_examples(test_2, {Plus(Const(0), Const(0)),Mul(Const(1), Const(1)), Var("i0"), Var("i1"), Var("i2")}))
#print(solve_examples(test_3, {Plus(Const(0), Const(0)), Mul(Const(1), Const(1)), Minus(Const(0), Const(0)), Var("i0"),
#                             Var("i1"), Var("i2")}))
#print(solve_examples(test_4, {Plus(Const(0), Const(0)), Mul(Const(1), Const(1)), Minus(Const(0), Const(0)), Var("i0"),
                              #Var("i1"), Var("i2")}.union(set([Const(i) for i in range(3)]))))
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
