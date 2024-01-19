"""
_summary_

Raises:
    NotImplementedError: _description_
    NotImplementedError: _description_
    NotImplementedError: _description_

Returns:
    _type_: _description_
"""
from ..utility import num_to_bin
class MemContent:
    """
    _summary_
    """
    @property
    def bin(self) -> str:
        """
        _summary_

        Raises:
            NotImplementedError: _description_

        Returns:
            str: _description_
        """
        raise NotImplementedError

    @property
    def hex(self) -> str:
        """
        _summary_

        Raises:
            NotImplementedError: _description_

        Returns:
            str: _description_
        """
        return hex(self.value)

    @property
    def value(self) -> int:
        """
        _summary_

        Raises:
            NotImplementedError: _description_

        Returns:
            int: _description_
        """
        raise NotImplementedError



class Data(MemContent):
    """
    _summary_

    Args:
        MemContent (_type_): _description_
    """
    def __init__(self, data: int):
        self.data = data

    @property
    def value(self) -> int:
        return self.data

    @property
    def bin(self) -> str:
        return num_to_bin(self.data, 32)


class Memory:
    """
    _summary_
    """
    def __init__(self, start_addr = 0):
        self.memory = {}
        self.head = start_addr

    def get(self, step = 4):
        """
        _summary_

        Args:
            step (int, optional): _description_. Defaults to 4.

        Returns:
            _type_: _description_
        """
        val = self.memory[self.head]
        self.head += step
        return val

    def push(self, val, step = 4):
        """
        _summary_

        Args:
            val (_type_): _description_
            step (int, optional): _description_. Defaults to 4.
        """
        self.memory[self.head] = val
        self.head += step

    def __call__(self, new_head:int):
        self.head = new_head


    def __getitem__(self, address: int) -> MemContent or None:
        return self.memory.get(address, None)

    def __setitem__(self, address: int, value: MemContent) -> None:
        self.memory[address] = value
