
def mario_easy():
    while (True):

      try:
        height = int(input("Enter the height "))
        if 1<= height <=8:
          pyramid(height)
      except ValueError:
        print("That is not a valid value , please enter again")
            
def pyramid(height):
    j = (height - 1) 
    for i in range(1,(height+1)):
      print(' ' * j , i * '#')
      j -=1

mario_easy()
