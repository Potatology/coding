graph = {
    'a': {'b' : 4, 'c': 5, 'd' : 6},
    'b': {'e': 7},
    'c': {'e': 4},
    'd': {'f': 4, 'e': 2},
    'e': {'f': 1, 'g': 3},
    'f': {'g': 1},
    'g':{}
}

processed = []
parents = { k: [] for k in graph.keys() }
for p in graph.keys():
    for c in graph[p].keys():
        parents[c].append(p)

print(parents)

costs = {k:v for k,v in graph['a'].items()}
costs['e'] = float('inf')
costs['f'] = float('inf')
costs['g'] = float('inf')
print(costs)

def find_lcn(costs):
    l_cost = float('inf')
    lcn = None
    for node in costs:
        cost = costs[node]
        if cost < l_cost and node not in processed:
            l_cost = cost
            lcn = node
    print(f'Lowest cost node: {lcn} : {costs}, processed: {processed}')
    return lcn

node = find_lcn(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lcn(costs)
print(costs['g'])
    