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
from pyssemble import Pyssemble

# Set an address for first instruction and
# import all registers and instructions
Pyssemble.initiate(440)

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
Pyssemble.load(program)

# Execute the program
Pyssemble.execute(440)

# Read Values
print(a1.value, a2.value) # Should give 10, 10

# For Debugging
from pyssemble import Debugger
Debugger.initiate()

# Now you can add print instructions
Li(a1, 10)
PrintR(a1)
Add(a2, a3, a1)
PrintR(a2)
Ret()

# Now when executing, we should expect values to be printed
Pyssemble.execute(440) # Should give 10, 10

# Or we can execute step by step using
Debugger.step()

```
