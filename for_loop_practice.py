import turtle

def print_triangle(n_lines):
    for i in range(n_lines):
        print(i*'*')

my_drawings=[(0,0),(0,100),(100,100),(100,0),(0,10),(10,0)]
for my_pos in my_drawings:
    turtle.goto(my_pos)
x=3
x=x+3
x-=3
print(x-3)
print(x)
