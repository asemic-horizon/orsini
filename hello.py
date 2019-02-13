#from satispy import Variable, Cnf
from satispy import Variable, Cnf
from satispy.solver import Minisat


mon = Variable('mon')
tue = Variable('tue')
wed = Variable('wed')
thu = Variable('thu')
fri = Variable('fri')
sat = Variable('sat')
sun = Variable('sun')

#con1 = (mon | tue) & -wed &-thu &-fri &-sat & -sun
#con2 = -mon & (tue | wed) &-thu &-fri &-sat & -sun
con1 = (mon | tue)
con2 = (tue | wed)
exp = con1 & con2
solver = Minisat()

solution = solver.solve(exp)

if solution.success:
    print(type(solution))
    for v in solution.varmap:
      print(v, solution[v])
else:
    print("The expression cannot be satisfied")
