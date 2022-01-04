from cmu_112_graphics import *
import random
import time, math

#takes user inputs for the user name and wanted level of play 
USERNAME = input("Enter Username: ")
LEVEL = 10* int(input ("Choose your hardness: 1, 2, or 3: "))

#directions used to create the maze
NORTH = (-1,0)
SOUTH = (1,0)
EAST  = (0,1)
WEST  = (0,-1)

def appStarted(app):
    app.rows = int(LEVEL)
    app.cols = int(LEVEL)
    app.path = set()
    app.solution = None
    app.playerLocation = (0,0)
    app.playerXCoord = 0 
    app.playerYCoord = 0
    app.finalLocation = ((app.rows -1), (app.cols -1))
    app.path.add(app.playerLocation)
    app.cellWidth = (app.width)/app.cols
    app.cellHeight = (app.height)/app.rows
    app.maze = makeMaze(app.rows, app.cols)
    # http://clipart-library.com/ocean-background-cliparts.html
    app.ocean = app.loadImage('ocean.jpeg')
    app.ocean = app.scaleImage(app.ocean, 1.6)
    connectIslands(app.maze)
    app.turtleX = app.playerLocation[0] * app.cellWidth
    app.turtleY = app.playerLocation[1] * app.cellHeight
    app.r = (app.width+app.height)/100
    app.gameOver = False
    app.timerDone = False 
    app.timer = 0 
    app.internalTimer = 0
    # Turtle starts with three lives 
    app.lives = 3
    app.justHit = False
    app.startTime = -4
    app.sharkMaze = (list(solveMaze(app)))
    # To see which quadrant the turte is in 
    app.quadOne = False 
    app.quadTwo = False
    app.quadThree = False
    app.quadFour = False 
    app.quadrants = 4 
    # https://www.vecteezy.com/vector-art/3115975-under-the-sea-background-vector
    app.homeScreen = app.loadImage('homeScreenImage.png')
    app.homeScreenImage = app.scaleImage(app.homeScreen, 1/2)
    # https://www.shutterstock.com/search/turtle+cartoon
    app.endScreen = app.loadImage('endScreenTurtle.png')
    app.endScreenImage = app.scaleImage(app.endScreen, 1/2)
    # https://www.kindpng.com/imgv/ThJbTT_turtle-cartoon-png-transparent-png/
    app.tempTurtle = app.loadImage('happyTurtle.png')
    app.happyTurtle = app.scaleImage(app.tempTurtle, 1/2)
    # https://www.google.com/search?q=shark+square&tbm=isch&ved=2ahUKEwjTiM-0h7r0AhUpAp0JHbaiB_oQ2-cCegQIABAA&oq=shark+square&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAUQHjIGCAAQBRAeMgYIABAFEB4yBggAEAgQHjoHCCMQ7wMQJ1CPBViPBWDOB2gAcAB4AIABhAGIAdcBkgEDMS4xmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=vO-iYdO6FamE9PwPtsWe0A8&bih=709&biw=1440&rlz=1C5CHFA_enUS909US909#imgrc=JssdFXfvCoNHsM
    # Changes the size of the shark based on the level of the maze 
    app.sharkImage = app.loadImage('shark.png')
    if LEVEL == 10:
        app.finalSharkImage = app.scaleImage(app.sharkImage, 1/20)
    if LEVEL == 20:
        app.finalSharkImage = app.scaleImage(app.sharkImage, 1/22)
    if LEVEL == 30:
        app.finalSharkImage = app.scaleImage(app.sharkImage, 1/26)
    # https://www.freepik.com/premium-vector/cute-tropical-fish-blue-background-with-bubbles-brightly-coloured-ocean-fish-underwater-marine-wild-life-illustration_10088137.htm
    # Changes the size of the fish enemy based on the level of the maze 
    app.fishImage = app.loadImage('fish.png')
    if LEVEL == 10:
        app.finalFishImage = app.scaleImage(app.fishImage, 1/10)
    if LEVEL == 20:
        app.finalFishImage = app.scaleImage(app.fishImage, 1/12)
    if LEVEL == 30:
        app.finalFishImage = app.scaleImage(app.fishImage, 1/13)
    # https://feature.undp.org/plastic-tidal-wave/
    # changes the size of the plastic based on the level of the maze
    app.plastic1Image = app.loadImage('plastic1.png')
    if LEVEL == 10:
        app.finalPlastic1Image = app.scaleImage(app.plastic1Image, 1/20)
    if LEVEL == 20:
        app.finalPlastic1Image = app.scaleImage(app.plastic1Image, 1/24)
    if LEVEL == 30:
        app.finalPlastic1Image = app.scaleImage(app.plastic1Image, 1/26)
    # https://grist.org/climate/ocean-plastic-which-countries-are-responsible/
    app.plastic2Image = app.loadImage('plastic2.png')
    if LEVEL == 10:
        app.finalPlastic2Image = app.scaleImage(app.plastic2Image, 1/20)
    if LEVEL == 20:
        app.finalPlastic2Image = app.scaleImage(app.plastic2Image, 1/24)
    if LEVEL == 30:
        app.finalPlastic2Image = app.scaleImage(app.plastic2Image, 1/26)
    # https://www.istockphoto.com/illustrations/green-turtle
    # changes the size of the turtle based on the level of the maze 
    app.turtleImage = app.loadImage('turtle.png')
    app.tempTurtle = app.turtleImage.transpose(Image.FLIP_LEFT_RIGHT)
    if LEVEL == 10:
        app.finalTurtle = app.scaleImage(app.tempTurtle, 1/60)
    if LEVEL == 20:
        app.finalTurtle = app.scaleImage(app.tempTurtle, 1/80)
    if LEVEL == 30:
        app.finalTurtle = app.scaleImage(app.tempTurtle, 1/100)
    # the dimensions for the store screen 
    app.secRows = 4
    app.secCols = 3
    app.secMargin = 5
    app.secRow = -1
    app.secCol = -1 
    # https://www.istockphoto.com/search/2/image?mediatype=illustration&phrase=small+business+clipart
    app.storeImage = app.loadImage('store.png')
    app.finalStoreImage = app.scaleImage(app.storeImage, 1/2)
    app.totalPoints = 10 
    app.oneLifePoints = 2
    app.twoLifePoints = 4
    app.threeLifePoints = 6
    app.error = False
    app.homeScreen = True
    app.storeScreen = False
    app.startGame = False
    app.added = False
    app.bestPlayer = ''
    app.bestTime = 10**10
    app.chosen = False
    app.leader = False
    
