import json
import time

from main import solve_examples
from representation.representation import Const, Plus, Mul, Var, Minus

assignment_tests = json.load(open("tests.json")) #load data_file


def getTask(n: int) -> list:
    task_data = assignment_tests[" Task -{}".format(n)]
    task_examples = []
    for example in task_data:
        task_examples.append((example[' Input '], example[' Output ']))

    return task_examples


start_time = time.time_ns()
test_1 = getTask(1)
print("evaluating task 1 : {}".format(test_1))
print(solve_examples(test_1, {Plus(Const(0), Const(0)), Mul(Const(1), Const(1)), Var("i0"), Var("i1")}))
print("time taken to find solution is {} seconds".format((time.time_ns() - start_time) / 10 ** 9))

start_time = time.time_ns()
test_3 = getTask(3)
print("evaluating task 3 : {}".format(test_3))
#print(solve_examples(test_3, {Plus(Const(0), Const(0)), Mul(Const(1), Const(1)), Minus(Const(0), Const(0)), Var("i0"),
#                              Var("i1"), Var("i2")}))
print("time taken to find solution is {} seconds".format((time.time_ns() - start_time) / 10 ** 9))


start_time = time.time_ns()
test_2 = getTask(2)
print("evaluating task 2 : {}".format(test_2))
print(solve_examples(test_2,
                     {Plus(Const(0), Const(0)), Mul(Const(1), Const(1)), Var("i0"), Var("i1"), Var("i2"), Const(3)}))
print("time taken to find solution is {} seconds".format((time.time_ns() - start_time) / 10 ** 9))
