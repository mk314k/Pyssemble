"""
_summary_

Raises:
    Exception: _description_
    Exception: _description_

Returns:
    _type_: _description_
"""
# pylint: disable=C3001  # Ignore lambda assignment
from typing import Type
from .memory import MemContent
from .assembler import Assembler
from .exception import PyAssembleException




class AssemblyInstruction(MemContent):
    """
    _summary_

    Returns:
        _type_: _description_
    """
    def __init__(self, reg1 = None, reg2 = None, reg3 = None):
        self.reg1 = reg1
        self.reg2 = reg2
        self.reg3 = reg3
        self.func = lambda *args: None
    def binary_rep(self):
        return ""
    def num_value(self):
        return 0
    def hex_rep(self):
        return ""
    def __repr__(self):
        return ''
    def execute(self):
        """
        _summary_
        """


class RegInstruction(AssemblyInstruction):
    """
    _summary_

    Args:
        AssemblyInstruction (_type_): _description_
    """
    def __init__(self, *args):
        if len(args)!=3:
            raise PyAssembleException
        self.rd, self.rs1, self.rs2 = args
    def execute(self):
        Assembler.registers[self.rd] = self.func(
            Assembler.registers[self.rs1], Assembler.registers[self.rs2]
        )

class RegImmInstruction(RegInstruction):
    """
    _summary_

    Args:
        RegInstruction (_type_): _description_
    """
    def execute(self):
        Assembler.registers[self.rd] = self.func(
            Assembler.registers[self.rs1], Assembler.registers[self.rs2]
        )
class BranchInstruction(RegInstruction):
    """
    _summary_

    Args:
        RegInstruction (_type_): _description_
    """
    def execute(self):
        Assembler.registers[self.rd] = self.func(
            Assembler.registers[self.rs1], Assembler.registers[self.rs2]
        )

class MemInstruction(RegInstruction):
    """
    _summary_

    Args:
        RegInstruction (_type_): _description_
    """
    def execute(self):
        Assembler.registers[self.rd] = self.func(
            Assembler.registers[self.rs1], Assembler.registers[self.rs2]
        )

class Add(RegInstruction):
    """
    _summary_

    Args:
        RegInstruction (_type_): _description_
    """
    func = lambda arg1, arg2: arg1 + arg2

class Sub(RegInstruction):
    """
    _summary_

    Args:
        RegInstruction (_type_): _description_
    """
    func = lambda arg1, arg2: arg1 - arg2

class Or(RegInstruction):
    """
    _summary_

    Args:
        RegInstruction (_type_): _description_
    """
    func = lambda arg1, arg2: arg1 | arg2

class And(RegInstruction):
    """
    _summary_

    Args:
        RegInstruction (_type_): _description_
    """
    func = lambda arg1, arg2: arg1 & arg2

class Xor(RegInstruction):
    """
    _summary_

    Args:
        RegInstruction (_type_): _description_
    """
    func = lambda arg1, arg2: arg1 ^ arg2

class Srl(RegInstruction):
    """
    _summary_

    Args:
        RegInstruction (_type_): _description_
    """
    func = lambda arg1, arg2: arg1 ^ arg2

class Sra(RegInstruction):
    """
    _summary_

    Args:
        RegInstruction (_type_): _description_
    """
    func = lambda arg1, arg2: arg1 ^ arg2

class Sll(RegInstruction):
    """
    _summary_

    Args:
        RegInstruction (_type_): _description_
    """
    func = lambda arg1, arg2: arg1 ^ arg2

class Addi(RegImmInstruction, Add):
    """
    _summary_

    Args:
        RegImmInstruction (_type_): _description_
        add (_type_): _description_
    """


class Ori(RegImmInstruction, Or):
    """
    _summary_

    Args:
        RegImmInstruction (_type_): _description_
        or_ (_type_): _description_
    """


class Andi(RegImmInstruction, And):
    """
    _summary_

    Args:
        RegImmInstruction (_type_): _description_
        and_ (_type_): _description_
    """


class Xori(RegImmInstruction, Xor):
    """
    _summary_

    Args:
        RegImmInstruction (_type_): _description_
        xor (_type_): _description_
    """

class Slli(RegImmInstruction, Sll):
    """
    Args:
        RegImmInstruction (_type_): _description_
        Sll (_type_): _description_

    Raises:
        PyAssembleException: _description_
    """
class Srai(RegImmInstruction, Sra):
    """
    _summary_

    Args:
        RegImmInstruction (_type_): _description_
        Sra (_type_): _description_

    Raises:
        PyAssembleException: _description_
    """

class Srli(RegImmInstruction, Srl):
    """
    _summary_

    Args:
        RegImmInstruction (_type_): _description_
        Srl (_type_): _description_

    Raises:
        PyAssembleException: _description_
    """
class Slti(RegImmInstruction):
    """
    _summary_

    Args:
        RegImmInstruction (_type_): _description_

    Raises:
        PyAssembleException: _description_
    """
class Sltiu(RegImmInstruction):
    """
    _summary_

    Args:
        RegImmInstruction (_type_): _description_

    Raises:
        PyAssembleException: _description_
    """

class Li(RegImmInstruction):
    """
    _summary_

    Args:
        AssemblyInstruction (_type_): _description_
    """
    def __init__(self, *args):
        if len(args)!=2:
            raise PyAssembleException
        self.rd, self.val = args
    def execute(self):
        Assembler.registers[self.rd] = self.val

class Lui(RegImmInstruction):
    """
    _summary_

    Args:
        RegImmInstruction (_type_): _description_
    """

class Beq(BranchInstruction):
    """

    Args:
        BranchInstruction (_type_): _description_
    """

class Bne(BranchInstruction):
    """
    _summary_

    Args:
        BranchInstruction (_type_): _description_
    """
class Blt(BranchInstruction):
    """
    _summary_

    Args:
        BranchInstruction (_type_): _description_
    """
class Bge(BranchInstruction):
    """
    _summary_

    Args:
        BranchInstruction (_type_): _description_
    """
class Bltu(BranchInstruction):
    """
    _summary_

    Args:
        BranchInstruction (_type_): _description_
    """
class Bgeu(BranchInstruction):
    """
    _summary_

    Args:
        BranchInstruction (_type_): _description_
    """

class Lw(MemInstruction):
    """
    _summary_

    Args:
        MemInstruction (_type_): _description_
    """

class Sw(MemInstruction):
    """
    _summary_

    Args:
        MemInstruction (_type_): _description_
    """
class Ret(AssemblyInstruction):
    """
    _summary_

    Args:
        AssemblyInstruction (_type_): _description_
    """


instructions = {
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
}  # type: Dict[str, Type[AssemblyInstruction]]