class Island(object): pass

def keyPressed(app, event):
    row,col = app.playerLocation
    if event.key=="r":
        resetGame(app)
    if event.key == 'k':
        app.startGame = True
        app.homeScreen = False
        app.storeScreen = False
    elif event.key == 'h':
        app.homeScreen = True
        app.storeScreen = False
        app.startGame = False
        app.leader = False
    elif event.key == 'b':
        app.storeScreen = True
        app.homeScreen = False
        app.startGame = False
        app.error = False
        app.leader = False
    elif event.key == 'Space':
        with open("Leaderboard.txt", 'r+') as f:
            f.truncate(0)
    elif event.key=="s":
        if app.solution==None:
            app.solution = solveMaze(app)
        else:
            app.solution=None
    elif event.key == '+':
        app.rows += 1
        app.cols += 1
    elif event.key == '-':
        app.rows -= 1 
        app.cols -= 1 
    # the key pressed functions to move the turtle 
    elif event.key == "Up" and isValid(app, row,col,NORTH):
        doMove(app, row,col,NORTH)
        getCell(app, app.playerLocation[0], app.playerLocation[1])
    elif event.key == "Down" and isValid(app, row,col,SOUTH):
        doMove(app, row,col,SOUTH)
        getCell(app, app.playerLocation[0], app.playerLocation[1])
    elif event.key == "Left" and isValid(app, row,col,WEST):
        doMove(app, row,col,WEST)
        getCell(app, app.playerLocation[0], app.playerLocation[1])
    elif event.key == "Right" and isValid(app, row,col,EAST):
        doMove(app, row,col,EAST)
        getCell(app, app.playerLocation[0], app.playerLocation[1])

# everytime r is pressed game is reset with these original values 
def resetGame(app):
    rows,cols = len(app.maze),len(app.maze[0])
    app.solution = None
    app.path = set([(0,0)])
    app.playerLocation = (0,0)
    app.maze = makeMaze(rows,cols)
    app.timer = 0
    app.gameOver = False
    app.timerDone = False
    app.justHit = False
    app.startTime = -4
    app.quadOne = False
    app.quadTwo = False
    app.quadThree = False
    app.quadFour = False
    app.added = False
    connectIslands(app.maze)

# Maze Creation

# Makes the maze
def makeMaze(rows,cols):
    islands = [[0]*cols for row in range(rows)]
    counter = 0
    for row in range(rows):
        for col in range(cols):
            islands[row][col] = makeIsland(counter)
            counter+=1
    return islands

# https://www.cs.cmu.edu/~112/notes/notes-recursion-part2.html
def makeIsland(number):
    island = Island()
    island.east = False
    island.south = False
    island.number = number
    return island

# https://www.cs.cmu.edu/~112/notes/notes-recursion-part2.html
def connectIslands(islands):
    rows,cols = len(islands),len(islands[0])
    for i in range(rows*cols-1):
        makeBridge(islands)

def randomGenerator():
    return random.choice([True, False])

# https://www.cs.cmu.edu/~112/notes/notes-recursion-part2.html
# creates the bridges connection the different nodes of the maze
def makeBridge(islands):
    rows,cols = len(islands),len(islands[0])
    while True:
        row,col = random.randint(0,rows-1),random.randint(0,cols-1)
        start = islands[row][col]
        if randomGenerator(): 
            if col==cols-1: 
                continue
            target = islands[row][col+1]
            if start.number==target.number: 
                continue
            start.east = True
            renameIslands(start,target,islands)
        else: 
            if row==rows-1: 
                continue
            target = islands[row+1][col]
            if start.number==target.number: 
                continue
            start.south = True
            renameIslands(start,target,islands)
        return

