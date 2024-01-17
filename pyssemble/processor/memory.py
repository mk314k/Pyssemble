"""
_summary_

Raises:
    NotImplementedError: _description_
    NotImplementedError: _description_
    NotImplementedError: _description_

Returns:
    _type_: _description_
"""
class MemContent:
    """
    _summary_
    """
    def binary_rep(self) -> str:
        """
        _summary_

        Raises:
            NotImplementedError: _description_

        Returns:
            str: _description_
        """
        raise NotImplementedError

    def hex_rep(self) -> str:
        """
        _summary_

        Raises:
            NotImplementedError: _description_

        Returns:
            str: _description_
        """
        return hex(self.num_value())

    def num_value(self) -> int:
        """
        _summary_

        Raises:
            NotImplementedError: _description_

        Returns:
            int: _description_
        """
        raise NotImplementedError


def num_to_bin(num: int, bit_length: int = 5) -> str:
    """
    _summary_

    Args:
        num (int): _description_
        bit_length (int, optional): _description_. Defaults to 5.

    Returns:
        str: _description_
    """
    num_bin = bin(num)[2:]
    if len(num_bin) < bit_length:
        num_bin = "0" * (bit_length - len(num_bin)) + num_bin
    return num_bin


class Data(MemContent):
    """
    _summary_

    Args:
        MemContent (_type_): _description_
    """
    def __init__(self, data: int):
        self.data = data

    def num_value(self) -> int:
        return self.data

    def binary_rep(self) -> str:
        return num_to_bin(self.data, 32)


class Memory:
    """
    _summary_
    """
    def __init__(self):
        self.memory = {}

    def __getitem__(self, address: int) -> MemContent or None:
        return self.memory.get(address, None)

    def __setitem__(self, address: int, value: MemContent) -> None:
        self.memory[address] = value
