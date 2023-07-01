from register import RegIndex, RegisterSet
from memory import Memory

x0 = zero = RegIndex(0)
x1 = ra = RegIndex(1)
x2 = sp = RegIndex(2)
x3 = gp = RegIndex(3)
x4 = tp = RegIndex(4)
x5 = t0 = RegIndex(5)
x6 = t1 = RegIndex(6)
x7 = t2 = RegIndex(7)
x8 = s0 = RegIndex(8)
x9 = s1 = RegIndex(9)
x10 = a0 = RegIndex(10)
x11 = a1 = RegIndex(11)
x12 = a2 = RegIndex(12)
x13 = a3 = RegIndex(13)
x14 = a4 = RegIndex(14)
x15 = a5 = RegIndex(15)
x16 = a6 = RegIndex(16)
x17 = a7 = RegIndex(17)
x18 = s2 = RegIndex(18)
x19 = s3 = RegIndex(19)
x20 = s4 = RegIndex(20)
x21 = s5 = RegIndex(21)
x22 = s6 = RegIndex(22)
x23 = s7 = RegIndex(23)
x24 = s8 = RegIndex(24)
x25 = s9 = RegIndex(25)
x26 = s10 = RegIndex(26)
x27 = s11 = RegIndex(27)
x28 = t3 = RegIndex(28)
x29 = t4 = RegIndex(29)
x30 = t5 = RegIndex(30)
x31 = t6 = RegIndex(31)

class pyInstruction:
    regs = RegisterSet()
    pc = 0
    instruction_memory = Memory()
    data_memory = Memory()
    def __repr__(self):
        return ''
    def addInstruction(self, instruction):
        

class add(pyInstruction):
    def __init__(self, rd, rs1, rs2):
        self.regs[rd] = self.regs[rs1] + self.regs[rs2]

class sub(pyInstruction):
    def __init__(self, rd, rs1, rs2):
        self.regs[rd] = self.regs[rs1] - self.regs[rs2]

class or_(pyInstruction):
    def __init__(self, rd, rs1, rs2):
        self.regs[rd] = self.regs[rs1] | self.regs[rs2]

class and_(pyInstruction):
    def __init__(self, rd, rs1, rs2):
        self.regs[rd] = self.regs[rs1] & self.regs[rs2]

class xor(pyInstruction):
    def __init__(self, rd, rs1, rs2):
        self.regs[rd] = self.regs[rs1] ^ self.regs[rs2]

class li(pyInstruction):
    def __init__(self, rd, constant):
        self.regs[rd] = constant

class addi(pyInstruction):
    def __init__(self, rd, rs1, constant):
        self.regs[rd] = self.regs[rs1] + constant

class ori(pyInstruction):
    def __init__(self, rd, rs1, constant):
        self.regs[rd] = self.regs[rs1] | constant

class andi(pyInstruction):
    def __init__(self, rd, rs1, constant):
        self.regs[rd] = self.regs[rs1] & constant

class xori(pyInstruction):
    def __init__(self, rd, rs1, constant):
        self.regs[rd] = self.regs[rs1] ^ constant

