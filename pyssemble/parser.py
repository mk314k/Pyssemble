"""
Author: mk314k
This file parses assembly code into ADT defined in instructions file
and store it in an Memory-like object for execution. The parse is done
in one pass here.
"""
from typing import Union, Dict
from .instruction import AssemblyInstruction, instructions
from .assembler.register import reg_valid
from .assembler.assembler import Assembler
from .exception import PyAssembleSyntaxException

labels: Dict[str, int] = {}
remove_paranthesis = str.maketrans('(',',',')')

def get_reg_num(arg: Union[str, None]) -> Union[str, int]:
    """
    Get the register number or label value.

    Args:
        arg (Union[str, None]): The register name or label.

    Returns:
        Union[str, int]: The register number or label value.
    """
    if arg is None:
        return ''
    arg = arg.strip()
    if arg in labels:
        return labels[arg]
    if reg_valid(arg):
        return arg
    return int(arg)

def parse(code: str):
    """
    Parse assembly code and update the instruction memory.

    Args:
        code (str): The assembly code.

    Raises:
        SyntaxError: If there is a syntax error in the code.
    """
    lines = code.split("\n")
    labels.clear()
    def process_arg(line_num:int, idrd:list[str], idrd_res:list[str])->AssemblyInstruction:
        """
        _summary_

        Args:
            line_num (int): current line number 
            idrd (list[str]): list of instruction id and maybe first register arg
            idrd_res (list[str]): list of whole line split by ','

        Raises:
            PyAssembleSyntaxException: when extra regs or comma convention is not followed
        Returns:
            AssemblyInstruction: instruction corresponding to the id with given regs
        """
        if len(idrd) > 2:
            raise PyAssembleSyntaxException(f"It seems you have extra space in line {line_num}")
        inst_id = instructions[idrd[0]]
        if len(idrd) == 1:
            # Instructions like ret
            return inst_id()
        arg1 = get_reg_num(idrd[1])
        if len(idrd_res) == 1:
            # Instructions like jal
            return inst_id(arg1)
        arg2 = get_reg_num(idrd_res[1])
        if len(idrd_res) == 2:
            # Instructions like li
            return inst_id(arg1, arg2)
        arg3 = get_reg_num(idrd_res[2])
        if len(idrd_res) == 3:
            # more general instructions like add
            return inst_id(arg1, arg2, arg3)
        raise PyAssembleSyntaxException(f"more registers than needed in line {line_num}")

    for line_num, line in enumerate(lines):
        line = line.strip()
        if line:
            if line.endswith(':'):
                labels[line[:-1]] = Assembler.inst_memory.head
            else:
                # A line shall be of form with atmost three arguments (reg or num)
                # inst rd, rs1, rs2
                # inst rd, offset(rs1)
                line = line.translate(remove_paranthesis)
                idrd_res = line.split(',')
                idrd = idrd_res[0].split(' ')
                if idrd[0] in instructions:
                    _ = process_arg(line_num, idrd, idrd_res)
                else:
                    raise SyntaxError(f"{idrd[0]} in line {line_num} is not defined instruction")

def parse2(code:str):
    """
    A two pass version of parser implemented above.

    Args:
        code (str): _description_
    """
    parse(code)