# https://www.cs.cmu.edu/~112/notes/notes-recursion-part2.html
def renameIslands(i1,i2,islands):
    n1,n2 = i1.number,i2.number
    lo,hi = min(n1,n2),max(n1,n2)
    for row in islands:
        for island in row:
            if island.number==hi: 
                island.number=lo

# the helper function to solve the maze with DFS/backtracking
def solve(app, row, col, visitedNodes, targetedRow, targetedCol ):
    if row == targetedRow and col == targetedCol:
        return visitedNodes
    for direction in [(1,0),(-1,0),(0,1),(0,-1)]:
        drow, dcol = direction
        newRow = row+drow
        newCol = col+dcol
        if ((newRow, newCol) not in visitedNodes) and \
         (isValid(app, row, col, direction)):
            visitedNodes.add((newRow,newCol))
            solution = solve(app, newRow, newCol, visitedNodes, 
                                targetedRow, targetedCol)
            if solution != None:
                return solution
            visitedNodes.remove((newRow,newCol))
    return None

# function call to solve the maze (calls a helper)
def solveMaze(app):
    visitedNodes = set()
    visitedNodes.add((0, 0))
    targetedRow = len(app.maze) - 1
    targetedCol = len(app.maze[0]) - 1
    return solve(app, 0, 0, visitedNodes, targetedRow, targetedCol)

# https://www.cs.cmu.edu/~112/notes/notes-recursion-part2.html
# checks to see if a move is valid in the grid 
def isValid(app, row,col,direction):
    maze = app.maze
    rows,cols = len(maze),len(maze[0])
    if not (0<=row<rows and 0<=col<cols): 
        return False
    if direction==EAST: 
        return maze[row][col].east
    if direction==SOUTH: 
        return maze[row][col].south
    if direction==WEST: 
        return maze[row][col-1].east
    if direction==NORTH: 
        return maze[row-1][col].south

# if a certain move is valid move the turtle in that direction
def doMove(app, row,col,direction):
    (drow,dcol) = direction
    maze = app.maze
    path = app.path
    rows,cols = len(maze),len(maze[0])
    if not (0<=row<rows and 0<=col<cols): 
        return False
    if ((row+drow,col+dcol)) in path: 
        path.remove((row,col))
    else: 
        path.add((row+drow,col+dcol))
    app.playerLocation = (row+drow,col+dcol)

#https://www.cs.cmu.edu/~112/notes/notes-recursion-part2.html
def drawIslands(app, canvas):
    islands = app.maze
    rows,cols = len(islands),len(islands[0])
    color = 'pink'
    r = app.r
    for row in range(rows):
        for col in range(cols):
            app.playerXCoord = islandCenter(app,row,col)[0]
            app.playerYCoord = islandCenter(app,row,col)[1]
            drawCircle(app, canvas, app.playerXCoord, 
                        app.playerYCoord ,r,color)

def drawCircle(app, canvas, row, col, r, color):
    cx,cy = row,col
    canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill=color)
    canvas.create_image(cx, cy, image=ImageTk.PhotoImage(app.finalTurtle))

# https://www.cs.cmu.edu/~112/notes/notes-recursion-part2.html
# given a row and a col, finds the center of the circle that will be drawn there
def islandCenter(app, row, col):
    cellWidth,cellHeight = app.cellWidth,app.cellHeight
    return ((col+0.5)*cellWidth,(row+0.5)*cellHeight)

# https://www.cs.cmu.edu/~112/notes/notes-recursion-part2.html
# draws the lines of the maze 
def drawBridges(app,canvas):
    islands = app.maze
    rows,cols = len(islands),len(islands[0])
    color = 'light blue'
    width = min(app.cellWidth,app.cellHeight)/15
    for r in range(rows):
        for c in range(cols):
            island = islands[r][c]
            if (island.east):
                canvas.create_line(islandCenter(app, r,c),
                                   islandCenter(app, r,c+1),
                                   fill=color, width=width)
            if (island.south):
                canvas.create_line(islandCenter(app, r,c),
                                   islandCenter(app, r+1,c),
                                   fill=color, width=width)

# https://www.cs.cmu.edu/~112/notes/notes-recursion-part2.html
# takes the stored path of the player and draws it on the maze 
def drawPlayerPath(app, canvas):
    path = app.path
    (playerRow,playerCol) = app.playerLocation
    color = 'blue'
    r = min(app.cellWidth,app.cellHeight)/6
    width = min(app.cellWidth,app.cellHeight)/15
    for (row,col) in path:
        if (row+1,col) in path and isValid(app, row,col,SOUTH):
            canvas.create_line(islandCenter(app, row,col),
                                   islandCenter(app, row+1,col),
                                   fill=color, width=width)
        if (row,col+1) in path and isValid(app, row,col,EAST):
            canvas.create_line(islandCenter(app, row,col),
                                   islandCenter(app, row,col+1),
                                   fill=color, width=width)
    drawCircle(app, canvas, islandCenter(app, playerRow,playerCol)[0],
            islandCenter(app, playerRow,playerCol)[1],r,color)

