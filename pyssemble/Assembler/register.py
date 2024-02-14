"""
Author: mk314k
This file contains an implementation of 32 registers for rv32base instructions.
"""
import re
from ..exception import RegisterIndexError

reg_map = {
        'zero': 'x0',
        'ra': 'x1',
        'sp': 'x2',
        'gp': 'x3',
        'tp': 'x4',
        't0': 'x5',
        't1': 'x6',
        't2': 'x7',
        's0': 'x8',
        's1': 'x9',
        'a0': 'x10',
        'a1': 'x11',
        'a2': 'x12',
        'a3': 'x13',
        'a4': 'x14',
        'a5': 'x15',
        'a6': 'x16',
        'a7': 'x17',
        's2': 'x18',
        's3': 'x19',
        's4': 'x20',
        's5': 'x21',
        's6': 'x22',
        's7': 'x23',
        's8': 'x24',
        's9': 'x25',
        's10': 'x26',
        's11': 'x27',
        't3': 'x28',
        't4': 'x29',
        't5': 'x30',
        't6': 'x31'
    }

def reg_valid(reg:str)->bool:
    """
    Check if the given string is a valid register.

    Args:
        reg (str): String representing a register.

    Returns:
        bool: True if the string is a valid register, False otherwise.
    """
    pattern = r'^x([0-9]|[1-2]\d|3[0-1])$'
    return bool(re.match(pattern, reg)) or (reg in reg_map)


class Counter:
    """
    Counter class to keep track of values.

    Attributes:
        val (int): Current value of the counter.

    Methods:
        __call__(): Get the current value of the counter.
        step(): Increment the counter by 4.
        jump(val: int): Set the counter to a specific value.

    Args:
        val (int): Initial value of the counter. Defaults to 0.
    """
    def __init__(self, val=0):
        self.val = val

    def __call__(self):
        """
        Get the current value of the counter.

        Returns:
            int: Current value of the counter.
        """
        return self.val

    def step(self):
        """
        Increment the counter by 4.
        """
        self.val += 4

    def jump(self, val:int):
        """
        Set the counter to a specific value.

        Args:
            val (int): New value for the counter.
        """
        self.val = val

class RegisterSet:
    """
    RegisterSet class to manage registers.

    Attributes:
        __registers (list): List representing the registers.

    Methods:
        reg_to_index(reg): Convert register name to index.
        __getitem__(index): Get the value of a register.
        __setitem__(index, value): Set the value of a register.

    Raises:
        RegisterIndexError: If the register index is invalid.
        TypeError: If the value to set is not an integer.
        ValueError: If the value to set is not a 32-bit integer.
    """
    def __init__(self):
        self.__registers = [0]*32

    def reg_to_index(self, reg):
        """
        Convert register name to index.

        Args:
            reg (str): Register name.

        Raises:
            RegisterIndexError: If the register name is invalid.

        Returns:
            int: Index of the register.
        """
        if reg in reg_map:
            index = int(reg_map[reg][1:])
        elif reg_valid(reg):
            index = int(reg[1:])
        else:
            raise RegisterIndexError
        return index

    def __getitem__(self, index):
        """
        Get the value of a register.

        Args:
            index (str or int): Register name or index.

        Returns:
            int: Value of the register.
        """
        index = index if isinstance(index, int) else self.reg_to_index(index)
        return self.__registers[index]

    def __setitem__(self, index, value):
        """
        Set the value of a register.

        Args:
            index (str or int): Register name or index.
            value (int): Value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not a 32-bit integer.
        """
        index = index if isinstance(index, int) else self.reg_to_index(index)
        if index == 0:
            return
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")

        if value < 0 or value > 0xFFFFFFFF:
            raise ValueError("Value must be a 32-bit integer")

        self.__registers[index] = value
