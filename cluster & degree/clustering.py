import snap

UGraph = snap.LoadConnList(snap.PUNGraph, "com-youtube.ungraph.txt")

'''
for EI in UGraph.Edges():
    print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())
'''

'''
#Returns the (approximation of the) Effective Diameter (90-th percentile of the distribution of shortest path lengths) of a graph (by performing BFS from NTestNodes random starting nodes).
NTestNodes = 10
IsDir = False
EffDiam = snap.GetBfsEffDiam(UGraph, NTestNodes, IsDir)
print EffDiam

#Returns a 90th percentile of the shortest path length distribution of a Graph (based on a NRuns runs of Approximate Neighborhood Function of approximation quality NApprox).
AnfEffDiam = snap.GetAnfEffDiam(UGraph)
print AnfEffDiam

#Computes the diameter, or 'longest shortest path', of a Graph by performing a breadth first search over the Graph. This diameter is approximate, as it is calculated with an NTestNodes number of random starting nodes.
diam = snap.GetBfsFullDiam(UGraph, 1000, False)
print diam
'''

cf = snap.GetClustCf(UGraph)
print cf

snap.PlotClustCf(UGraph, "com-youtube.ungraph", "com-youtube.ungraph - clustering coefficient")

snap.PlotInDegDistr(UGraph, "com-youtube.ungraph", "com-youtube.ungraph - in-degree Distribution")