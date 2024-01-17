"""
_summary_

Raises:
    Exception: _description_

Returns:
    _type_: _description_
"""
from .memory import Memory
from .register import *

class AssemblyGrammar:
    is_reg = lambda index: lambda args : reg_valid(args[index]) or args[index] in reg_map
    is_reg_all = lambda args: all([reg_valid(arg) or arg in reg_map for arg in args])
    arg_length = lambda length: lambda args: len(args) == length

class InstructionSet:
    def __init__(self, ):
        self.instructions = {}
        self.grammar = {}
    def add_instruction(self, identifier, grammar, function):
        self.instructions[identifier] = function
        self.grammar[identifier] = grammar
    def process_grammar(self, id, arguments):
        return all(
            [
                rule(arguments) for rule in self.grammar[id]
            ]
        )
    def apply_function(self):
        pass
    def execute(self, id, arguments):
        pass

class Assembler:
    def __init__(self)->None:
        self.registers = RegisterSet()
        self.memory = Memory()
        pass
    def expand_memory(self, new_memory_size):
        pass
    def reset_memory(self):
        pass
    def reset_register(self):
        pass
    def process_code(self, code):
        # lines = code.split('\n')
        # instructions = []; labels = {}
        # for index, line in enumerate(lines):
        #     if line.strip():
        #         if line[-1] == ':':
        #             labels[line[:-1]] = index
        #         elif line == 'ret':
        #             pass
        #         instruction = line.split()
        #         id = instruction[0]
        #         args = instruction[1:]
        #         if inst.process_grammar(id, args):
        #             pass
        #         else:
        #             raise Exception
        # return inst
        pass