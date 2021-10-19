import math

area_per_pint =400/8

while(True):
    radius = float(input("Enter radius of cylinder :"))
    height = float(input("Enter height of cylinder :"))
    cost_per_pint = float(input("Enter cost per pint of coating :"))

    if(radius < 0 or height < 0 or cost_per_pint < 0):
        print("invalid Input")
        continue

    area = (2 * math.pi * radius)*(height + radius)

    total_pints = math.ceil(area/area_per_pint)

    total_cost = total_pints * cost_per_pint

    print("Total Cost :$", round(total_cost,2))
    print("Total Pints :", total_pints)

    another_calc = input("Want to do another calculation (Y/N): ")

    if another_calc.upper() == 'Y':
        continue
    else:
        break
