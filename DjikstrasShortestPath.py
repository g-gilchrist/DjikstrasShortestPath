
graph = {

    'a':{'b':4, 'c':2},
    'b':{'a':4, 'c':1, 'd':5},
    'c':{'a':2, 'b':1, 'd':8, 'e':10},
    'd':{'b':5, 'c':8, 'e':2, 'z':6},
    'e':{'c':10, 'd':2,'z':5},
    'z':{'d':6, 'e':5},
}
  
# Create Dijkstra's Shortest Path Alogrithm in a function
def dijkstraPath (graph,start,end):
    minDistance = {}
    visitedNodes = {}
    unvisitedNodes = graph
    infinity = 19 # this has to be a value larger than the ammount of keys in the dictionary
    route = []
    # Dijkstra's algorithm sets the start node to zero and all other nodes to infinity to begin
    for node in unvisitedNodes:
        minDistance[node] = infinity
    minDistance[start] = 0
       
    # Continue until all nodes in the graph have been checked
    # It will then iterate through the queue finding the most efficient path to each node
    while unvisitedNodes:
        runtNode = None
        for node in unvisitedNodes:
            if runtNode is None:
                runtNode = node
            elif minDistance[node] < minDistance[runtNode]:
                runtNode = node            
      
        # this seperates the dictionary into a list of a specific node's neighbors
        Neighbors = graph[runtNode].items()

        # this takes the new list and assigns a variable to the neigborNode and it's weight
        # We can then check if the runtNode is weighted less than it's neigborNode
        # We compare these weights to find the least weighted route from the Start node to the end Node
        # if we find a more effecient route we will then add it to the visitedNodes and pop it out of the unvisitedNodes
        for neigborNode, weight in Neighbors:
            if weight + minDistance[runtNode] < minDistance[neigborNode]:
                minDistance[neigborNode] = weight + minDistance[runtNode]
                visitedNodes[neigborNode] = runtNode
     
        unvisitedNodes.pop(runtNode)
    
    # Finally we work backwards from the end node inserting the vistedNodes into our route until we get back to the start node.
    # Because we stop when the currentNode reaches the start node we will finally insert the start node into the path and we are done.
    # If a path is unreachable or perhaps is not even on the graph at all it will error.
    currentNode = end
     
    while currentNode != start:
        try:
            route.insert(0, currentNode)
            currentNode = visitedNodes[currentNode]

        except KeyError:
            print('Path is not reachable. ')
            break
    route.insert(0,start)
         
    # We now simply print off the route, I've added the minDistance as well se we can see the final weight of the quickest path
    print("\n""Dijkstra's Shortest Path Algorithm: ")
    print('Shortest distance: ' + str(minDistance[end]))
    print('Shortest path: ' + str(route))
         
     
# This calls the dijkstraPath function
dijkstraPath(graph,'a','z')

