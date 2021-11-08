# copyright Adam Weiss

# Take a set of programs and enumerate all combinations
import copy
import random

from representation.representation import Program, StrConst, IntConst, Plus, Times, Minus, Const, Var


def is_leaf(program: Program) -> bool:
    return isinstance(program, IntConst) or isinstance(program, StrConst)


def stitch(host: Program | IntConst, graft: Program) -> Program:  # return a random graft replacing a leaf
    match host:  # E expressions
        # case IntConst | StrConst:
        #   return graft
        case Const():
            return graft
        case Var():
            return graft
        case Plus(operand_1=x, operand_2=y) | Times(operand_1=x, operand_2=y) | Minus(operand_1=x, operand_2=y):

            match (x, y):
                case (None, None):
                    raise Exception("Error in program generation", "Error in program generation")

                case (z, None):
                    host.operand_1 = stitch(z, graft)
                    return host

                case (None, z):
                    host.operand_2 = stitch(z, graft)
                    return host

                case (z, w):
                    if random.random() < .5:
                        host.operand_1 = stitch(z, graft)
                    else:
                        host.operand_2 = stitch(w, graft)
                    return host

        case _:
            return None


def enumerate(programs: set) -> set:
    new_programs = set()
    for program_piece_host in programs:
        clone_host = copy.deepcopy(program_piece_host)  # avoid state issues by cloning
        for program_piece_graft in programs:
            if isinstance(programs, Times) and (clone_graft == Const(1) or clone_graft == Const(0)):
                continue
            clone_graft = copy.deepcopy(program_piece_graft)  # same as above
            new_programs.add(stitch(clone_host,clone_graft))
    return programs.union(new_programs)
