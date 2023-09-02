'''colors - red,black,white,green
   numbers- 1,2,3,4
   shapes - spade,club,heart,diamond
   choose - black 4 spade(wins lucky draw)'''

print("  ****WELCOME TO LUCKY DRAW****   ")
colors= ['red','black','white','green']
print(colors)
a=input("choose a color: ")
numbers= ['1','2','3','4']
print(numbers)
b=input("choose a number: ")
shapes= ['spade','club','heart','diamond']
print(shapes)
c=input("choose a shape: ")
if (a=='black' and b=='4' and c=='spade'):
    print("congratulations!!U won a lucky draw")
elif (a=='red' and b=='3' and c=='spade'):
     print("congratulations!!U won a lucky draw")
else:
    print("better luck next time")
