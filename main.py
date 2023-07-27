
import random
from gl import Renderer
import math
from obj import *
from mathcou import *
from shader import *
from collections import namedtuple

objetos =[]


V2 = namedtuple('Point2', ['x', 'y'])

poligono1= [[165, 380] ,[185, 360], [180, 330] ,[207, 345], [233, 330], [230, 360], [250, 380], [220, 385] ,[205, 410] ,[193, 383]]
poligono2 = [[321, 335], [288, 286] ,[339, 251] ,[374, 302]]
poligono3= [[377, 249] ,[411, 197], [436, 249]]
poligono4 = [[413, 177] ,[448, 159] ,[502, 88] ,[553, 53] ,[535, 36] ,[676, 37] ,[660, 52],[750, 145], [761, 179] ,[672, 192] ,[659, 214] ,[615, 214], [632, 230], [580, 230],[597, 215], [552, 214] ,[517, 144] ,[466, 180]]
poligono5 = [[682, 175] ,[708, 120] ,[735, 148] ,[739, 170]]




windoWidth = 1920*1
windowHeight = 1080*1
scale= 1
viewportWidth= windoWidth*scale
viewportHeight= windowHeight *scale
viewportX=0
viewportY=0

M = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
Angulox=0
Anguloy=0
Anguloz=0

myRenderer = Renderer(windoWidth, windowHeight)
myRenderer.glViewPort(viewportX,viewportY,viewportWidth,viewportHeight)



# vertex1 = V2(50,50)
# vertex2 = V2(305,750)
# vertex3 = V2(650,800)
 

# # myRenderer.glTriangle(750,50,700,100,900,200)
# # myRenderer.glTriangle(750,10,00,00,500,200)
# myRenderer.glTriangle(vertex1[0],vertex1[1],360,100,90,500)
# myRenderer.glTriangle2(vertex1,vertex2,vertex3)



# matrix1= [[1,2,3],[2,6,9],[5,0,4]]
# matrix2 = [[3,6,1],[8,0,7],[1,0,42]]


# resultadoMatrices= matrixVectorMultiplication(matrix1,matrix2)
# objetito = Object("object.obj")

# objetos.append(objetito)


def transformarVertices():
    for objeto in objetos:
        for vert in objeto.vertices:
            print(vert)
            vert= vertexShader(vert)
            print(vert)
    



def renderizar():
    ## dibujara los objetos en el origen por el momento pero hay que hacer el pipeline de transformaciones.
    for objeto in objetos:
        for face in objeto.faces:
            # print("HARE UN TRIANGULO CON ESTOS VERTICES :"+ str(face))
            vert1= objeto.vertices[face[0][0]-1]
            vert2= objeto.vertices[face[1][0]-1]
            vert3= objeto.vertices[face[2][0]-1]
            print(vert1)
            print(vert2)
            print(vert3)
            myRenderer.glTriangle2(vert1,vert2,vert3)

# transformarVertices()
# renderizar()

#poligono1
faces1=[[0,1,9],[1,2,3],[3,4,5],[5,6,7],[7,8,9],[1,7,9],[1,5,7],[1,3,5]]
myRenderer.polygonGeneral(poligono1,faces1)

#poligono2
faces2=[[0,1,2],[1,2,3],[2,3,0]]
myRenderer.polygonGeneral(poligono2,faces2)

#poligono3

faces3=[[0,1,2]]
myRenderer.polygonGeneral(poligono3,faces3)

#poligono

print(len(poligono4))
faces4=[[0,1,17],[1,17,16],[1,2,16],[2,3,16],[3,4,5],[3,5,6],[3,6,16],[6,7,16],[7,8,9],[7,9,16],[9,10,11],[9,11,16],[11,12,13],[11,13,14],[14,15,16],[11,14,16]]
myRenderer.polygonGeneral(poligono4,faces4)


#poligono5
print(len(poligono5))
faces5=[[1,2,0],[0,2,3]]
myRenderer.glColor(1,1,1)
myRenderer.polygonGeneral(poligono5,faces5)




#poligono trasladado
myRenderer.glColor(0,0,0)
movex=350
movey=350
poligono6= poligono4
for poli in poligono6:
    poli[0]+=movex
    poli[1]+=movey
    
    
poligono7= poligono5
for poli in poligono7:
    poli[0]+=movex
    poli[1]+=movey   

faces6=faces4
faces7 =faces5

myRenderer.polygonGeneral(poligono6,faces6)
myRenderer.glColor(1,1,1)
myRenderer.polygonGeneral(poligono7,faces7)



myRenderer.glFinish("output.bmp")