triangle_line1 = input("Enter the first triangle line: ")
triangle_line2 = input("Enter the second triangle line: ")
triangle_line3 = input("Enter the third triangle line: ")
if triangle_line1 == triangle_line2 == triangle_line3:
    print("The triangle is equilateral.")
elif triangle_line1 == triangle_line2 or triangle_line1 == triangle_line3 or triangle_line2 == triangle_line3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")
