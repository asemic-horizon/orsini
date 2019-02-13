Minimal example (2D version)

    from Equipment import *
    agents = ['P1','P2']
    equipment = ['mon', 'tue','wed','thu','fri']
    portfolio = {'P1':['mon','tue','thu'], 'P2':['tue','wed','thu']}
    w = World(agents, equipment, portfolio)
    u = w.allocate_agents(['tue','wed'])

Output:

    P2 tue wed
    No more solutions
