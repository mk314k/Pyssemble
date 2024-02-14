"""
_summary_
"""
from .instruction import *
from .assembler import AssemblerReg, Assembler, reg_map
from .parser import parse as code_from_string

x0 = zero = AssemblerReg(0)
x1 = ra = AssemblerReg(1)
x2 = sp = AssemblerReg(2)
x3 = gp = AssemblerReg(3)
x4 = tp = AssemblerReg(4)
x5 = t0 = AssemblerReg(5)
x6 = t1 = AssemblerReg(6)
x7 = t2 = AssemblerReg(7)
x8 = s0 = AssemblerReg(8)
x9 = s1 = AssemblerReg(9)
x10 = a0 = AssemblerReg(10)
x11 = a1 = AssemblerReg(11)
x12 = a2 = AssemblerReg(12)
x13 = a3 = AssemblerReg(13)
x14 = a4 = AssemblerReg(14)
x15 = a5 = AssemblerReg(15)
x16 = a6 = AssemblerReg(16)
x17 = a7 = AssemblerReg(17)
x18 = s2 = AssemblerReg(18)
x19 = s3 = AssemblerReg(19)
x20 = s4 = AssemblerReg(20)
x21 = s5 = AssemblerReg(21)
x22 = s6 = AssemblerReg(22)
x23 = s7 = AssemblerReg(23)
x24 = s8 = AssemblerReg(24)
x25 = s9 = AssemblerReg(25)
x26 = s10 = AssemblerReg(26)
x27 = s11 = AssemblerReg(27)
x28 = t3 = AssemblerReg(28)
x29 = t4 = AssemblerReg(29)
x30 = t5 = AssemblerReg(30)
x31 = t6 = AssemblerReg(31)


class Pyssemble:
    """
    _summary_
    """
    def __init__(self, start_addr=540):
        self.initiate(start_addr)

    @staticmethod
    def initiate(start_addr=540):
        """
        _summary_

        Args:
            start_addr (int, optional): _description_. Defaults to 540.
        """
        Assembler.initiate(start_addr)
        import inspect # pylint: disable=C0415  # Ignore import outside toplevel
        caller_global = inspect.currentframe().f_back.f_globals
        for reg, regx in reg_map.items():
            caller_global[reg] = caller_global[regx] = AssemblerReg(reg)
        for inst_name, inst in instructions.items():
            caller_global[inst_name.capitalize()] = inst
        del caller_global

    @staticmethod
    def execute(start_addr=540):
        """
        _summary_

        Args:
            start_addr (int, optional): _description_. Defaults to 540.
        """
        Assembler.execute(start_addr)
