"""
_summary_
"""
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
        num_bin = "0b"+"0" * (bit_length - len(num_bin)) + num_bin
    return num_bin
