from os import read

#CLASE PARA LEER Y DEFINIR LOS COMPONENTES QUE CONFORMAN AL OBJETO EN LA ESCENA


class Object() :
    def __init__(self, filename) :
        
        
        self.filename = filename
        self.vertices =[]
        self.faces = []
        self.normals = []
        self.texcoords = []
        
        with open(filename, "r") as file:
            self.lines= file.read().splitlines()
        self.readFile()
        # self.printMe()
        
        
    def printMe(self):
        print("Mis vertices son :\n" + str(self.vertices))
        print("Mis caras son son :\n" + str(self.faces))
        print("Mis normales son :\n" + str(self.normals))
        print("Mis textcoord son :\n" + str(self.texcoords))
        
        
        
        
        
        
    def readFile(self):
        for line in self.lines:
            if line:
                    #divide cada linea en prefijo y contenido
                try:
                        prefix, value = line.split(' ', 1)
                except:
                    continue
                    #clasifica segun prefijos
                    #Vertices
                if prefix == 'v':
                    self.vertices.append(list(map(float, value.split(' '))))
                    #texcoor
                elif prefix == 'vt': 
                    self.texcoords.append(list(map(float, value.split(' '))))
                    #vertex normals
                elif prefix == 'vn': 
                    self.normals.append(list(map(float, value.split(' '))))
                    #faces
                elif prefix == 'f': 
                    self.faces.append( [ list(map(int, vert.split('/'))) for vert in value.split(' ')] )

