"""
Author: mk314k
This file contains an implementation of hardware memory and ADT for its content.
"""
from ..utility import num_to_bin
from ..exception import MemoryAddressError

class MemContent:
    """
    Abstract class (interface) representing content in memory.

    Methods:
        bin: Get the binary representation of the content.
        hex: Get the hexadecimal representation of the content.
        value: Get the numerical value of the content.

    Raises:
        NotImplementedError: If the methods are not implemented by the subclass.
    """
    @property
    def bin(self) -> str:
        """
        Get the binary representation of the content.

        Raises:
            NotImplementedError: If the method is not implemented.

        Returns:
            str: Binary representation of the content.
        """
        raise NotImplementedError

    @property
    def hex(self) -> str:
        """
        Get the hexadecimal representation of the content.

        Raises:
            NotImplementedError: If the method is not implemented.

        Returns:
            str: Hexadecimal representation of the content.
        """
        return hex(self.value)

    def __repr__(self)->str:
        return self.hex

    def __str__(self)->str:
        return self.hex

    @property
    def value(self) -> int:
        """
        Get the numerical value of the content.

        Raises:
            NotImplementedError: If the method is not implemented.

        Returns:
            int: Numerical value of the content.
        """
        raise NotImplementedError



class Data(MemContent):
    """
    Class representing data in memory.

    Attributes:
        data (int): Numerical value of the data.

    Methods:
        value: Get the numerical value of the data.
        bin: Get the binary representation of the data.

    Args:
        data (int): Numerical value to initialize the data with.
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
    Class representing memory.

    Attributes:
        memory (dict): Dictionary representing memory contents.
        head (int): Address to track the current position in memory.

    Methods:
        get(step=4): Get content from memory and move the head.
        push(val, step=4): Push content into memory and move the head.
        __call__(new_head): Set a new value for the head.
        __getitem__(address): Get content at a specific address.
        __setitem__(address, value): Set content at a specific address.

    Args:
        start_addr (int): Starting address for the memory. Defaults to 0.
    """
    def __init__(self, start_addr = 0):
        self.memory = {}
        self.head = start_addr

    def get(self, step = 4):
        """
        Get content from memory and move the head.

        Args:
            step (int, optional): Number of bytes to step. Defaults to 4.

        Returns:
            Any: Content from memory.
        """
        val = self.memory[self.head]
        self.head += step
        return val

    def push(self, val, step = 4):
        """
        Push content into memory and move the head.

        Args:
            val (Any): Content to push into memory.
            step (int, optional): Number of bytes to step. Defaults to 4.
        """
        self.memory[self.head] = val
        self.head += step

    def __call__(self, new_head:int):
        """
        Set a new value for the head.

        Args:
            new_head (int): New value for the head.
        """
        self.head = new_head


    def __getitem__(self, address: int) -> MemContent or None:
        data = self.memory.get(address, None)
        if (data is None): # pylint: disable=C0325 #if is needed here
            raise MemoryAddressError(f'{address} is an empty location')
        return data


    def __setitem__(self, address: int, value: MemContent) -> None:
        self.memory[address] = value

    def __repr__(self)->str:
        return self.memory.__repr__() + f" with head at {self.head}"
