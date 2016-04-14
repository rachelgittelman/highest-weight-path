'''This script will calculate the highest weight path in a directed acyclic graph. It will
implement it using either a set of dictionaires, or a matrix, or a node class. It will 
assume that the nodes are already in topological order, but it will be possible to modify
this'''

'''an example file containing a DAG is given in example.DAG.txt'''

import sys

DAG_file=open(sys.argv[1])

'''First create a node class.'''
#####################################################################
class node:

	#node class will have a name, a highest weight parent, a highest weight
	#and a dictionary of child nodes (key=node, value=weight)
	
	def __init__(self, name, highest_weight_parent, highest_weight, parent_node_dict):
		self.highest_weight_parent = highest_weight_parent
		self.highest_weight = highest_weight
		self.parent_node_dict = parent_node_dict
	def reset_highest_weight_parent(self, new_node):
		self.highest_weight_parent = new_node
	def reset_highest_weight(self, new_weight):
		self.highest_weight = new_weight
	def add_parent_node(self, new_node, weight, edge):
		self.parent_node_dict[new_node]=[weight,edge]
	def __str__(self):
		return self.name
#####################################################################

'''First read in the DAG to a list of nodes. Because order is important, I can't just
make a dictionary. So I need to know which node is in which position of the list. 
make a dictionary with node as key and index as value.'''

node_list=[]
node_map={}
node_index=0
start_node=""
end_node=""

for line in DAG_file:
	fields=line.strip().split()
	if fields[0] == "v":
		node_list.append(node(fields[1], "", "", {}))
		node_map[fields[1]] = node_index
		try:
			if fields[2]=="START":
				start_node=fields[1]
			elif fields[2]=="END":
				end_node=fields[1]
		except:
			pass
	else:
		node_list[node_map[fields[3]]].add_parent_node(fields[2],int(fields[4]),fields[1])
	node_index += 1
	
'''Now parse through the node list in order, keeping track of the highest weight parent and
the highest weight for each node. Assume here that the path must go through the first and
last node.'''

max_weight=0
max_node=""
for node in node_list:
	
	'''found depth zero nodes. If the path is unconstrained, set all to zero. Otherwise, 
	only set start node to zero.'''
	if len(node.parent_node_dict) == 0:
		if start_node=="":
			node.reset_highest_weight(0)
		elif node.name==start_node:
			node.reset_highest_weight(0)
					
	else:																					##'''Otherwise, set highest weight and record highest weight parent'''
		for parent_node in node.parent_node_dict:
			##print parent_node
			##parent_weight=node_map[node.parent_node_dict[parent_node]].highest_weight
			parent_weight=node_list[node_map[parent_node]].highest_weight
			
			'''if the parent has no weight, that means the path is constrained and it can't
			be a candidate for the highest weight path. skip it.'''
			if parent_weight=="":
				if start_node != "":
					continue
				else:
					parent_weight=0															##parent weight wasnt set, but were not constrained. that means that the parent weight would have been negative 
			
			'''otherwise, find the new weight'''	
			edge_weight=node.parent_node_dict[parent_node][0]
			total_weight=parent_weight+edge_weight
			
			if total_weight < 0 and start_node=="":											## if we're not constrained to start at a certain point, don't consider paths that decrease the weight 
				continue
			
			if(total_weight > node.highest_weight or node.highest_weight==""):
				node.reset_highest_weight_parent(parent_node)
				node.reset_highest_weight(total_weight)
				
			'''also record the max weight and node overall'''
			if(total_weight > max_weight):
				max_weight=total_weight
				max_node=node.name
			
'''now parse backwards and print the highest weight path'''
def print_path(node_name):

	node=node_list[node_map[node_name]]
	print node
	if node.highest_weight_parent=="":
		return
	print node.parent_node_dict[node.highest_weight_parent][1]
	print_path(node.highest_weight_parent)
	

if end_node =="":
	print_path(max_node)
else:
	print_path(end_node)
	

			 
	