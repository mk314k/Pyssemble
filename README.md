# PySsemble

PySsemble is a Python library that allows you to write assembly code and debug it with a Python-like experience. It provides a set of tools for processing and assembling assembly code, as well as a built-in debugger for efficient debugging.

## Features

- Write assembly code using a Python-like syntax.
- Process and assemble assembly code with ease.
- Step through and debug assembly code with the built-in debugger.
- Comprehensive error handling and reporting.
- Lightweight and easy to integrate into existing projects.

## Installation
<!--
You can install PySsemble using pip:

pip install pyssemble
-->


## Usage

Here's a simple example demonstrating how to use PySsemble:

```python
from pyssemble import assembler, debugger

# Create an assembly program
program = """
MOV R1, 10
ADD R2, R1, 5
SUB R3, R2, 3
"""

# Assemble the program
assembled_code = assembler.assemble(program)

# Create a debugger and load the assembled code
dbg = debugger.Debugger()
dbg.load(assembled_code)

# Step through the code and print the state at each step
while not dbg.is_done():
    dbg.step()
    print(dbg.get_state())

# Get the final state
final_state = dbg.get_state()
print("Final State:", final_state)
