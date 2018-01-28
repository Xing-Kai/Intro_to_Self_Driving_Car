import math

def shortest_path(M,start,goal):

	### data in M

	## 1. M.intersections - dict - x,y coordinate of every node.
	# {0: [0.7801603911549438, 0.49474860768712914],
 	# 1: [0.5249831588690298, 0.14953665513987202],
	# 2: [0.8085335344099086, 0.7696330846542071],
	# ......
	# 37: [0.3345284735051981, 0.6569436279895382],
	# 38: [0.17972981733780147, 0.999395685828547],
	# 39: [0.6315322816286787, 0.7311657634689946]}

	## 2. M.roads - list - roads[i] contains a list of the intersections that node i connects to.
	# [[36, 34, 31, 28, 17],
	# [35, 31, 27, 26, 25, 20, 18, 17, 15, 6],
	# [39, 36, 21, 19, 9, 7, 4],
	# ......
	# [12, 16, 22, 29],
	# [23, 29, 32],
	# [2, 4, 7, 22, 28, 36]]

	## initialise 
	frontier = set()
	known = set()
	path = []

	## calculate distance between two nodes
	def distance(i,j):
		return math.sqrt((M.intersections[i][0] - M.intersections[j][0])**2 + (i.y_coornidate - j.y_coornidate)**2)

	## initialise start node
	start.g = 0
	start.h = distance(start, goal)
	start.f = start.g + start.h
	start.parent = false

	## add start to frontier
	frontier.append(start)

	## choose the node with minimal f in frontier
	def choose_search_node(frontier):
		## find the minimal f in frontier
		f_min = min(frontier.f)
		## return the node number that has minimal f
		return f_min[0]

	## search the neighbors of node i with minimal f, updating g and f of it's neighbors
	## adding neighbors to frontier, remove i from frontier to known
	def search(i):
		for j in i.neighbors:
			## choose neighbors that is not in known
			if j not in known:
				## update g(i), f(i)
				w(ij) = distance(i, j)
				j.g = i.g + w(ij) ## w(ij) is the distance between i and j
				j.h = distance(j, goal)
				j.f = j.g + j.h ## j.h is the hypothesis distance between node j and goal
				## update j's parent node to i
				j.parent = i
				## add j to frontier
				if j not in frontier:
					frontier.append(j)

		## move i from frontier to known
		frontier.remove(i)
		known.append(i)

		return frontier, known


	while frontier != ():
		## choose search node in frontier
		i = choose_search_node(frontier)

		## search in i's neighbors, updating frontier and known
		frontier, known = search(i)

		## if goal is in frontier, and goal has the minimal f, then the path is found, break the loop
		if goal in frontier:
			if goal == choose_search_node(frontier):
				frontier.remove(goal)
				known.append(goal)
				path.append(goal)
				break


	## if find a shortest path to goal, then trace back to start, return the path
	if i == goal:
		i = goal
		while parent:
			path.append(i.parent)
			i = i.parent
		return path

	## if the frontier is empty, yet the goal hasn't been reached
	if frontier == [] and i != goal:
		return "path not find"





    print("shortest path called")
    return