from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

import self as self
from ortools.sat.python import cp_model


def SimpleSatProgram():
    ###load file

    filepath = "kakuro_input.txt"
    try:
        filepath = sys.argv[1]
    except:
        filepath = "kakuro_input.txt"

    theFile = open(filepath, "r")
    array = []
    for val in theFile.read().split():
        val = val.replace(",", "")
        array.append(int(val))
    theFile.close()


    """Minimal CP-SAT example to showcase calling the solver."""
    # Creates the model.
    model = cp_model.CpModel()

    # Creates the variables.
    num_vals = 10
    a1 = "X"
    a2 = array[0]
    a3 = array[1]
    a4 = array[2]


    b1 = array[3]
    b2 = model.NewIntVar(1, num_vals - 1, 'b2')
    b3 = model.NewIntVar(1, num_vals - 1, 'b3')
    b4 = model.NewIntVar(1, num_vals - 1, 'b4')

    c1 = array[4]
    c2 = model.NewIntVar(1, num_vals - 1, 'c2')
    c3 = model.NewIntVar(1, num_vals - 1, 'c3')
    c4 = model.NewIntVar(1, num_vals - 1, 'c4')


    d1 = array[5]
    d2 = model.NewIntVar(1, num_vals - 1, 'd2')
    d3 = model.NewIntVar(1, num_vals - 1, 'd3')
    d4 = model.NewIntVar(1, num_vals - 1, 'd4')


    # Creates the constraints.

    model.AddAllDifferent([b2,b3,b4])
    model.AddAllDifferent([c2,c3,c4])
    model.AddAllDifferent([d2,d3,d4])

    model.AddAllDifferent([b2,c2,d2])
    model.AddAllDifferent([b3,c3,d3])
    model.AddAllDifferent([b4,c4,d4])




    #
    model.Add(a2 == b2 + c2 + d2)
    model.Add(a3 == b3 + c3 + d3)
    model.Add(a4 == b4 + c4 + d4)
    #
    model.Add(b1 == b2 + b3 + b4)
    model.Add(c1 == c2 + c3 + c4)
    model.Add(d1 == d2 + d3 + d4)



    # Creates a solver and solves the model.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE:
        print(" "+a1+ ", "+str(a2)+", " +str(a3)+", "+str(a4), "\n",
        str(b1)+ ", "+str(solver.Value(b2))+", " +str(solver.Value(b3))+", "+str(solver.Value(b4)), "\n",
        str(c1)+ ", "+str(solver.Value(c2))+", " +str(solver.Value(c3))+", "+str(solver.Value(c4)), "\n",
        str(d1)+ ", "+str(solver.Value(d2))+", " +str(solver.Value(d3))+", "+str(solver.Value(d4)))

        print(" "+a1+ ", "+str(a2)+", " +str(a3)+", "+str(a4), "\n",
        str(b1)+ ", "+str(solver.Value(b2))+", " +str(solver.Value(b3))+", "+str(solver.Value(b4)), "\n",
        str(c1)+ ", "+str(solver.Value(c2))+", " +str(solver.Value(c3))+", "+str(solver.Value(c4)), "\n",
        str(d1)+ ", "+str(solver.Value(d2))+", " +str(solver.Value(d3))+", "+str(solver.Value(d4)),file=open('kakuro_output.txt', 'w'))


SimpleSatProgram()