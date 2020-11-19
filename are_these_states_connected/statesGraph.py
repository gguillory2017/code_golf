import networkx as nx

file_raw = open("states_list.txt").read()

state_pairs = file_raw.split()
state_set = set(file_raw.replace("\n", ",").split(","))

state_graph = nx.Graph()

for state in state_set:
    state_graph.add_node(state)

for pair in state_pairs:
    pair_list = pair.split(",")
    state_graph.add_edge(pair_list[0], pair_list[1])

print("Number of nodes in state graph: " + str(state_graph.number_of_nodes()))

# Uncomment the line below to produce a graph of the states
#nx.draw_kamada_kawai(state_graph, with_labels=True)

input_states_string = str(input(
    "Enter a list of states below. Use all capital letters, separated by commas"+
    ". Do not end or start the list with a comma.\n"))

input_states_list = input_states_string.split(",")

input_states_list = filter(lambda s: s not in state_set, input_states_list)

print(input_states_list)