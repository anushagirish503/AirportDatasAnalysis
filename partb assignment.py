
################################################## Part B ##############################################
# load data to data frame (airplane delay)

from pyflowchart import Flowchart

with open('Part A & B.py') as f:
    code = f.read()
fc = Flowchart.from_code(code,field="",inner=True,simplify=True,conds_align=False)
print(fc.flowchart())

