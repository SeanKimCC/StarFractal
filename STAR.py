import turtle
wn = turtle.Screen()
a = turtle.Turtle()
a.speed(0)

HowSmall = int(input('detail(integer)(the smaller the number gets, the more detailed it gets = ')) #The smaller the number gets, the more detailed it gets
SizeOfTheStar = int(input('The size of the star = '))# Size of the star. From left end to the right end.
length = SizeOfTheStar

def Star(length, scale):

    if length <= HowSmall:
        a.fd(length) # When the function meets the requirements (the length becoming less than or equal to HowSmall) it moves forward by the length.
        return
    
     #The function keeps repeating like a fractal until the length is less than or equal to HowSmall.
    if scale == 1:
        Star(length/2.618033989, 1)
        a.left(72)
        Star(length/2.618033989, 1)
        a.right(144)
        Star(length/2.618033989, 1)
        a.left(72)    
        Star(length/2.618033989, 1)
    else:
        Star(length/2.618033989, -1) #The function keeps repeating like a fractal until the length is less than or equal to HowSmall.
        a.right(72)
        Star(length/2.618033989, -1)
        a.left(144)
        Star(length/2.618033989, -1)
        a.right(72)    
        Star(length/2.618033989, -1)
        
    



a.penup()
a.goto(-140,-30)
a.pendown()
a.color('red')
for l in range(1,3):
    for i in range(1,4):
        Star(length,1)
        a.right(144)
    a.left(144)
    a.color('orange')

a.right(180)
a.penup()
Star(length, -1)#goes opposite to the other sides 
a.pendown()
a.right(36)
a.color('yellow')

for i in range(1,4):
    Star(length, 1)
    a.right(144)
a.left(144)
##    Colour = str(input('The colour is ='''))
##    a.color(Colour)




