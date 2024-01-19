"""
_summary_
"""
from .register import RegisterSet, Counter, reg_valid
from .memory import Memory
from ..exception import RegisterIndexError

class Assembler:
    """
    _summary_
    """
    registers = RegisterSet()
    data_memory = Memory()
    inst_memory = Memory()
    pc = Counter()
    def execute(self, addr = 540):
        """
        _summary_

        Args:
            addr (int, optional): _description_. Defaults to 540.
        """
        Assembler.pc.jump(addr)
        while Assembler.pc() != 0:
            Assembler.inst_memory[Assembler.pc()].execute()
            Assembler.pc.step()

class AssemblerReg:
    """
    summary
    """
    def __init__(self, name:str|int):
        if isinstance(name, int) and (0<=name <=31):
            self.__name = f'x{name}'
        elif isinstance(name, str) and reg_valid(name):
            self.__name = name
        else:
            raise RegisterIndexError()
    def __repr__(self):
        return self.__name
    def __call__(self, val:int|None = None)->int:
        if val is not None:
            Assembler.registers[self.__name] = val
        return Assembler.registers[self.__name]
    @property
    def value(self)->int:
        """
        _summary_

        Returns:
            int: _description_
        """
        return Assembler.registers[self.__name]
    @value.setter
    def value(self, val:int):
        Assembler.registers[self.__name] = val
