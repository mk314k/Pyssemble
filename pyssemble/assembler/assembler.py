"""
Author: mk314k
This file contains an implementation of Assembler to process assembly code.
"""
from .register import RegisterSet, Counter, reg_valid, reg_map
from .memory import Memory
from ..exception import RegisterIndexError
from ..utility import num_to_bin

class Assembler:
    """
    Class representing the main assembler.

    Attributes:
        registers (RegisterSet): Set of registers.
        data_memory (Memory): Memory for data.
        inst_memory (Memory): Memory for instructions.
        pc (Counter): Program counter.

    Methods:
        execute(addr=540): Execute instructions starting from the specified address.
    """
    registers = RegisterSet()
    data_memory = Memory()
    inst_memory = Memory()
    pc = Counter()

    @staticmethod
    def initiate(start_addr = 540):
        """
        initiate instruction memory with start_address for instruction

        Args:
            start_addr (int, optional): Address for the first instruction. Defaults to 540.
        """
        Assembler.inst_memory(start_addr)

    @staticmethod
    def execute(addr = 540):
        """
        Execute instructions starting from the specified address.

        Args:
            addr (int, optional): Starting address. Defaults to 540.
        """
        Assembler.pc.jump(addr)
        while Assembler.pc() != 0:
            Assembler.inst_memory[Assembler.pc()].execute()
            Assembler.pc.step()

class AssemblerReg:
    """
    Class representing a register in the assembler.

    Args:
        name (str|int): Name or index of the register.

    Raises:
        RegisterIndexError: If an invalid register index is provided.

    Attributes:
        __name (str): Name of the register.
        __index (int): Index of the register.

    Methods:
        __call__(val=None): Get or set the value of the register.
    """
    def __init__(self, name:str|int):
        """
        Initialize the register.

        Args:
            name (str|int): Name or index of the register.

        Raises:
            RegisterIndexError: If an invalid register index is provided.
        """
        if isinstance(name, int) and (0<=name <=31):
            self.__name = f'x{name}'
            self.__index = name
        elif isinstance(name, str) and reg_valid(name):
            if name in reg_map:
                name = reg_map.get(name)
            self.__name = name
            self.__index = int(name[1:])
        else:
            raise RegisterIndexError()

    def __repr__(self):
        """
        Return the string representation of the register.

        Returns:
            str: String representation of the register.
        """
        return self.__name

    def __str__(self):
        """
        Return the value of the register.
        """
        return str(self.value)

    def __call__(self, val:int|None = None)->int:
        """
        Get or set the value of the register.

        Args:
            val (int, optional): Value to set. If None, returns the current value.

        Returns:
            int: Current value of the register or the updated value if set.
        """
        if val is not None:
            Assembler.registers[self.__name] = val
        return Assembler.registers[self.__name]

    @property
    def bin(self)->str:
        """
        Get the binary representation of the register's index.

        Returns:
            str: Binary representation of the register's index.
        """
        return num_to_bin(self.__index, 5)

    @property
    def value(self)->int:
        """
        Get the current value of the register.

        Returns:
            int: Current value of the register.
        """
        return Assembler.registers[self.__index]

    @value.setter
    def value(self, val:int):
        """
        Set the value of the register.

        Args:
            val (int): Value to set.
        """
        Assembler.registers[self.__index] = val
