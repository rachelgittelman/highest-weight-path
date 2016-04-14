'''This function will make the edit graph for two sequences, given a 
substitution matrix and a gap penalty. Make sure nodes are printed in 
correct order!'''


weights={"A":{"A":5, "C":-5, "G":0, "T":-5},
"C":{"A":-5, "C":5, "G":-5, "T":0},
"G":{"A":0, "C":-5, "G":5, "T":-5},
"T":{"A":-5, "C":0, "G":-5, "T":5}}

gap_penalty=-6

seqx="TAG"
seqy="TGG"

'''print vertices'''
for x in xrange(0,len(seqx)+1):
	for y in xrange(0,len(seqy)+1):
		print "v\t"+"".join(["(",str(x),",",str(y),")"])
		
'''print edges for nodes that have all 3 edges. If I'm at the end of x or y, print
the edges for nodes with just a single edge'''
for x in xrange(len(seqx)):
	for y in xrange(len(seqy)):
		'''print down'''
		label="-"+seqy[y]
		weight=gap_penalty
		print "\t".join(["e",label,"".join(["(",str(x),",",str(y),")"]), "".join(["(",str(x),",",str(y+1),")"]), str(weight)])

		'''print across'''
		label=seqx[x]+"-"
		weight=gap_penalty
		print "\t".join(["e",label,"".join(["(",str(x),",",str(y),")"]), "".join(["(",str(x+1),",",str(y),")"]), str(weight)])

		'''print diagonal'''
		label=seqx[x]+seqy[y]
		weight=weights[seqx[x]][seqy[y]]
		print "\t".join(["e",label,"".join(["(",str(x),",",str(y),")"]), "".join(["(",str(x+1),",",str(y+1),")"]), str(weight)])
		
		'''if we're at the end of a column, print the node with a single edge'''
		if y == len(seqy)-1:
			label=seqx[x]+"-"
			weight=gap_penalty
			print "\t".join(["e",label,"".join(["(",str(x),",",str(y+1),")"]), "".join(["(",str(x+1),",",str(y+1),")"]), str(weight)])
	
	'''if we're at the end of a row, print the node with a single edge downwards'''
	if x == len(seqx)-1:
		label="-"+seqy[y]
		weight=gap_penalty
		print "\t".join(["e",label,"".join(["(",str(x+1),",",str(y),")"]), "".join(["(",str(x+1),",",str(y+1),")"]), str(weight)])
			
		