"""
_summary_
"""
from .instruction import *
from .Assembler.assembler import AssemblerReg
from .parser import parse

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
