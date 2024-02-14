# Pyssemble

Pyssemble is a Python library that allows you to write assembly code and debug it with a Python-like experience. It provides a set of tools for processing and assembling assembly code, as well as a built-in debugger for efficient debugging.

## Features

- Write assembly code using a Python-like syntax.
- Process and assemble assembly code with ease.
- Step through and debug assembly code with the built-in debugger.
- Lightweight and easy to integrate into existing projects.

## Installation
<!--
You can install PySsemble using pip:

pip install pyssemble
-->

## Usage

The examples can be seen in the example folder as notebooks, here's one simple example demonstrating how to use Pyssemble:

```python
# Import Registers and Instructions and Assembler
from pyssemble import *

# Set an address for first instruction
Assembler.inst_memory(440)

# Write Assembly Program
Li(a1, 10)
Add(a2, a3, a1)
Ret()

# OR write Assembly program as string
program = """
li a1, 10
add a2, a1, a3
ret
"""
code_from_string(program)

# Execute the program
Assembler.execute(440)

# Read Values
print(a1.value, a2.value)
# Should give 10, 10
```

<!--
# # Create a debugger and load the assembled code
# dbg = debugger.Debugger()
# dbg.load(assembled_code)

# # Step through the code and print the state at each step
# while not dbg.is_done():
#     dbg.step()
#     print(dbg.get_state())

# # Get the final state
# final_state = dbg.get_state()
# print("Final State:", final_state)
-->