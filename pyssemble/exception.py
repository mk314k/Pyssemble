"""
Exceptions raised during working with this package
"""
class PyAssembleException(Exception):
    """
    _summary_

    Args:
        Exception (_type_): _description_
    """
class PyAssembleSyntaxException(Exception):
    """
    _summary_

    Args:
        Exception (_type_): _description_
    """

class RegisterIndexError(PyAssembleException):
    """
    _summary_

    Args:
        pyAssembleException (_type_): _description_
    """

class MemoryAddressError(PyAssembleException):
    """

    Args:
        PyAssembleException (_type_): _description_
    """
