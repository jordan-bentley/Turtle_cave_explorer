from Stack import *
import turtle
import time

class Player(object):
    def __init__(self, pos, mapp, dim):
        """
        :param pos: Must be a tuple with integers in this format (x, y)
        :param mapp: Must be a nested list of rows
        :param dim: Must be tuple with integers in the format of (x, y)
        :return: None
        """
        self.mapp = mapp  # Gives the Explorer a map of the area
        self.dim = dim  # Sets dimensions of the map
        self.row = pos[0]  # Sets the row position of the Explorer
        self.col = pos[1]  # Sets the column position of the Explorer
        self.pos = (self.row, self.col)  # Sets self.pos to a tuple to the current row, current col
        self.breadcrum = Stack()                #Instantiates a Stack object to keep track of movements
        self.path = Stack()                     #Instantiates a Stack
        self.treasure = Stack()
        self.treas_turt = turtle.Turtle()
        self.treas_turt.hideturtle()
        self.treas_turt.penup()
        self.turt = turtle.Turtle()
        self.treas_num = 0
        self.check = False


    def draw_map(self):
        #turt = turtle.Turtle()
        self.x = self.dim[0]
        self.y = self.dim[1]
        self.turt.penup()
        self.turt.speed(0)
        self.turt.shape('square')
        self.turt.setpos(-10*self.x, self.y*10)
        for row in self.mapp:    #looking at the rows in the map
            for column in row:   #looking at the columns in the rows
                # for place in column:
                if column == 'w':            #this evaluates what letter 'column' is
                    self.turt.color('brown') #sets color based on  which character is imported
                    self.turt.stamp()        #each stamp draws a pixel  of the map
                elif column == 't':          #this evaluates what letter 'column' is
                    self.turt.color('navy')  #sets color based on  which character is imported
                    self.turt.stamp()        #each stamp draws a pixel  of the map
                elif column == 'm' or column == 'r': #this evaluates what letter 'column' is
                    self.x = self.turt.xcor()
                    self.y = self.turt.ycor()
                    self.turt.color('red')   #sets color based on  which character is imported
                    self.turt.stamp()        #each stamp draws a pixel  of the map
                elif column == 's':          #this evaluates what letter 'column' is
                    self.turt.color('brown') #sets color based on  which character is imported
                    self.turt.stamp()        #each stamp draws a pixel  of the map
                elif column == 'o':          #this evaluates what letter 'column' is
                    self.turt.color('peach puff')#sets color based on  which character is imported
                    self.turt.stamp()        #each stamp draws a pixel  of the map
                elif column == 'b':          #this evaluates what letter 'column' is
                    self.turt.color('black') #sets color based on  which character is imported
                    self.turt.stamp()        #each stamp draws a pixel  of the map
                elif column == 'l':          #this evaluates what letter 'column' is
                    self.turt.color('light blue')#sets color based on  which character is imported
                    self.turt.stamp()        #each stamp draws a pixel  of the map
                elif column == 'p':          #this evaluates what letter 'column' is
                    self.turt.color('pink')  #sets color based on  which character is imported
                    self.turt.stamp()        #each stamp draws a pixel  of the map
                elif column == 'h':          #this evaluates what letter 'column' is
                    self.turt.color('white') #sets color based on  which character is imported
                    self.turt.stamp()        #each stamp draws a pixel  of the map
                elif column == 'y':          #this evaluates what letter 'column' is
                    self.turt.color('yellow')#sets color based on  which character is imported
                    self.turt.stamp()        #each stamp draws a pixel  of the map
                elif column == 'g':          #this evaluates what letter 'column' is
                    self.turt.color('gray')  #sets color based on  which character is imported
                    self.turt.stamp()        #each stamp draws a pixel  of the map
                self.turt.setpos(self.turt.xcor()+20, self.turt.ycor()) #this moves over by 20 units with each stamp, which is the size of the pixels
            self.turt.setpos(self.turt.xcor()-(len(row)*20),self.turt.ycor()-20) #this moves to the beginning of the line and moves down by the width of a pixel
        self.turt.setpos(self.x,self.y)      #the position of 'm' from before is retrieved so the player starts there
        self.turt.pendown()
        self.turt.pensize(5)
        self.turt.color("green")


    def get_pos(self):
        """
        pre: None
        :return: Updated self.pos
        """
        self.pos = (self.col, self.row)  # Resets the self.pos using the current values of the row and col
        return self.pos  # Returns the updated self.pos

    def get_surroundings(self):
        """
        This method checks the area around the Explorer and sets the surroundings to variables.
        The 'if' statement will check for Treasure in these locations. If found, it calls the self.get_treasure method
        :return: The variables self.n, self.e, self.w, self.s are filled with the corresponding items.
        """
        self.n = self.mapp[self.row - 1][self.col]  # Returns the value 'north' of the Explorer
        self.e = self.mapp[self.row][self.col + 1]  # Returns the value 'east' of the Explorer
        self.w = self.mapp[self.row][self.col - 1]  # Returns the value 'west' of the Explorer
        self.s = self.mapp[self.row + 1][self.col]  # Returns the value 'south' of the Explorer


    def north(self):
        self.get_surroundings()
        self.undo()
        if self.n == '.':  # If the value to the 'North' is a valid path i.e. a '.'
            self.row -= 1  # Sets the Explorers location to that of the '.'
            self.mapp[self.row][self.col] = 'm'  # Moves the 'm' in mapp to match the Explorers location
            self.mapp[self.row + 1][self.col] = ','  # Leaves a 'breadcrumb' to tell the Explorer that they have been here
            self.breadcrum.push('n')  # Adds the movement to the breadcrum stack
            self.path.push("North")
            self.turt.color("green")
            self.turt.setheading(90)
            self.turt.forward(20)
            self.turt.shape("player.gif")
        elif self.n == ",":
            self.row -= 1  # Sets the Explorers location to that of the '.'
            self.mapp[self.row][self.col] = 'm'  # Moves the 'm' in mapp to match the Explorers location
            self.mapp[self.row + 1][self.col] = ','  # Leaves a 'breadcrumb' to tell the Explorer that they have been here
            self.breadcrum.push('n')  # Adds the movement to the breadcrum stack
            self.path.push("North")
            self.turt.color("green")
            self.turt.setheading(90)
            self.turt.forward(20)
            self.turt.shape("player.gif")
        elif self.n == "t":
            self.row -= 1  # Sets the Explorers location to that of the '.'
            self.mapp[self.row][self.col] = 'm'  # Moves the 'm' in mapp to match the Explorers location
            self.mapp[self.row + 1][self.col] = ','  # Leaves a 'breadcrumb' to tell the Explorer that they have been here
            self.breadcrum.push('n')  # Adds the movement to the breadcrum stack
            self.path.push("North")
            self.turt.color("green")
            self.turt.setheading(90)
            self.turt.forward(20)
            self.turt.shape("player.gif")
            self.get_treasure()



    def east(self):
        self.get_surroundings()
        self.undo()
        if self.e == '.':  # Else if the value to the East is a valid path i.e. a '.'
            self.col += 1
            self.mapp[self.row][self.col] = 'm'
            self.mapp[self.row][self.col - 1] = ','
            self.breadcrum.push('e')
            self.path.push("East")
            self.turt.color("green")
            self.turt.setheading(0)
            self.turt.forward(20)
            self.turt.shape("player.gif")
        elif self.e == ',':  # Else if the value to the East is a valid path i.e. a '.'
            self.col += 1
            self.mapp[self.row][self.col] = 'm'
            self.mapp[self.row][self.col - 1] = ','
            self.breadcrum.push('e')
            self.path.push("East")
            self.turt.color("green")
            self.turt.setheading(0)
            self.turt.forward(20)
            self.turt.shape("player.gif")
        elif self.e == 't':
            self.col += 1
            self.mapp[self.row][self.col] = 'm'
            self.mapp[self.row][self.col - 1] = ','
            self.breadcrum.push('e')
            self.path.push("East")
            self.turt.color("green")
            self.turt.setheading(0)
            self.turt.forward(20)
            self.turt.shape("player.gif")
            self.get_treasure()

    def west(self):
        self.get_surroundings()
        self.undo()
        if self.check == True:
            self.treas_turt.undo()
            self.check = False
        if self.w == '.':                               #Else if the value to the West is a valid path i.e. a '.'
            self.col -= 1
            self.mapp[self.row][self.col] = 'm'
            self.mapp[self.row][self.col + 1] = ','
            self.breadcrum.push('w')
            self.path.push("West")
            self.turt.color("green")
            self.turt.setheading(180)
            self.turt.forward(20)
            self.turt.shape("player.gif")
        elif self.w == ',':                             #Else if the value to the West is a valid path i.e. a '.'
            self.col -= 1
            self.mapp[self.row][self.col] = 'm'
            self.mapp[self.row][self.col + 1] = ','
            self.breadcrum.push('w')
            self.path.push("West")
            self.turt.color("green")
            self.turt.setheading(180)
            self.turt.forward(20)
            self.turt.shape("player.gif")
        elif self.w == 't':
            self.col -= 1
            self.mapp[self.row][self.col] = 'm'
            self.mapp[self.row][self.col + 1] = ','
            self.breadcrum.push('w')
            self.path.push("West")
            self.turt.color("green")
            self.turt.setheading(180)
            self.turt.forward(20)
            self.turt.shape("player.gif")
            self.get_treasure()

    def south(self):
        self.get_surroundings()
        self.undo()
        if self.s == '.':                               #Else if the value to the West is a valid path i.e. a '.'
            self.row += 1
            self.mapp[self.row][self.col] = 'm'
            self.mapp[self.row - 1][self.col] = ','
            self.breadcrum.push('s')
            self.path.push("South")
            self.turt.color("green")
            self.turt.setheading(270)
            self.turt.forward(20)
            self.turt.shape("player.gif")
        elif self.s == ',':                             #Else if the value to the West is a valid path i.e. a '.'
            self.row += 1
            self.mapp[self.row][self.col] = 'm'
            self.mapp[self.row - 1][self.col] = ','
            self.breadcrum.push('s')
            self.path.push("South")
            self.turt.color("green")
            self.turt.setheading(270)
            self.turt.forward(20)
            self.turt.shape("player.gif")
        elif self.s == 't':
            self.row += 1
            self.mapp[self.row][self.col] = 'm'
            self.mapp[self.row - 1][self.col] = ','
            self.breadcrum.push('s')
            self.path.push("South")
            self.turt.color("green")
            self.turt.setheading(270)
            self.turt.forward(20)
            self.turt.shape("player.gif")
            self.get_treasure()


    def show_treasure(self):
        return self.treasure.get_items()

    def get_treasure(self):
        self.treas_turt.undo()
        self.treas_turt.penup()
        self.treas_num += 1
        self.treas_turt.setpos(-100, -220)
        self.treas_turt.write(str("Total treasures:" +str(self.treas_num)), True, "center", ("Corsiva", 30, "normal"))
        self.treas_turt.setpos(-100, -250)
        self.treas_turt.write("You found a Treasure!", True, "center", ("Corsiva", 20, "normal"))
        self.treasure.push(self.get_pos())
        self.check = True


    def undo(self):
        if self.check == True:
            self.treas_turt.undo()
            self.treas_turt.undo()
            self.check = False