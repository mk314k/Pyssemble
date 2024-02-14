"""
Author: mk314k
This module includes additional debugging instructions for printing
register and memory in the middle of program execution, executing
instructions step by step and logging history of registers.
"""
from .assembler import Assembler
from .instruction import AssemblyInstruction
class Debugger:
    """
    Main Debugger class exported outside this module
    """
    @staticmethod
    def initiate():
        """
        Initiate debugger, make the debugging instructions accessible
        """
        import inspect # pylint: disable=C0415  # Ignore import outside toplevel
        caller_global = inspect.currentframe().f_back.f_globals
        caller_global.update({
            'PrintR':PrintR,
            'PrintM':PrintM
        })
        del caller_global

    @staticmethod
    def step_execute(start_addr=540):
        """
        execute program step by step. Only one step is performed.

        Args:
            start_addr (int, optional): Address to start executing from. Defaults to 540.
        """


class DebugInstruction(AssemblyInstruction):
    """
    Additional set of instructions for debugging the given code without
    affecting them.
    """
    def __init__(self, reg_num):
        super().__init__(reg_num=reg_num)

    @property
    def bin(self)->str:
        return "1"*32

    def execute(self):
        raise NotImplementedError

class PrintR(DebugInstruction):
    """
    Print numerical value in the given register
    """
    def execute(self):
        print(self.reg_num.value)


class PrintM(DebugInstruction):
    """
    Print the content in the memory. The address is the value 
    in the given register.
    """
    def execute(self):
        print(Assembler.data_memory.get(self.reg_num.value))


class Print(DebugInstruction):
    """
    Print multiple registers at once
    """
    def __init__(self, *args):
        self.args = args
        super().__init__(0)

    def execute(self):
        pass
