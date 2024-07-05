row1 = ['❌', '❌', '❌']
row2 = ['❌', '❌', '❌']
row3 = ['❌', '❌', '❌'] 

matrix = [row1, row2, row3]

print(f" {row1} \n {row2} \n {row3}")

pos = input("Enter position where you want to hide money : ")

row_num = int(pos[0])
col_num = int(pos[1])

selected_row = matrix[row_num - 1]

selected_row[col_num - 1] = '⭕️'

print(f" {row1} \n {row2} \n {row3}")
