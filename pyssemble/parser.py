"""
_summary_

Raises:
    SyntaxError: _description_

Returns:
    _type_: _description_
"""
from typing import Union, Dict
from .pyInstruction import AssemblyInstruction, instructions
from .register import reg_valid
from .exception import PyAssembleSyntaxException

labels: Dict[str, int] = {}
remove_paranthesis = str.maketrans('(',',',')')

def get_reg_num(arg: Union[str, None]) -> Union[str, int]:
    """
    _summary_

    Args:
        arg (Union[str, None]): _description_

    Returns:
        Union[str, int]: _description_
    """
    if arg is None:
        return ''
    arg = arg.strip()
    if arg in labels:
        return labels[arg]
    if reg_valid(arg):
        return arg
    return int(arg)

PseudoMem = Dict[int, AssemblyInstruction]

def parser(code: str, start_addr=540, memory=None) -> Union[PseudoMem, None]:
    """
    _summary_

    Args:
        code (str): _description_
        start_addr (int, optional): _description_. Defaults to 540.
        memory (_type_, optional): _description_. Defaults to None.

    Raises:
        SyntaxError: _description_

    Returns:
        Union[PseudoMem, None]: _description_
    """
    lines = code.split("\n")
    inst_mem = memory if memory is not None else {}
    addr = start_addr
    labels.clear()
    def process_arg(idrd, idrd_res)->AssemblyInstruction:
        if len(idrd) > 2:
            raise PyAssembleSyntaxException
        inst_id = instructions[idrd[0]]
        if len(idrd) == 1:
            return inst_id()
        arg1 = get_reg_num(idrd[1])
        if len(idrd_res) == 1:
            return inst_id(arg1)
        arg2 = get_reg_num(idrd_res[1])
        if len(idrd_res) == 2:
            return inst_id(arg1, arg2)
        arg3 = get_reg_num(idrd_res[2])
        if len(idrd_res) == 3:
            return inst_id(arg1, arg2, arg3)
        raise PyAssembleSyntaxException("")

    for line in lines:
        line = line.strip()
        if line:
            if line.endswith(':'):
                labels[line[:-1]] = addr
            else:
                line = line.translate(remove_paranthesis)
                idrd_res = line.split(',')
                idrd = idrd_res[0].split(' ')
                if idrd[0] in instructions:
                    inst = process_arg(idrd, idrd_res)
                    inst_mem[addr] = inst
                    addr += 4
                else:
                    raise SyntaxError(f"{idrd[0]} is not a defined Assembly instruction")

    if memory is None:
        return inst_mem
