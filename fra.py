# coding: utf-8
help(len)
len(...)
get_ipython().run_line_magic('pinfo', 'len')
L = [1, 2, 3]
get_ipython().run_line_magic('pinfo', 'L.insert')
get_ipython().run_line_magic('pinfo', 'len')
L = [1, 2, 3]
get_ipython().run_line_magic('pinfo', 'L.insert')
get_ipython().run_line_magic('pinfo', 'L')
# Docstring
def square(a):
    """Return the square of a."""
# Docstring
def square(a):
    """Return the square of a.
    return a ** 2
    """
get_ipython().run_line_magic('pinfo', 'square')
get_ipython().run_line_magic('pinfo2', 'square')
get_ipython().run_line_magic('pinfo2', 'len')
# Exploring Modules with Tab Completion
L.append
L.copy
L.extend
L.insert
L.remove
L.reverse
L.sort
L.clear
L.count
L.index
L.pop
L.__add__
# Tab completion when importing
from itertools import compress
import dis
import hashlib
# Beyond tab completion: WildCard matching
*Warning?ArithmeticError
# Beyond tab completion: WildCard matching
get_ipython().run_line_magic('psearch', '*Warning')
ArithmeticError
str.*find*?str
get_ipython().run_line_magic('psearch', 'str.*find*')
str.find
get_ipython().run_line_magic('psearch', 'str.*find*')
get_ipython().run_line_magic('psearch', 'str.*find*')
al
str
(reverse-i-search)'sqa'
get_ipython().run_line_magic('pinfo2', 'square')
(reverse-i-search)'':
(reverse-i-search)'sqa': def square(a):
(reverse-i-search)'sqa': def square(a):
        """Return the square of a"""
        return a ** 2
(reverse-i-search)'sqa': def square(a):
        """Return the square of a"""
        return a ** 2
def square(a):
    """Return the square of a"""
    return a ** 2
square(2)
get_ipython().run_line_magic('', 'aleyna')
get_ipython().run_line_magic('aleyna', '')
get_ipython().run_line_magic('square', '')
# IPython Magic Commands:
get_ipython().run_line_magic('aleyna', '')
get_ipython().run_cell_magic('aleyna', '', '')
# Pasting Code Blocks : %paste and %cpaste
def donothing(x):
    return x
def donothind(x):
        return x
def donothing(x):
        return x
def donothing(x):
        return x
get_ipython().run_line_magic('paste', '')
def donothing(x):
    return x
print(__)
print(_)
print(___)
# Input and Output History
import math
math.sin()
# Input and Output History
import math
math.sin(2)
math.cos(2)
print(In)
out
Out
print(In[1])
print(Out[1])
print(Out[2])
print(Out[])
print(Out[0)
print(Out[0])
print(Out[2)
print(Out[2])
print(ot[2])
print(ou[2])
print(Out[2])
print(Out[48])
print(In[47])
Out[48] **  + Out[49] ** 
Out[48] ** 2 + Out[49] ** 2
# Underscore Shortcuts and Previous Outputs
print(_)
print(__)
print(___)
Out[48]
_48
# Suppressing Output
math.sin(2) + math.cos(2)
# Suppressing Output
math.sin(2) + math.cos(2);
14 in Out
74 in Out
get_ipython().run_line_magic('history', '-n 1-4')
# For more information:
get_ipython().run_line_magic('pinfo', '%history')
# Similar:
get_ipython().run_line_magic('rerun', '')
# Similar:
get_ipython().run_line_magic('rerun', '-n 1-4')
# Similar:
get_ipython().run_line_magic('rerun', '1:4')
# Similar:
get_ipython().run_line_magic('rerun', '"1:4"')
# Similar:
get_ipython().run_line_magic('rerun', '-n 1:4')
# Similar:
get_ipython().run_line_magic('rerun', '-n 1:4:')
# Similar:
get_ipython().run_line_magic('rerun', '1:4:')
# Similar:
get_ipython().run_line_magic('rerun', '1:4')
get_ipython().run_line_magic('save', '')
get_ipython().run_line_magic('save', '-n 1-4')
