def mario_difficult():
    while (True):

        ##try and except to catch the error when use inputs string instead of a number
        try:
            height = int(input("Enter the height "))
            if 1 <= height <= 8:
                pyramid(height)
        except ValueError:
            print("That is not a valid value , please enter again")


##function to calculate the pyramid
def pyramid(height):
    for i in range(1, (height + 1)):
        print(' ' * (height - 1), i * '#',' ', i * '#' )
        height -= 1


mario_difficult()

