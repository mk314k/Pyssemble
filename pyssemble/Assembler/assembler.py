"""
_summary_
"""
from .register import RegisterSet, Counter
from .memory import Memory

class Assembler:
    """
    _summary_
    """
    registers = RegisterSet()
    data_memory = Memory()
    inst_memory = Memory()
    pc = Counter()