# https://www.cs.cmu.edu/~112/notes/notes-recursion-part2.html
# whenever s is clicked, the path of the solution is drawn in green as a hint
def drawSolutionPath(app, canvas, path):
    color = 'green'
    r = min(app.cellWidth,app.cellHeight)/6
    width = min(app.cellWidth,app.cellHeight)/15
    for (row,col) in path:
        row,
        if (row+1,col) in path and isValid(app, row,col,SOUTH):
            canvas.create_line(islandCenter(app, row,col),
                                   islandCenter(app, row+1,col),
                                   fill=color, width=width)
        if (row,col+1) in path and isValid(app, row,col,EAST):
            canvas.create_line(islandCenter(app, row,col),
                                   islandCenter(app, row,col+1),
                                   fill=color, width=width)


# Store Creation 

# https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
def getStoreCell(app, x, y):
    gridWidth  = app.width - 2*app.secMargin
    gridHeight = app.height - 2*app.secMargin
    cellWidth  = gridWidth / app.secCols
    cellHeight = gridHeight / app.secRows
    row = int((y - app.secMargin) / cellHeight)
    col = int((x - app.secMargin) / cellWidth)
    return (row, col)

# https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
def getCellBounds(app, row, col):
        gridWidth  = app.width - 2*app.secMargin
        gridHeight = app.height - 2*app.secMargin
        cellWidth = gridWidth / app.secCols
        cellHeight = gridHeight / app.secRows
        x0 = app.secMargin + col * cellWidth
        x1 = app.secMargin + (col+1) * cellWidth
        y0 = app.secMargin + row * cellHeight
        y1 = app.secMargin + (row+1) * cellHeight
        return (x0, y0, x1, y1)

# draws the labels on the cells which indicate the lives that you can buy 
def drawCells(app, canvas):
    descriptionList = ["1 Life", "Cost: 2 Points", "2 Lives", "Cost: 4 Points", "3 Lives", "Cost: 6 Points"]
    index = 0 
    for row in range(app.secRows):
            for col in range(app.secCols):
                if row == 3:
                    (x0, y0, x1, y1) = getCellBounds(app, row, col)
                    canvas.create_text((x0+x1)/2, (y0+y1)/2, text=descriptionList[index], font = 'Times 15 bold', fill = 'blue')
                    canvas.create_text((x0+x1)/2, (y0+y1)/2 + 30, text=descriptionList[index + 1], font = 'Times 15 bold', fill = 'dark blue')
                    index += 2

# Creation of all the enemies

# gets the cell that the turtle is currently in and which quadrant it is in 
def getCell(app, x, y):
    halfWay = app.rows//app.quadrants
    if (0 <= x < halfWay) and (0 <= y <= halfWay):
        app.quadOne = True 
        app.quadTwo = False
        app.quadThree = False
        app.quadFour = False 
    if (halfWay <= x < app.cols) and (0 <= y < halfWay):
        app.quadOne = False 
        app.quadTwo = False
        app.quadThree = True
        app.quadFour = False 
    if (0 <= x < halfWay) and (halfWay <= y < app.rows):
        app.quadOne = False 
        app.quadTwo = True
        app.quadThree = False
        app.quadFour = False 
    if (halfWay <= x < app.cols) and (halfWay <= y < app.rows):
        app.quadOne = False 
        app.quadTwo = False
        app.quadThree = False
        app.quadFour = True 

# creation of the fish enemy object's maze that needs to be solved and it depends on the level of the maze
class Enemy(object):
	def __init__(self, size):
		self.length = size
		self.rows = LEVEL
		self.cols = LEVEL

	def makeNodes (self):
		lst = [str(i+1) for i in range(self.length)]
		return lst
	
	def makeAdjacency(self):
		newMatrix = [[random.randint(0,1) for i in range (self.rows)] for j in range(self.cols)]
		return newMatrix 

# creation of a graph that is random each time the game is run 
enemy = Enemy(LEVEL)
nodesNames = enemy.makeNodes()
alreadySeen = [0 for x in range(len(nodesNames))]
previous = [-1 for x in range(len(nodesNames))]
adjacencyMatrix = enemy.makeAdjacency()

# https://pencilprogrammer.com/algorithms/shortest-path-in-unweighted-graph-using-bfs/
# uses BFS to solve the randomly generated maze 
class BFS:
	def __init__(self, start, end):
		self.start = start
		self.end = end 

	def bfs(self):
		lst = []
		alreadySeen[self.start] = 1
		lst.append(self.start)
		while len(lst) > 0:
			curr = lst.pop(0)
			while self.unvisitedNeighbor(curr) != -1:
				neighbor = self.unvisitedNeighbor(curr)
				alreadySeen[neighbor] = 1
				lst.append(neighbor)
				previous[neighbor] = curr
				if neighbor == self.end:
					lst = []
					break
		finalList = []
		for num in self.trace():
			finalList.append(int(num))
		return(finalList)

	def unvisitedNeighbor(self, index):
		for i in range(len(nodesNames)):
			if adjacencyMatrix[index][i] == 1 and alreadySeen[i] == 0:
				return i
		return -1

	def trace(self):
		last = self.end
		route = []
		while last != -1:
			route.append(nodesNames[last])
			last = previous[last]
		route.reverse()
		return route

