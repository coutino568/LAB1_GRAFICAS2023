
#para multiplicaciones de dos matrices
def matrixMultiplication(matrix1, matrix2):
    print(matrix1)
    print(matrix2)
    result =  [[0 for x in range(len(matrix1))] for y in range(len(matrix2[0]))]
    
    if(len(matrix1[0])== len(matrix2)):
        #print("Tamaño valido")
        
        for i in range(0, len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
                # local=0
                # value1= matrix1[j][j] * matrix2[j][i]
                # value2= matrix1[][j] * matrix2[j][i]
                # value3= matrix1[j][j]*matrix2[j][i]
                # result = value1+value2+value3
        print(result)
                
        
    
    else:
        print("Tamaño Invalido")
    



#para operacion de un vectori y una matriz
def matrixVectorMultiplication (matrix, vector):
    
    result =[[0 for i in range (len(matrix))] for j in range (len(matrix[0]))]
    print(result)
    if(len(vector)==len(matrix[0])):
        #print("Tamaño valido")
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result[i][j] = matrix[i][j]*vector[j]
                
                
                
        print(result)        
    else:
        print("Tamaño invlaido")


matrix1= [[5,2,4],[2,1,1],[1,2,3]]
matrix2 = [[1,0,2],[4,3,1],[2,0,3]]

matrix3= [[12,7],[4 ,0]]
matrix4= [[5,2],[6,0]]

vector1 = [100,0,0.00001]

# resultadoMatrices= matrixMultiplication(matrix1,matrix2)
#resultado esperado: [102,24 ] [20,8]
resultadoMatrices= matrixMultiplication(matrix3,matrix4)

#resultado esperado
resultadoMatrices= matrixVectorMultiplication(matrix1,vector1)