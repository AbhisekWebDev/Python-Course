import math

def paint_calculator(wall_height, wall_width, paint_can_coverage):
    area = wall_height * wall_width
    no_of_cans = area / paint_can_coverage
    print(f"You need {math.ceil(no_of_cans)} number of cans")

height = int(input("Enter height of the wall in meters : "))
width = int(input("Enter width of the wall in meters : "))

coverage = 7 # 1 can of paint covers 7 sq. mtr. 

paint_calculator(wall_height = height, wall_width = width, paint_can_coverage = coverage)