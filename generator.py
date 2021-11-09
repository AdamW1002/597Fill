# copyright Adam Weiss

# Take a set of programs and enumerate all combinations
import copy
import random

import interpreter
from IOtests import test_on_example
from representation.representation import Program, StrConst, IntConst, Plus, Mul, Minus, Const, Var


def is_leaf(program: Program) -> bool:
    return isinstance(program, IntConst) or isinstance(program, StrConst)


def stitch(host: Program | IntConst, graft: Program,
           check_example: list) -> set | Program:  # return a random graft replacing a leaf
    match host:  # E expressions
        # case IntConst | StrConst:
        #   return graft
        case Const():
            return {copy.deepcopy(graft)}
        case Var():
            return {copy.deepcopy(graft)}
        case Plus(operand_1=x, operand_2=y) | Mul(operand_1=x, operand_2=y) | Minus(operand_1=x, operand_2=y):

            match (x, y):
                case (None, None):
                    raise Exception("Error in program generation", "Error in program generation")

                case (z, None):
                    host.operand_1 = stitch(z, copy.deepcopy(graft))
                    return {host}

                case (None, z):
                    host.operand_2 = stitch(z, copy.deepcopy(graft))
                    return {host}

                case (z, w):
                    host_clone_l = copy.deepcopy(host)
                    host_clone_r = copy.deepcopy(host)

                    # graft_copy_l = copy.deepcopy(graft)
                    # graft_copy_r = copy.deepcopy(graft)

                    # new_children_l = stitch(host_clone_l.operand_1, graft_copy_l)
                    # new_children_r = stitch(host_clone_r.operand_2, graft_copy_r)
                    new_children_l = stitch(host_clone_l.operand_1, graft, check_example)
                    new_children_r = stitch(host_clone_r.operand_2, graft, check_example)

                    acc = set()
                    for child in new_children_l:
                        host_copy = copy.deepcopy(host)
                        host_copy.operand_1 = child

                        try:
                            test_on_example(host_copy, check_example)
                        except Exception:
                            pass
                        else:
                            acc.add(host_copy)

                    for child in new_children_r:
                        host_copy = copy.deepcopy(host)
                        host_copy.operand_2 = child
                        try:
                            test_on_example(host_copy, check_example)
                        except Exception:
                            pass
                        else:
                            acc.add(host_copy)

                    return acc

        case _:
            return None


def enumerate(programs: set, check_example : list) -> set:
    new_programs = set()
    count = 0
    for program_piece_host in programs:
        # clone_host_l = copy.deepcopy(program_piece_host)  # avoid state issues by cloning
        # clone_host_r = copy.deepcopy(program_piece_host)

        clone_host = copy.deepcopy(program_piece_host)  # avoid state issues by cloning
        for program_piece_graft in programs:
            if isinstance(clone_host, Mul) and (program_piece_graft == Const(1) or program_piece_graft == Const(0)):
                continue
            elif isinstance(clone_host, Plus) and program_piece_graft == Const(0):
                continue
            elif isinstance(clone_host, Var) or isinstance(clone_host, Const):
                continue
            elif program_piece_host == program_piece_graft:
                continue

            all_vars = ["i{}".format(j) for j in range(len(check_example[0]))] #make a list of all vars

            all_vars_in_host = True
            all_vars_in_graft = True
            for var in all_vars:
                all_vars_in_host = all_vars_in_host and (var in str(program_piece_host))
                all_vars_in_graft = all_vars_in_graft and (var in str(program_piece_graft))

            #if len(str(program_piece_graft) + str(program_piece_host)) > 150 and not (all_vars_in_graft and all_vars_in_host):#if too long without all vars, skip
            #    continue
            #print("count is {}".format(count))
            # clone_graft_l = copy.deepcopy(program_piece_graft)  # same as above
            # clone_graft_r = copy.deepcopy(program_piece_graft)  # same as above
            # result_l = stitch(clone_host_l, clone_graft_l, "l")
            # result_r = stitch(clone_host_r, clone_graft_r, "r")
            # new_programs.add(result_l)
            # new_programs.add(result_r)

            clone_graft = copy.deepcopy(program_piece_graft)

            result = stitch(clone_host, clone_graft, check_example)
            if 'i0' in str(result) and 'i1' in str(result) and 'i2' in str(result):
                print("good")
            new_programs = new_programs.union(result)
            count += 1
    return programs.union(new_programs)