# returns the solution to the solved maze 
def createEnemyList():
	sp = BFS(0, LEVEL - 1)
	return (sp.bfs())

# a class that creates the display of the enemy using the BSF maze generation
class drawEnemy(object):
    def __init__(self, path):
        self.path = path
        self.finalPath = []
        if len(self.path) == 2:
            self.path += [self.path[1], self.path[0]]
        for i in range(len(self.path)):
            for j in range(i+1, len(self.path)):
                tempX = i 
                tempY = j
                row = self.path[tempX]
                col = self.path[tempY]
                self.finalPath.append((row,col))
        self.index = 0 
        self.x = 100
        self.y = 100
        self.coordsList = []
        self.time0 = time.time()
    
    # uses the island center function to get the coordinates for the enemy given the list of rows and cols it moves in 
    # the location is different depending on which quadrant the player is currently in 
    def getCoords(self, app):
        self.coordsList = []
        if app.quadOne == True:
            for node in self.finalPath:
                tempX = node[0]
                tempY = node[1]
                if (tempX >= app.cols//4):
                    tempX = int(tempX - app.cols//4)
                if (tempY >= app.rows//4):
                    tempY = int(tempY - app.rows//4)
                x = islandCenter(app, tempX, tempY)[0]
                y = islandCenter(app, tempX, tempY)[1]
                self.coordsList.append((x, y))
        if app.quadThree == True:
            for node in self.finalPath:
                tempX = node[0]
                tempY = node[1]
                if (tempX <= app.cols//4):
                    tempX = int(tempX + app.cols//4)
                if (tempY >= app.rows//4):
                    tempY = int(tempY - app.rows//4)
                x = islandCenter(app, tempX, tempY )[0]
                y = islandCenter(app, tempX, tempY )[1]
                self.coordsList.append((x, y))
        if app.quadTwo == True:
            for node in self.finalPath:
                tempX = node[0]
                tempY = node[1] 
                if (tempX >= app.cols//4):
                    tempX = int(tempX - app.cols//4)
                if (tempY <= app.rows//4):
                    tempY = int(tempY + app.rows//4)
                x = islandCenter(app, tempX, tempY)[0]
                y = islandCenter(app, tempX, tempY)[1]
                self.coordsList.append((x, y))
        if app.quadFour == True:
            for node in self.finalPath:
                tempX = node[0] 
                tempY = node[1] 
                if (tempX <= app.cols//4):
                    tempX = int(tempX + app.cols//4)
                if (tempY <= app.rows//4):
                    tempY = int(tempY + app.rows//4)
                x = islandCenter(app, tempX, tempY )[0]
                y = islandCenter(app, tempX , tempY)[1]
                self.coordsList.append((x, y))
        return self.coordsList

    # the enemy moves each time the timer is fired but there is a timer delay 
    def timerFired (self, app):
        self.coordsList = self.getCoords(app)
        time1 = time.time()
        if app.quadOne == True:
            if (time1 - self.time0) > 0.5:
                if self.index == len(self.coordsList):
                    self.index = 0
                self.x = self.coordsList[self.index][0]
                self.y = self.coordsList[self.index][1]
                self.index += 1 
                self.time0 = time.time()
        if app.quadTwo == True:
            if (time1 - self.time0) > 0.5:
                if self.index == len(self.coordsList):
                    self.index = 0
                self.x = self.coordsList[self.index][0]
                self.y = self.coordsList[self.index][1]
                self.index += 1 
                self.time0 = time.time()    
        if app.quadThree == True:
            if (time1 - self.time0) > 0.5:
                if self.index == len(self.coordsList):
                    self.index = 0 
                self.x = self.coordsList[self.index][0]
                self.y = self.coordsList[self.index][1]
                self.index += 1 
                self.time0 = time.time()
        if app.quadFour == True:
            if (time1 - self.time0) > 0.5:
                if self.index == len(self.coordsList):
                    self.index = 0 
                self.x = self.coordsList[self.index][0]
                self.y = self.coordsList[self.index][1]
                self.index += 1 
                self.time0 = time.time()
            
    def draw(self, app, canvas):
        if app.gameOver == False:
            self.r = (app.width+app.height)/100
            canvas.create_oval(self.x- self.r, self.y - self.r, 
                                self.x + self.r, self.y + self.r, fill = 'pink')
            canvas.create_image(self.x, self.y, image=ImageTk.PhotoImage(app.finalFishImage))

# the enemy creation using the class
enemy1 = drawEnemy(createEnemyList())

# the creation of a plastic class 
class Plastic(object):
    def __init__(self, speed, x, y):
        self.speed = speed
        self.x = x
        self.y = y
    
    def drawPlastic(self, app, canvas):
        if app.gameOver == False:
            self.r = app.r
            canvas.create_oval(self.x - self.r, self.y - self.r, 
                                self.x + self.r, self.y + self.r, fill = 'red')
            plasticImages = [app.finalPlastic1Image, app.finalPlastic2Image]
            ranNum = random.randrange(0,1)
            canvas.create_image(self.x, self.y, image=ImageTk.PhotoImage(plasticImages[ranNum]))

    def timerFiredLeft(self, app):
        self.x -= self.speed
        if (self.x + self.r)  <= 0:
            self.x = app.width + self.r
    
    def timerFiredRight(self, app):
        self.x += self.speed
        if(self.x + self.r) >= app.width:
            self.x = self.r
    
    def timerFiredUp(self, app):
        self.y -= self.speed 
        if (self.y + self.r) <= 0:
            self.y = app.height+self.r
    
    def timerFiredDown(self,app):
        self.y += self.speed
        if (self.y + self.r) >= app.height:
            self.y = self.r

    def timerFiredDiagonal(self, app):
        self.x += self.speed
        self.y += self.speed
        if ((self.x + self.r) >= app.width)and((self.y + self.r) >= app.height):
            self.x = self.r
            self.y = self.r

def randomNum(num):
    return (random.randrange(1, num))

def randomXYNum():
    return (random.randrange(100,500))

# creates a different number of plastic based on the level of hardness the player chooses 
# the starting location and speed of the plastic is also different everywhere 
if LEVEL == 10:
    plastic1 = Plastic(randomNum(10), randomXYNum(), randomXYNum())
    plastic2 = Plastic(randomNum(10), randomXYNum(), randomXYNum())
elif LEVEL == 20:
    plastic1 = Plastic(randomNum(10), randomXYNum(), randomXYNum())
    plastic2 = Plastic(randomNum(10), randomXYNum(), randomXYNum())
    plastic3 = Plastic(randomNum(10), randomXYNum(), randomXYNum())
elif LEVEL == 30:
    plastic1 = Plastic(randomNum(10), randomXYNum(), randomXYNum())
    plastic2 = Plastic(randomNum(10), randomXYNum(), randomXYNum())
    plastic3 = Plastic(randomNum(10), randomXYNum(), randomXYNum())
    plastic4 = Plastic(randomNum(10), randomXYNum(), randomXYNum())
    plastic5 = Plastic(randomNum(10), randomXYNum(), randomXYNum())

# the shark enemy moves along the solution path 
def getSharkCoords(app):
    coordsList = []
    for pairs in app.sharkMaze:
        row = pairs[0]
        col = pairs[1]
        xCoord = islandCenter(app, row, col)[0]
        yCoord = islandCenter(app, row, col)[1]
        coordsList.append((xCoord, yCoord))
    return coordsList

# creation of a shark class 
class Shark(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.path = []
        self.index = 0
        self.time0 = time.time()

    def drawShark (self, app, canvas):
        if app.gameOver == False:
            self.r = app.r
            canvas.create_oval(self.x- self.r, self.y - self.r, 
                            self.x + self.r, self.y + self.r, fill = 'purple')
            canvas.create_image(self.x, self.y, image=ImageTk.PhotoImage(app.finalSharkImage))

    # the speed of the shark changes depending on the level of the game
    def levelTime(self):
        if LEVEL == 10:
            seconds = 1
        if LEVEL == 20:
            seconds = 0.5
        if LEVEL == 30:
            seconds = 0.25
        return seconds

    def timerFired (self, app):
        time1 = time.time()
        if time1 - self.time0 > self.levelTime():
            self.index += 1
            if self.index == len(self.path):
                self.index = 0
            self.path = getSharkCoords(app)
            self.x = self.path[self.index][0]
            self.y = self.path[self.index][1]
            self.time0 = time.time()

shark1 = Shark(randomXYNum(), randomXYNum())

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def intersectCircles(x1, y1, x2, y2, r1, r2):
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    radiusSum = (r1 + r2)
    if distance <= (radiusSum):
        return True
    return False

# checks if the player interescts any of the enemies and decreases lives depending on which enemy is hit
def collision(app):
    row = app.playerLocation[0]
    col = app.playerLocation[1]
    app.playerXCoord = islandCenter(app,row,col)[0]
    app.playerYCoord = islandCenter(app,row,col)[1]
    turtleX = int(app.playerXCoord)
    turtleY = int(app.playerYCoord)
    if app.startGame == True and app.gameOver == False:
        if LEVEL == 10:
            if intersectCircles(turtleX, turtleY, plastic1.x, plastic1.y, app.r, plastic1.r):
                app.justHit = True
                app.lives -=1 
                app.startTime = time.time()
                return True
            if intersectCircles(turtleX, turtleY, plastic2.x, plastic2.y, app.r, plastic2.r):
                app.justHit = True
                app.lives -=1 
                app.startTime = time.time()
                return True
        if LEVEL == 20:
            if intersectCircles(turtleX, turtleY, plastic1.x, plastic1.y, app.r, plastic1.r):
                app.justHit = True
                app.lives -=1 
                app.startTime = time.time()
                return True
            if intersectCircles(turtleX, turtleY, plastic2.x, plastic2.y, app.r, plastic2.r):
                app.justHit = True
                app.lives -=1 
                app.startTime = time.time()
                return True
            if intersectCircles(turtleX, turtleY, plastic3.x, plastic3.y, app.r, plastic3.r):
                app.justHit = True
                app.lives -=1 
                app.startTime = time.time()
                return True
        if LEVEL == 30:
            if intersectCircles(turtleX, turtleY, plastic1.x, plastic1.y, app.r, plastic1.r):
                app.justHit = True
                app.lives -=1 
                app.startTime = time.time()
                return True
            if intersectCircles(turtleX, turtleY, plastic2.x, plastic2.y, app.r, plastic2.r):
                app.justHit = True
                app.lives -=1 
                app.startTime = time.time()
                return True
            if intersectCircles(turtleX, turtleY, plastic3.x, plastic3.y, app.r, plastic3.r):
                app.justHit = True
                app.lives -=1 
                app.startTime = time.time()
            if intersectCircles(turtleX, turtleY, plastic4.x, plastic4.y, app.r, plastic4.r):
                app.justHit = True
                app.lives -=1 
                app.startTime = time.time()
                return True
            if intersectCircles(turtleX, turtleY, plastic5.x, plastic5.y, app.r, plastic5.r):
                app.justHit = True
                app.lives -=1 
                app.startTime = time.time()
                return True
        if intersectCircles(turtleX, turtleY, shark1.x, shark1.y, app.r, shark1.r):
            app.justHit = True
            app.lives -= 2
            app.startTime = time.time()
            return True
        if intersectCircles(turtleX, turtleY, enemy1.x, enemy1.y, app.r, enemy1.r):
            app.justHit = True
            app.lives -= 1
            app.startTime = time.time()
            return True
        
def timerFired (app):
    if app.lives <= 0:
        app.gameOver = True
    if time.time() - app.startTime >2:
        app.justHit = False
        if app.justHit == False:
            collision(app)
    if (app.timerDone == False):
        app.internalTimer += app.timerDelay 
        if app.gameOver == False and app.startGame == True:
            if app.internalTimer >= 1000:
                app.internalTimer = 0 
                app.timer += 1
    if (app.playerLocation == app.finalLocation):
        app.gameOver = True 
        app.timerDone = True
        addScore(app)
    if app.gameOver == True and app.lives > 0:
        app.leader = True
        leaderboard(app)

def getPlayerScore(app):
    if app.chosen == False:
        leaderboard(app)
        app.chosen = True
        app.leader = True

def addScore(app):
    if app.added == False:
        app.totalPoints += app.lives
        app.added = True

def drawTimer(app, canvas):
    if app.gameOver == False and app.startGame == True:
        canvas.create_text(app.width/2, 580, 
                            text=f'Seconds Elapsed: {app.timer}', fill = 'black', font = 'Times 20 bold')
    else:
        canvas.create_rectangle(0,0,app.width, app.height, fill = 'white')
        canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.endScreenImage))
        canvas.create_text(app.width/2, app.height/6 - 50, 
                            text = "Game Over", fill = 'black', font=f'Times 50 bold italic' )
        canvas.create_text(app.width/2, app.height/6, 
                            text = f'Final Time: {app.timer} seconds', fill = 'black', font = f'Times 20 bold')
        if app.leader == True:
            canvas.create_text(app.width/2, app.height/2 + 150, text = f'Current Best Player: {app.bestPlayer} and Current Best Time: {app.bestTime}', font = 'Times 20 bold')
        if app.lives < 0:
            livesRemaining = 0 
        else:
            livesRemaining = app.lives
        canvas.create_text(app.width/2, app.height/6 + 38, text =  f'Lives Remaining: {livesRemaining}', fill = 'black', font = f'Times 20 bold')
        if app.lives > 0:
            canvas.create_text(app.width/2, app.height/2 + 200, text = f'You earned {app.lives} points for making it home with {app.lives} lives remaining', font = 'Times 15')
        canvas.create_text(app.width/2, app.height/2 + 250, text = f'You have a total of {app.totalPoints} points you can use to buy additional lives', font = 'Times 15')

def drawLives(app, canvas):
    if app.gameOver == False:
        canvas.create_text(app.width/2, 15, text = f'Lives Remaining: {app.lives}', fill = 'black', font = 'Times 20 bold')

def drawGameOverScreen(app, canvas):
    canvas.create_rectangle(0,0,app.width, app.height, fill = 'dark blue')
    canvas.create_text(app.width/2, app.height/2, text = 'Game Over')

# draws the home screen whenever h is pressed
def homeScreen_redrawAll(app, canvas):
    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.homeScreenImage))
    canvas.create_text(app.width/2, 85, text="A TURTLE'S WAY HOME", font=f'Times 26 bold italic', fill='white')
    canvas.create_text(app.width/2, 125, text = f'Welcome Player {USERNAME}', font = f'Times 20 bold', fill = 'white')
    canvas.create_line(0, 150, app.width, 150, fill="white", width=5)
    canvas.create_text( app.width/2, 180, text= 'Game Rules', font = f'Times 20 bold', fill = 'white')
    messages = [ "Solve the maze while avoiding all the enemies and maintaining all 3 of your lives", 
                "If you hit a shark, you lose two lives", 
                "If you hit plastic or a fish, you lose one life",
                "Press k to start the game", 
                "Use the arrows to control your turtle", 
                "Press s to get a hint on how to solve the maze", 
                "Press h to return to the home screen", 
                "Press r to restart and get a new maze", 
                "Press b to go to the store and buy more lives",
                "Press Space to clear the leaderboard"]
    counter = 0
    for message in messages:
        canvas.create_text(app.width/2, 220 +25*counter, text = message, font = 'Times 16', fill = 'white')
        counter += 1
    canvas.create_line(0, 470, app.width, 470, fill="white", width=5)
    canvas.create_text(app.width/2, 530, text = f'Time to start playing the game at level {LEVEL//10}', font = 'Times 25 bold', fill = 'white')

def storeScreen_redrawAll(app, canvas):
    drawCells(app, canvas)
    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.finalStoreImage))
    canvas.create_text(app.width/2, app.height/2 - 200, text = f'Points: {app.totalPoints}', font = 'Times 25 bold', fill = 'dark blue')
    canvas.create_text(app.width/2, app.height/2 -150, text = f'Current Lives: {app.lives}', font = 'Times 25 bold', fill = 'blue')
    if app.error: 
        canvas.create_text(app.width/2, app.height - 150, text = 'Need more points', font = 'Times 20 bold', fill = 'dark green')

def storeScreen_mousePressed(app, event):    
    (app.secRow, app.secCol) = getStoreCell(app, event.x, event.y)
    app.error = False
    if app.secRow == 3:
        if app.secCol == 0:
            if app.totalPoints >= app.oneLifePoints:
                app.lives += 1 
                app.totalPoints -= app.oneLifePoints
            else:
                app.error = True
        if app.secCol == 1:
            if app.totalPoints >= app.twoLifePoints:
                app.lives += 2 
                app.totalPoints -= app.twoLifePoints
            else:
                app.error = True
        if app.secCol == 2:
            if app.totalPoints >= app.threeLifePoints:
                app.lives += 3 
                app.totalPoints -= app.threeLifePoints
            else:
                app.error = True

def  mousePressed(app, event):
    if app.storeScreen == True:
        storeScreen_mousePressed(app, event)

# stores the username and the time to finish the maze in a text file and finds the best time and the user name
def leaderboard(app):
    if app.gameOver == True:
        file = open("Leaderboard.txt", 'a')
        file.write((USERNAME) + ' ' + str(app.timer) + '\n')
        file.close()
        # https://python-forum.io/thread-31687.html 
        file = open("Leaderboard.txt", 'r')
        readthefile = file.readlines()
        sortedData = sorted(readthefile)
    
        for line in range(len(sortedData)):
            values = (sortedData[line]).split()
            player = values[0]
            playerTime = int(values[1])
            if playerTime <= app.bestTime:
                app.bestTime = playerTime
                app.bestPlayer = player

def redrawAll(app, canvas):
    if app.homeScreen == True:
        homeScreen_redrawAll(app, canvas)
    if app.storeScreen == True:
        storeScreen_redrawAll(app, canvas)
    if app.startGame:
        canvas.create_image(app.width/2, app.height/2, 
                            image=ImageTk.PhotoImage(app.ocean))
        drawBridges(app, canvas)
        if app.solution!= None: 
            drawSolutionPath(app, canvas, app.solution)
        drawPlayerPath(app, canvas)
        drawTimer(app, canvas)
        drawLives(app,canvas)
        if LEVEL == 10:
            plastic1.drawPlastic(app, canvas)
            plastic2.drawPlastic(app, canvas)
            plastic1.timerFiredLeft(app)
            plastic2.timerFiredDiagonal(app)
        elif LEVEL == 20:
            plastic1.drawPlastic(app, canvas)
            plastic2.drawPlastic(app, canvas)
            plastic3.drawPlastic(app, canvas)    
            plastic1.timerFiredLeft(app)
            plastic2.timerFiredRight(app)
            plastic3.timerFiredUp(app)
        elif LEVEL == 30:
            plastic1.drawPlastic(app, canvas)
            plastic2.drawPlastic(app, canvas)
            plastic3.drawPlastic(app, canvas)
            plastic4.drawPlastic(app, canvas)
            plastic5.drawPlastic(app, canvas) 
            plastic1.timerFiredLeft(app)
            plastic2.timerFiredRight(app)
            plastic3.timerFiredUp(app)
            plastic4.timerFiredDown(app)
            plastic5.timerFiredDiagonal(app)   
        shark1.drawShark(app, canvas)
        shark1.timerFired(app)
        enemy1.draw(app, canvas)
        enemy1.timerFired(app)
    
runApp(width=600, height=600)