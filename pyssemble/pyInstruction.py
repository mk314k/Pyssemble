from register import RegIndex, RegisterSet, Counter
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
    ic = Counter()
    pc = Counter()
    instruction_memory = Memory()
    data_memory = Memory()
    def __repr__(self):
        return ''
    def execute(self):
        while (self.pc.val <self.ic.val):
            self.instruction_memory[self.pc.val].execute()
        pass

class RegInstruction(pyInstruction):
    def __init__(self, *args):
        if len(args)!=3:
            raise Exception
        self.rd, self.rs1, self.rs2 = args
        self.instruction_memory[self.ic.val] = self
        self.ic.step()
    def execute(self):
        self.regs[self.rd] = self.func(self.regs[self.rs1], self.regs[self.rs2])
        self.pc.step()

class RegImmInstruction(RegInstruction):
    def execute(self):
        self.regs[self.rd] = self.func(self.regs[self.rs1], self.rs2)
        self.pc.step()

class add(RegInstruction):
    func = lambda _, arg1, arg2: arg1 + arg2

class sub(RegInstruction):
    func = lambda _, arg1, arg2: arg1 - arg2

class or_(RegInstruction):
    func = lambda _, arg1, arg2: arg1 | arg2

class and_(RegInstruction):
    func = lambda _, arg1, arg2: arg1 & arg2

class xor(RegInstruction):
    func = lambda _, arg1, arg2: arg1 ^ arg2

class addi(RegImmInstruction, add):
    pass

class ori(RegImmInstruction, or_):
    pass

class andi(RegImmInstruction, and_):
    pass

class xori(RegImmInstruction, xor):
    pass

class li(pyInstruction):
    def __init__(self, *args):
        if len(args)!=2:
            raise Exception
        self.rd, self.val = args
        self.instruction_memory[self.ic.val] = self
        self.ic.step()
    def execute(self):
        self.regs[self.rd] = self.val
        self.pc.step()

class eor(RegInstruction):
    func = lambda _, arg1, arg2: 0 if arg1 == arg2 else 1

class lsl(RegInstruction):
    func = lambda _, __, arg, amt: arg << amt

class rsl(RegInstruction):
    func = lambda _, __, arg, amt: arg >> amt

class asr(RegInstruction):
    def func(_, arg, amt):
        if arg >= 0:
            return arg >> amt
        else:
            
class mul(RegInstruction):
    func = lambda _, arg1, arg2: arg1 * arg2 #CHECK

# class smull(RegInstruction) #INCOMPLETE 
    
# class umull(RegInstruction) 

# class B.cond(RegInstruction) 
    

    



