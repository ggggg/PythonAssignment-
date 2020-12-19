import math


def volume(radius, height):
    return math.pi * (radius * radius) * height


def area(radius, height):
    return 2 * math.pi * (radius * radius) + 2 * math.pi * height

def main():
  print('Enter radius:')
  radius = float(input())
  print('Enter height:')
  height = float(input())
  print('Volume:', volume(radius, height))
  print('Surface area:', area(radius, height))

while(True):
  main()
  print('Do you wish to do another run? (yes, no)')
  if(input().upper() != 'YES'): break;