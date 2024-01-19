"""
Author: mk314k
This file contains all the rv32base instructions for Assembly.
Motivated from MIT 6.004 Computation Structures class isa reference handout.
"""
# pylint: disable=C3001  # Ignore lambda assignment
from typing import Type, Dict
from .Assembler.memory import MemContent, Data
from .Assembler.assembler import Assembler, AssemblerReg


class AssemblyInstruction(MemContent):
    """
    Base class for assembly instructions.

    Attributes:
        reg1: The first register.
        reg2: The second register.
        reg_num: The register or immediate number.
        func: main function the instruction implements.
    """
    func = lambda *args: None
    funct7 = ""
    funct3 = ""
    def __init__(self, reg1 = None, reg2 = None, reg_num = None):
        self.reg1 = reg1
        self.reg2 = reg2
        self.reg_num = reg_num
        Assembler.inst_memory.push(self)

    @property
    def value(self)->int:
        return int(self.bin, 2)

    def __repr__(self)->str:
        return self.hex

    def execute(self):
        """
        Execute the instruction.

        Raises:
            NotImplementedError: If the function is not implemented.
            It is implemented differently for instructions
        """
        raise NotImplementedError


class RegInstruction(AssemblyInstruction):
    """
    Class for register instructions.
    """
    opcode = "0110011"
    funct7 = "0000000"
    def __init__(self, rd:AssemblerReg, rs1:AssemblerReg, rs2:AssemblerReg):
        """
        Initialize a RegInstruction object.

        Args:
            rd: Destination register.
            rs1: Source register 1.
            rs2: Source register 2.
        """
        super().__init__(rd, rs1, rs2)

    @property
    def bin(self)->str:
        reg = f"{self.reg_num.bin}{self.reg2.bin}{self.funct3}{self.reg1.bin}"
        return f"{self.funct7}{reg}{self.opcode}"

    def execute(self):
        self.reg1.value = self.func(self.reg2.value, self.reg_num.value)


class RegImmInstruction(AssemblyInstruction):
    """
    Class for register immediate instructions.
    """
    opcode = "0010011"
    funct7 = "0000000"
    def __init__(self, rd:AssemblerReg, rs1:AssemblerReg, rval:int):
        """
        Initialize a RegImmInstruction object.

        Args:
            rd: Destination register.
            rs1: Source register 1.
            rval: Immediate value.
        """
        super().__init__(rd, rs1, rval)

    @property
    def bin(self)->str:
        pass

    def execute(self):
        self.reg1.value = self.func(self.reg2.value, self.reg_num)

class BranchInstruction(RegImmInstruction):
    """
    Class for branch instructions.
    It has same initialization structure as ImmInstruction
    label can be considered immediate value
    """
    @property
    def bin(self)->str:
        pass
    def execute(self):
        if self.func(self.reg1.value, self.reg2.value):
            Assembler.pc.jump(self.reg_num)

class MemInstruction(AssemblyInstruction):
    """
    Class for memory instructions.
    """
    def __init__(self, rd:AssemblerReg, offset:int, rs1:AssemblerReg):
        """
        Initialize a MemInstruction object.

        Args:
            rd: Destination register.
            offset: Memory offset.
            rs1: Source register.
        """
        super().__init__(rd, rs1, offset)
    @property
    def bin(self)->str:
        pass
    def execute(self):
        raise NotImplementedError

#-----------------------------------------------------------------------
# Register Instructions
#-----------------------------------------------------------------------
class Add(RegInstruction):
    """
    Addition instruction.
    """
    funct3 = "000"
    func = lambda arg1, arg2: arg1 + arg2

class Sub(RegInstruction):
    """
    Subtraction instruction.
    """
    funct3 = "000"
    funct7 = "0100000"
    func = lambda arg1, arg2: arg1 - arg2

class Or(RegInstruction):
    """
    Bitwise OR instruction.
    """
    funct3 = "110"
    func = lambda arg1, arg2: arg1 | arg2

class And(RegInstruction):
    """
    Bitwise AND instruction.
    """
    funct3 = "111"
    func = lambda arg1, arg2: arg1 & arg2

class Xor(RegInstruction):
    """
    Bitwise XOR instruction.
    """
    funct3 = "100"
    func = lambda arg1, arg2: arg1 ^ arg2

class Srl(RegInstruction):
    """
    Shift Right Logical instruction.
    """
    funct3 = "101"
    func = lambda arg1, arg2: arg1 >> (arg2 & 0b11111)

