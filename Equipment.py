from satispy import Variable, Cnf
from satispy.solver import Minisat
from functools import reduce


cnf_and = lambda xs: reduce(lambda a,b: a&b, xs)
cnf_or  = lambda xs: reduce(lambda a,b: a|b, xs)

def list_all(expr, verbose = True):
    solutions = []
    solver = Minisat()
    solution = solver.solve(expr)
    while solution.success:
        for v in solution.varmap:
            if solution[v] and verbose:
                print(v, end=" ", flush = True)
        expr = expr & -cnf_and([x if solution.varmap[x] else -x for x in solution.varmap])
        solution = solver.solve(expr)
        str_solution = {c.name: solution.varmap[c] for c in solution.varmap}
        solutions.append(str_solution)
        if verbose: print()
    else:
        print("No more solutions")
    return solutions


class World:
    '''Roster is an exhaustive dict of agents; Equipment is an exhaustive dict of resources
       Portfolio is a mapping (dict) from a subset of agents to a list of equipment they hold'''
    def __init__(self, roster = [], equipment = [], portfolio = {}):
        self.roster = {r: Variable(r) for r in roster}
        self.equipment = {e: Variable(e) for e in equipment}
        self.holdings = {a:
                [self.equipment[r] for r in portfolio[a]] for a in portfolio}
        list_diff = lambda xs,ys : list(set(xs).difference(set(ys)))
        self.neg_holdings = {a:
             list_diff(self.equipment.keys(), portfolio[a]) for a in self.holdings}
        self.neg_holdings = {a: [self.equipment[r] for r in self.neg_holdings[a]] for a in self.neg_holdings}
        self.roster_expression = reduce(lambda a,b: a|b, self.roster.values())
        self.equip_expression = reduce(lambda a,b: a|b, self.equipment.values())

        zs = []
        for a in self.neg_holdings:
            xs = reduce(lambda a,b:a|b,self.neg_holdings[a])
            xs = self.roster[a] >> -xs
            zs = zs + [xs]
        self.res_expression =  reduce(lambda a,b:a&b, zs)
        self.expression = self.roster_expression & self.res_expression & self.equip_expression
    def allocate_agents(self,equip_alloc):
        expr_alloc = cnf_and([self.equipment[e] for e in equip_alloc])
        expr = self.roster_expression & self.res_expression & expr_alloc
        return list_all(expr)
    def allocate_equipment(self,agent_alloc):
        expr_alloc = cnf_and([self.roster[r] for r in agent_alloc])
        expr = self.equip_expression & self.res_expression & expr_alloc
        return list_all(expr)
