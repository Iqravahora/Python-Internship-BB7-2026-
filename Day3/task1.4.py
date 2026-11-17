matrix = [
         
         [1,2,3],
         [4,5,6],
         [7,8,9]]

print("original matrix:")
print(matrix)

transpose = [[row[i] for row in matrix] for i in range (3)]
print("transported matrix:")
print(transpose)

         
         