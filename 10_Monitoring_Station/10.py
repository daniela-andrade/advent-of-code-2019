import math
from fractions import Fraction

def getPointOrder(x, endX, stepX, y, endY, stepY, matrix):
  points = []
  for j in range(x, endX, stepX):
    for i in range(y, endY, stepY):
      if j>=0 and j<len(matrix) and i>=0 and i<len(matrix[0]) and matrix[j][i]=='#' and (j,i) not in points:
        points.append((j,i))

    for x_ in range(j+stepX, endX, stepX):
      if x_>=0 and x_<len(matrix[0]) and y>=0 and y<len(matrix) and matrix[x_][y]=='#' and (x_,y) not in points: 
        points.append((x_,y))
    y = y + stepY
    x = x + stepX
  return points

def getImediateRow(start, end, step, col):
  for row in range (start,end, step):
    if matrix[row][col] == '#':
      return 1
  return 0

def getImediateCol(start, end, step, row):
  for col in range (start, end, step):
    if matrix[row][col] == '#':
      return 1
  return 0

def isHidden(stationX, stationY, x, y, asteroids):
  isHidden = False
  for asteroid in asteroids:
    if asteroid[0] == x and asteroid[1] == y:
      continue
    if (asteroid[0] - stationX == 0):
      if stationX == x:
        isHidden = x < asteroid[0] if asteroid[0] > stationX else x < asteroid[0]
      else:
        isHidden = False
    else:
      m = Fraction(asteroid[1]-stationY,asteroid[0]-stationX)
      b = Fraction(stationY - m*stationX)
      stationYprime = Fraction(m*x + b)
      if y == stationYprime:
        isHidden = (stationYprime > asteroid[1]) if (asteroid[1] > stationY) else (stationYprime < asteroid[1])
    if isHidden:
      return True
  return isHidden

def getQuadrantCount(points, matrix, stationX, stationY):
  asteroids = []
  for point in points:
    x = point[0]
    y = point[1]
    if matrix[x][y] == '#':
      if len(asteroids) == 0 or not isHidden(stationX, stationY, x, y, asteroids):
        asteroids.append((x,y))
  return(asteroids)

def getCount(stationX, stationY, matrix):
  maxX = len(matrix)
  maxY = len(matrix[0])

  upperLeft = getPointOrder(x=stationX-1, endX=-1, stepX=-1, y=stationY-1, endY=-1, stepY=-1, matrix=matrix)
  upperLeft = getQuadrantCount(upperLeft, matrix, stationX, stationY)

  upperRight = getPointOrder(x=stationX-1, endX=-1, stepX=-1, y=stationY+1, endY=maxY, stepY=1, matrix=matrix)
  upperRight = getQuadrantCount(upperRight, matrix, stationX, stationY)

  bottomLeft = getPointOrder(x=stationX+1, endX=maxX, stepX=1, y=stationY-1, endY=-1, stepY=-1, matrix=matrix)
  bottomLeft = getQuadrantCount(bottomLeft, matrix, stationX, stationY)
  
  bottomRight = getPointOrder(x=stationX+1, endX=maxX, stepX=1, y=stationY+1, endY=maxY, stepY=1, matrix=matrix)
  bottomRight = getQuadrantCount(bottomRight, matrix, stationX, stationY)

  up = getImediateRow(stationX-1, -1, -1, stationY)
  right = getImediateCol(stationY+1, maxY, 1, stationX)
  bottom = getImediateRow(stationX+1, maxX, 1, stationY)
  left = getImediateCol(stationY-1,-1,-1, stationX)

  inline = up + right + bottom + left
  quadrants = len(upperLeft) + len(upperRight) + len(bottomLeft + bottomRight

  return inline + quadrants

def getMaxCount(matrix):
  maxCount = 0
  stationX = -1
  stationY = -1
  
  for row in range(0,len(matrix)):
    for col in range(0,len(matrix[0])):
      if matrix[row][col] == '#':
        count = getCount(row, col, matrix)
        print('(%d,%d) can see %d asteroids'%(row,col,count))
        if count > maxCount:
          maxCount = count
          stationX = row
          stationY = col
  return maxCount, (stationX, stationY)

matrix = []
with open('input.txt', 'r') as f:
  rows = f.readlines()
  for row in rows:
    matrix.append([c for c in row.rstrip()])

print(getMaxCount(matrix))

points