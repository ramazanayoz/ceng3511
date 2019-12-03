from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

import self as self
from ortools.sat.python import cp_model

#initial veriable
A1 = "none"
A2 = "none"
A3 = "none"
A4 = "none"
B1 = "none"
B2 = "none"
B3 = "none"
B4 = "none"
C1 = "none"
C2 = "none"
C3 = "none"
C4 = "none"
D1 = "none"
D2 = "none"
D3 = "none"
D4 = "none"

###load file
filepath = "futoshiki_input.txt"
try:
    filepath = sys.argv[1]
except:
    filepath = "futoshiki_input.txt"

theFile = open(filepath, "r")
B2 = "none"
D4 = "none"
for val in theFile:
    val = val.replace(",", "").split()
    if (val[1].isdigit()):
        exec(val[0] + "=" + "int(" + val[1] + ")")
theFile.close()

"""Minimal CP-SAT example to showcase calling the solver."""
# Creates the model.
model = cp_model.CpModel()

# Creates the variables.
num_vals = 5

if (A1 == "none"):
    A1 = model.NewIntVar(1, num_vals - 1, 'A1')
if (A2 == "none"):
    A2 = model.NewIntVar(1, num_vals - 1, 'A2')
if (A3 == "none"):
    A3 = model.NewIntVar(1, num_vals - 1, 'A3')
if (A4 == "none"):
    A4 = model.NewIntVar(1, num_vals - 1, 'A4')

if (B1 == "none"):
    B1 = model.NewIntVar(1, num_vals - 1, 'B1')
if (B2 == "none"):
    B2 = model.NewIntVar(1, num_vals - 1, 'B2')
if (B3 == "none"):
    B3 = model.NewIntVar(1, num_vals - 1, 'B3')
if (B4 == "none"):
    B4 = model.NewIntVar(1, num_vals - 1, 'B4')

if (C1 == "none"):
    C1 = model.NewIntVar(1, num_vals - 1, 'C1')
if (C2 == "none"):
    C2 = model.NewIntVar(1, num_vals - 1, 'C2')
if (C3 == "none"):
    C3 = model.NewIntVar(1, num_vals - 1, 'C3')
if (C4 == "none"):
    C4 = model.NewIntVar(1, num_vals - 1, 'C4')

if (D1 == "none"):
    D1 = model.NewIntVar(1, num_vals - 1, 'D1')
if (D2 == "none"):
    D2 = model.NewIntVar(1, num_vals - 1, 'D2')
if (D3 == "none"):
    D3 = model.NewIntVar(1, num_vals - 1, 'D3')
if (D4 == "none"):
    D4 = model.NewIntVar(1, num_vals - 1, 'D4')





# Creates the constraints.

###load file
theFile = open(filepath, "r")
for val in theFile:
    val = val.replace(",", "").split()
    if (val[1].isdigit()):
        # setattr(self,val[0], val[1])
        print(end="")
    else:
        exec("model.Add(" + val[0] + " > " + val[1] + ")")
theFile.close()


model.AddAllDifferent([A1, A2, A3, A4])
model.AddAllDifferent([B1, B2, B3, B4])
model.AddAllDifferent([C1, C2, C3, C4])
model.AddAllDifferent([D1, D2, D3, D4])

model.AddAllDifferent([A1, B1, C1, D1])
model.AddAllDifferent([A2, B2, C2, D2])
model.AddAllDifferent([A3, B3, C3, D3])
model.AddAllDifferent([A4, B4, C4, D4])


# Creates a solver and solves the model.
solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.FEASIBLE:
    print(str(solver.Value(A1)) + ", " + str(solver.Value(A2)) + ", " + str(solver.Value(A3)) + ", " + str(
        solver.Value(A4)))
    print(str(solver.Value(B1)) + ", " + str(solver.Value(B2)) + ", " + str(solver.Value(B3)) + ", " + str(
        solver.Value(B4)))
    print(str(solver.Value(C1)) + ", " + str(solver.Value(C2)) + ", " + str(solver.Value(C3)) + ", " + str(
        solver.Value(C4)))
    print(str(solver.Value(D1)) + ", " + str(solver.Value(D2)) + ", " + str(solver.Value(D3)) + ", " + str(
        solver.Value(D4)))

    print(" "+str(solver.Value(A1)) + ", " + str(solver.Value(A2)) + ", " + str(solver.Value(A3)) + ", " + str(
        solver.Value(A4))+"\n",
    str(solver.Value(B1)) + ", " + str(solver.Value(B2)) + ", " + str(solver.Value(B3)) + ", " + str(
        solver.Value(B4))+"\n",
    str(solver.Value(C1)) + ", " + str(solver.Value(C2)) + ", " + str(solver.Value(C3)) + ", " + str(
        solver.Value(C4))+"\n",
    str(solver.Value(D1)) + ", " + str(solver.Value(D2)) + ", " + str(solver.Value(D3)) + ", " + str(
        solver.Value(D4)), file=open('futoshiki_output.txt', 'w'))
