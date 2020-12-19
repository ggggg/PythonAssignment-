import math

# returns the volume of a given cylinder
def volume(radius, height):
    return math.pi * (radius * radius) * height

# returns the area of a given cylinder
def area(radius, height):
    return 2 * math.pi * (radius * radius) + 2 * math.pi * height

def main():
  #get radius
  print('Enter radius:')
  radius = float(input())
  #get height
  print('Enter height:')
  height = float(input())
  #output results
  print('Volume:', volume(radius, height))
  print('Surface area:', area(radius, height))

#while the user wants to continue
while(True):
  main()
  print('Do you wish to do another run? (yes, no)')
  if(input().upper() != 'YES'): break;