class Sra(RegInstruction):
    """
    Shift Right Arithmetic instruction.
    """
    funct3 = "101"
    funct7 = "0100000"
    func = lambda arg1, arg2: arg1 ^ arg2

class Sll(RegInstruction):
    """
    Shift Left Logical instruction.
    """
    funct3 = "001"
    func = lambda arg1, arg2: arg1 << (arg2 & 0b11111)

#-----------------------------------------------------------------------
# Register Immediate Instructions
#-----------------------------------------------------------------------

class Addi(RegImmInstruction, Add):
    """
    Addition with immediate instruction.
    """


class Ori(RegImmInstruction, Or):
    """
    Bitwise OR with immediate instruction.
    """


class Andi(RegImmInstruction, And):
    """
    Bitwise AND with immediate instruction.
    """


class Xori(RegImmInstruction, Xor):
    """
    Bitwise XOR with immediate instruction.
    """

class Slli(RegImmInstruction, Sll):
    """
    Shift Left Logical Immediate instruction.

    Raises:
        PyAssembleException: _description_
    """
class Srai(RegImmInstruction, Sra):
    """
    Shift Right Arithmetic Immediate instruction.

    Raises:
        PyAssembleException: _description_
    """

class Srli(RegImmInstruction, Srl):
    """
    Shift Right Logical Immediate instruction.

    Raises:
        PyAssembleException: _description_
    """
class Slti(RegImmInstruction):
    """
    Set Less Than Immediate instruction.

    Raises:
        PyAssembleException: _description_
    """
    #TODO
class Sltiu(RegImmInstruction):
    """
    Set Less Than Immediate Unsigned instruction.

    Raises:
        PyAssembleException: _description_
    """
    #TODO

class Li(RegImmInstruction):
    """
    Load Immediate instruction.
    """
    def __init__(self, rd:AssemblerReg, val:int):
        super().__init__(rd, None, val)
    def execute(self):
        self.reg1.value = self.reg_num

class Lui(RegImmInstruction):
    """
    Load Upper Immediate instruction.
    """

#-----------------------------------------------------------------------
# Branch Instructions
#-----------------------------------------------------------------------

class Beq(BranchInstruction):
    """
    Branch if Equal instruction.
    """

class Bne(BranchInstruction):
    """
    Branch if Not Equal instruction.
    """
    func = lambda arg1, arg2: arg1 != arg2

class Blt(BranchInstruction):
    """
    Branch if Less Than instruction.
    """
    func = lambda arg1, arg2: arg1 < arg2

class Bge(BranchInstruction):
    """
    Branch if Greater Than or Equal instruction.
    """
    func = lambda arg1, arg2: arg1 >= arg2

class Bltu(BranchInstruction):
    """
    Branch if Less Than Unsigned instruction.
    """

class Bgeu(BranchInstruction):
    """
    Branch if Greater Than or Equal Unsigned instruction.
    """

#-----------------------------------------------------------------------
# Memory Instructions
#-----------------------------------------------------------------------

class Lw(MemInstruction):
    """
    Load Word instruction.
    """
    def execute(self):
        self.reg1.value = Assembler.data_memory[self.reg2.value + self.reg_num].value

class Sw(MemInstruction):
    """
    Store Word instruction.
    """
    def execute(self):
        Assembler.data_memory[self.reg2.value + self.reg_num] = Data(self.reg1.value)

#-----------------------------------------------------------------------
# Jump Instructions
#-----------------------------------------------------------------------

class Ret(AssemblyInstruction):
    """
    Return instruction.
    """
    def execute(self):
        Assembler.pc.jump(Assembler.registers['ra'] - 4)
    @property
    def bin(self)->str:
        pass

instructions:Dict[str, Type[AssemblyInstruction]] = {
    # Reg operations
    'add': Add,
    'sub': Sub,
    'and': And,
    'or': Or,
    'xor': Xor,
    'sll': Sll,
    'srl': Srl,
    'sra': Sra,

    # Reg Immediate Operations
    'addi': Addi,
    'andi': Andi,
    'ori': Ori,
    'xori': Xori,
    'slti': Slti,
    'sltiu': Sltiu,
    'slli': Slli,
    'srli': Srli,
    'srai': Srai,

    # Branch
    'beq': Beq,
    'bne': Bne,
    'blt': Blt,
    'bge': Bge,
    'bltu': Bltu,
    'bgeu': Bgeu,

    # Mem Operations
    'lw': Lw,
    'sw': Sw,

    # Reg Loading Operations
    'li': Li,
    'lui': Lui,

    # Jump operations
    'ret': Ret
}
