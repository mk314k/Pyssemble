"""
_summary_

Raises:
    RegisterIndexError: _description_
    RegisterIndexError: _description_

Returns:
    _type_: _description_
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
    _summary_

    Args:
        reg (_type_): _description_

    Returns:
        _type_: _description_
    """
    pattern = r'^x([0-9]|[1-2]\d|3[0-1])$'
    return bool(re.match(pattern, reg)) or (reg in reg_map)


class Counter:
    """
    _summary_
    """
    def __init__(self, val=0):
        self.val = val

    def __call__(self):
        return self.val

    def step(self):
        """
        _summary_
        """
        self.val += 4

    def jump(self, val:int):
        """
        _summary_

        Args:
            val (int): _description_
        """
        self.val = val

class RegisterSet:
    """
    _summary_
    """
    def __init__(self):
        self.__registers = [0]*32
    def reg_to_index(self, reg):
        """
        _summary_

        Args:
            reg (_type_): _description_

        Raises:
            RegisterIndexError: _description_

        Returns:
            _type_: _description_
        """
        if reg in reg_map:
            index = int(reg_map[reg][1:])
        elif reg_valid(reg):
            index = int(reg[1:])
        else:
            raise RegisterIndexError
        return index
    def __getitem__(self, index):
        index = index if isinstance(index, int) else self.reg_to_index(index)
        return self.__registers[index]

    def __setitem__(self, index, value):
        index = index if isinstance(index, int) else self.reg_to_index(index)
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")

        if value < 0 or value > 0xFFFFFFFF:
            raise ValueError("Value must be a 32-bit integer")

        self.__registers[index] = value
