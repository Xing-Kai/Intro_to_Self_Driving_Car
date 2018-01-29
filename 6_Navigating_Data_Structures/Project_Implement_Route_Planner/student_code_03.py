'''
> shortest_path(map_40, 5, 34)
[5, 16, 37, 12, 34]
'''

import math
import heapq

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

	## initialize 
	frontier = set()
	frontier_heap = []
	known = set()
	path = []

	## calculate distance between two nodes
	def distance(i,j):
		return math.sqrt((M.intersections[i][0] - M.intersections[j][0])**2 + (M.intersections[i][1] - M.intersections[j][1])**2)

	## initialize start node
	node = {}
	node[start] = {'g': 0, 
					'h': distance(start, goal), 
					'f': 0 + distance(start, goal), 
					'parent': None }

	## add start to frontier
	frontier.add(start)
	## add start to priority queue frontier_heap
	heapq.heappush(frontier_heap, (node[start]['f'], start))

	## search for shortest path
	while frontier != ():
		## choose search node i with minimal f in frontier as the searching node
		i = heapq.heappop(frontier_heap)[1]

		## search the neighbors of node i, update  it's neighbors
		for j in M.roads[i]:
			## choose neighbors that is not in known
			if j not in known:
				## initialize or update node j
				if (j not in frontier) or ((node[i]['g'] + distance(i, j) + distance(j, goal)) < node[j]['f']):
					node[j] = {'g': node[i]['g'] + distance(i, j), 
								'h': distance(j, goal), 
								'f': node[i]['g'] + distance(i, j) + distance(j, goal), 
								'parent': i }

					## add j to frontier
					frontier.add(j)
					## add j to priority queue frontier_heap
					heapq.heappush(frontier_heap, (node[j]['f'], j))

		## move i from frontier to known
		frontier.remove(i)
		known.add(i)

		## if goal has been searched and moved to known, then the path is found, contruct the path and break the loop
		if goal in known:
			i = goal
			while i:
				path.append(i)
				i = node[i]['parent']
			path.reverse()
			break

	return path
