# demo.py
from spreadsheet import Spreadsheet

ops = ["Spreadsheet", "getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"]
args = [[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]

result = []
obj = None

for op, arg in zip(ops, args):
    if op == "Spreadsheet":
        obj = Spreadsheet(*arg)
        result.append(None)
    elif op == "setCell":
        obj.setCell(*arg)
        result.append(None)
    elif op == "resetCell":
        obj.resetCell(*arg)
        result.append(None)
    elif op == "getValue":
        val = obj.getValue(*arg)
        result.append(val)

print("Results:", result)
