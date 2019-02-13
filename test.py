from Equipment import *

agents = ['North','South','West','East']
equipment = ['beach','heat','quiet','ocean']

portfolio = {'North':['heat'],'West':['heat','quiet'], 'South':['beach','heat'],'East':['ocean','quiet']}

# agents = ['P1','P2']
# equipment = ['mon', 'tue','wed','thu','fri']
# portfolio = {'P1':['mon','tue','thu'], 'P2':['tue','wed','thu']}
w = World(agents, equipment, portfolio)

u = w.allocate_agents(['heat'])
print()
#v = w.allocate_equipment(['West','North'])
# from satispy import Variable, Cnf
# from satispy.solver import Minisat
#
# solver = Minisat()
# exp = w.roster_expression & w.res_expression & w.equipment['thu']
# print(exp)
# # solution = solver.solve(exp)
# while solution.success:
#     for v in solution.varmap:
#         if solution[v]:# v.name in w.equipment.keys():
#             print(v, solution[v], end=",", flush = True)
#     print('---')
#     new_cond = [x if solution.varmap[x] else -x for x in solution.varmap]
#     exp = exp & -reduce(lambda a,b:a&b, new_cond)
#     solution = solver.solve(exp)
# else:
#     print("No more solutions")
