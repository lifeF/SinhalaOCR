""" 
Author : Kalana Dhanajaya Rathnayake 
Date : 2019 01 14
Git : lifeF@github.com

Intro
======
identify connected component in image

"""
import png

class component :
    def __init__(self,image):
        self.get(image)
        self.component = {}

    def get(self ,image):
        V =[0]
        selected = []
        component_id = 0
        component_size = {}
        component = {}
        rows = len(image)
        cols = len(image[0])
        for y in range(rows):
            for x in range(cols):
                if( [x,y] not in selected):
                    if(image[y,x] in V):
                        component_size[component_id] = []
                        component[component_id] = []
                        stack =[] 
                        stack.append([x,y])
                        max_x = 0
                        max_y = 0

                        min_x = cols
                        min_y = rows
                        
                        while(len(stack) != 0):
                            point = stack.pop()
                            selected.append(point)
                            component[component_id].append(point) 
                            x = point[0]
                            y = point[1]
                            # setup max , min point
                            min_x = min(min_x,x)
                            min_y = min(min_y,y) 
                            max_x = max(max_x,x)
                            max_y = max(max_y,y)
                            
                            x1 = x
                            if( x -1 >=0):
                                x1 = x-1
                            x2 = x
                            if( x +1 < cols):
                                x2 = x+1
                            
                            y1 = y
                            if( y -1 >=0):
                                y1 = y-1

                            y2 = y
                            if( y +1 < rows):
                                y2 = y+1
                            
                            for i in range(x1,x2+1):
                                for j in range(y1,y2+1):
                                    if([i,j] not in selected):
                                        if(image[j,i] in V):
                                            stack.append([i,j])
                                            selected.append([i,j])

                                            
                                            
                        A = component[component_id]
                        
                        w,h = max_x-min_x+1,max_y-min_y+1
                        Matrix = [[255 for x in range(w)] for y in range(h)] 
                        min_point =[min_x,min_y] 
                        for i in range(len(A)):
                            point = A[i]
                            c_x,c_y = [a_i - b_i for a_i, b_i in zip(point, min_point)]
                            Matrix[c_y][c_x] = 0
                        component[component_id] = Matrix
                        png.from_array(Matrix, 'L').save('characters/c_'+str(component_id)+'.png')
                        component_id += 1
                        
        