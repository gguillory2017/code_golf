import networkx as nx

file_raw = open("states_list.txt").read()
state_pairs = file_raw.split()
state_set=set(file_raw.replace("\n", ",").split(","))

