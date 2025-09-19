import heapq
class Spreadsheet(object):

    def __init__(self, rows):
        self.grid = {}

    def setCell(self, cell, value):
        self.grid[cell] = value

    def resetCell(self, cell):
        self.grid[cell] = 0
        

    def getValue(self, formula):
        if not formula.startswith("="):
            return int(formula)
        parts = formula[1:].split("+")
        total = 0
        for part in parts:
            part = part.strip()
            if part.isdigit():
                total += int(part)
            else:
                total += self.grid.get(part, 0)
                print(total)
        return total