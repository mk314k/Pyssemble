"""
This document is still under development, it is supposed to help
with finding syntax errors while writing Assembly code itself.
"""
# pylint: disable=C3001  # Ignore lambda assignment
from .Assembler.register import reg_valid

class AssemblyGrammar:
    """
    _summary_
    """
    is_reg = lambda index: lambda args : reg_valid(args[index])
    is_reg_all = lambda args: all([reg_valid(arg) for arg in args])
    arg_length = lambda length: lambda args: len(args) == length

class InstructionSet:
    """
    _summary_
    """
    def __init__(self, ):
        self.instructions = {}
        self.grammar = {}
    def add_instruction(self, identifier, grammar, function):
        """
        _summary_

        Args:
            identifier (_type_): _description_
            grammar (_type_): _description_
            function (_type_): _description_
        """
        self.instructions[identifier] = function
        self.grammar[identifier] = grammar
    def process_grammar(self, arguments):
        """
        _summary_

        Args:
            id (_type_): _description_
            arguments (_type_): _description_

        Returns:
            _type_: _description_
        """
        return all(
            [
                rule(arguments) for rule in self.grammar[id]
            ]
        )
    def apply_function(self):
        """
        _summary_
        """

    def execute(self, arguments):
        """
        _summary_

        Args:
            id (_type_): _description_
            arguments (_type_): _description_
        """
