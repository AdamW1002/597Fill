# Copyright Adam Weiss 10/20/21
# Test examples for the flashfill
#
# format [input0], output0 ......
from typing import Tuple, List

import interpreter
from representation.representation import Plus, Var, Program, Const

test_1 = [([2, 2], 4), ([2, 3], 5)]

prog = Plus(Var("i0"), Var("i1"))


def test_on_example(program: Program, example: Tuple) -> int | str:  # test program on IO tuple
    inputs, desired_output = example
    assignments = dict()

    for i in range(len(inputs)):
        parsed_value = None  # parse as either string or int
        try:
            parsed_value = int(inputs[i])
        except:
            parsed_value = str(inputs[i])
        #if '"' in str(inputs[i]):  # if is string
        #    parsed_value = str(inputs[i])
        #else:
        #    parsed_value = int(inputs[i])
        assignments["i{}".format(i)] = parsed_value

    result = interpreter.interpret(program,assignments)
    #print("Is program correct {}: {}".format(example,desired_output == result))

    return result == desired_output, result


def test_on_several(program : Program , tests : List) -> List:#run on whole test set
        results = []
        all_good = True
        for test in tests:
            result = test_on_example(program, test)
            results.append(result)

            all_good = all_good and result[0]

        return results, all_good
print(test_on_several(prog, test_1))
