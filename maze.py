import sys 

class Node():
    def __init__(self, state, parent , action ):
        self.state = state
        self.parent = parent
        self.action = action 

class StackFrontier():
    def __init__(self):
        self.Frontier = []
    
    def add(self, node ):
        self.Frontier.append(node)

    def contains_state(self , state ):
        return any(node.state == state for node in self.Frontier)

    def empty(self):
        return len(self.Frontier) == 0 

    def remove(self):
        if self.empty():
            raise Exception("This Frontier is empty ")
        else:
            node = self.Frontier[-1]
            self.Frontier = self.Frontier[:-1]
            return node

class Queuefrontier():
    def Remove(self):
        if self.empty():
            raise Exception("This is an Empty Frontier")
        else:

            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            
            return node

class Maze():
    def __init__(self , filename):
        # Read file and set height and width of mazee

        with open(filename) as f :
            contents = f.read()
        
        # validate start and goal 
        if contents.count("A") != 1:
            raise Exception("maize have exactly one starting point ")
        if contents.count("B") != 1 :
            raise Exception("maize should have only ond destination Point ")
        
        # determint height and width of the maze 

        contents = contents.splitlines()
        self.height = len(contents)
        self.width = len(contents)

        # Keep tracks of the walls 

        self.walls=[]

        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i,j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal == (i,j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            
            self.walls.append(row)
        self.solution = None

    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i , row  in enumerate(self.walls):
            for j, col in enumerate(row):
                if col : 
                    print ("☒",end= "")
                elif (i,j)== self.start:
                    print("A" , end= "")
                elif (i,j) == self.goal:
                    print("B" , end = "")
                elif solution is not None and (i,j) in solution :
                    print("*", end= "")
                else : 
                    print (" ", end = "")

            print()
        print()

    def neighbours(self, state):
        row , col = state

        # All Possible actions 

        candidates = [

            ("up", (row-1, col)),
             ("down", (row+1, col)),
              ("left", (row, col-1)),
               ("right", (row, col+1)),

        ]

        # Ensure actions are valid 
        result = []
        for action , (r,c) in candidates:
            try :
                if not self.walls[r][c]:
                    result.append((action , (r,c)))
            except IndexError:
                continue
        return result

        

    def solve(self):
        # find a solution to maze if one exists 

        # keepps no of states explored 
        self.num_explored = 0 

        # initialized frontieer to just the start position 

        start = Node(state=self.start, parent= None, action=None)
        frontier = StackFrontier()
        frontier.add(start)

        # initialized an empty explores set 
        self.explored = set()

        # keep looping until solution found 
        while True:

            # check if frontier is empty 
            if frontier.empty():
                raise Exception("No solution ")

            # choose a node from the forntier 
            node = frontier.remove()
            self.num_explored += 1

            # if noed is the goal then we have the solution 

            if node.state == self.goal:
                actions=[]
                cells = []

                # follow parent node to find a solution 
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells )
                return 

            # mark node as explored 
            self.explored.add(node.state)

            # add neightbour to the frontier 
            for action ,state in self.neighbour(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state ,parent=node, action=action )
                    frontier.add(child)


        def self_image(self,filename , show_solution= True, show_Explored = False):
            

