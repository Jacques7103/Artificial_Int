#Python Code
def r_triangle(angle1, angle2, angle3):
    if 0 <= angle1 < 180 and 0 <= angle2 < 180 and 0 <= angle3 < 180:
        if angle1 + angle2 == 90 or angle1 + angle3 == 90 or angle2 + angle3 == 90:
            return True
    return False

result = r_triangle(30, 60, 90)

if result:
    print("It's a right triangle.")
else:
    print("It's not a right triangle.")