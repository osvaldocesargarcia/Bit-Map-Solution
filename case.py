class Case:

    n=-1
    m=-1
    matrix = [[]]
    # Constructor
    def __init__(self,n,m,matrix):
        self.n = n
        self.m = m
        self.matrix = matrix

    # Método que calcula la distancia entre bits en el mapa
    def bits_distance(self,i1,i2,j1,j2):

        dist_i = i1 - i2
        dist_j = j1 - j2

        if dist_i<0:
            dist_i = dist_i*(-1)
        if dist_j<0:
            dist_j = dist_j*(-1)

        return dist_i+dist_j



    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # Método que devuelve valor de la distancia más pequeña a un bit "blanco"
    def min_distance(self,i,j):

        value_i = 0
        min_value = 9999

        for row in self.matrix:

            value_j = 0
            for column in row:

                if column == 1 :
                    temp_distance = self.bits_distance(i, value_i, j, value_j)
                    if temp_distance<min_value:
                        min_value = temp_distance

                value_j += 1
            value_i += 1

        return  min_value

    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # Método que devuelve la matriz salida ("Output")
    def output(self):
        output_matrix = []
        count_i = 0

        for row in self.matrix:
            output_row = []
            count_j = 0

            for column in row:
                output_row.append(self.min_distance(count_i, count_j))
                count_j += 1

            count_i += 1
            output_matrix.append(output_row)

        return output_matrix

