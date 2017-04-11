"""
Authors: Jordan Bentley, David Battoe
Project: Lab 02
This class will allow the user to input a position, and a map that is in the correct format and
the class object will then move through the map and collect treasures as it goes. When a treasure is found
the path taken to this treasure will be recorded alongside the location of the treasure. This information will be stored
in class variables which can be used to report the information to the driver file.
"""
from Stack import *

class Explorer(object):

    def __init__(self, pos, mapp, dim):
        """
        :param pos: Must be a tuple with integers in this format (x, y)
        :param mapp: Must be a nested list of rows
        :param dim: Must be tuple with integers in the format of (x, y)
        :return: None
        """
        self.mapp = mapp                        #Gives the Explorer a map of the area
        self.dim = dim                          #Sets dimensions of the map
        self.row = pos[0]                       #Sets the row position of the Explorer
        self.col = pos[1]                       #Sets the column position of the Explorer
        self.pos = (self.row, self.col)         #Sets self.pos to a tuple to the current row, current col
        self.breadcrum = Stack()                #Instantiates a Stack object to keep track of movements
        self.path = Stack()                     #Instantiates a Stack object to keep track of movements towards Treasure
        self.treasure = []                      #Creates a list to keep track of the Treasures that have been found
        self.treasure_path = []                 #Creates a list to keep track of the Path taken to each Treasure


    def get_pos(self):
        """
        pre: None
        :return: Updated self.pos
        """
        self.pos = (self.col, self.row)         #Resets the self.pos using the current values of the row and col
        return self.pos                         #Returns the updated self.pos


    def explore(self, done):
        """
        This method is used recursively to move through the cave.
        :param done: Keep track of the recursion
        :return: Returns True when the map has been explored.
        """
        if done == True:                        #Base case to break recursion
            self.explore(True)                  #Breaks recursion
        elif done == False:                     #If the map isn't fully explored, the recursion continues
            self.print_mapp()                   #Prints the map
            self.get_surroundings()             #Calls the get_surrounds method to update the needed variables
            stuck = self.order()                #Checks to see if the Explorer is in a location where they are stuck
            if stuck == False:                  #If they are not stuck, the self.explore method is called recursively
                self.explore(False)             #Continues recursion
            elif stuck == True:                 #If the Explorer is stuck, the self.backtrack is called
                finished = self.backtrack()     #Calls self.backtrack
                if finished == False:           #If the backtracking was successful, the recursion will continue
                    self.explore(False)         #with the new location
                elif finished == True:          #If the backtracking was unsuccessful, the recursion will begin to break
                    return True                 #Breaks recursion
        return True                             #Returns True when the map has been fully explored


    def backtrack(self):
        """
        pre: None
        :return: Moves the Explorer to the first position in the breadcrum stack object which is the last location the
            Explorer was located.
        """
        if not self.breadcrum.items:                        #Checks if the stack is empty
            return True                                     #If so, it returns True
        else:                                               #If not,
            direction = self.breadcrum.pop()                #Returns the first item in the stack being the last location
            if direction == 'n':                            #If the last location was 'n'
                self.row += 1                               #Returns the Explorer to that location
                self.mapp[self.row][self.col] = 'm'         #Sets 'm' to the correct location in the mapp
                self.mapp[self.row - 1][self.col] = ','     #Sets the previous location to a , indicating a visit there
                return False                                #Returns False to tell the explore method it was successful
            elif direction == 'e':                          #If the last location was 'e'
                self.col -= 1
                self.mapp[self.row][self.col] = 'm'
                self.mapp[self.row][self.col + 1] = ','
                return False
            elif direction == 'w':                          #If the last location was 'w'
                self.col += 1
                self.mapp[self.row][self.col] = 'm'
                self.mapp[self.row][self.col - 1] = ','
                return False
            elif direction == 's':                          #If the last location was 's'
                self.row -= 1
                self.mapp[self.row][self.col] = 'm'
                self.mapp[self.row + 1][self.col] = ','
                return False


    def get_surroundings(self):
        """
        This method checks the area around the Explorer and sets the surroundings to variables.
        The 'if' statement will check for Treasure in these locations. If found, it calls the self.get_treasure method
        :return: The variables self.n, self.e, self.w, self.s are filled with the corresponding items.
        """
        self.n = self.mapp[self.row - 1][self.col]                      #Returns the value 'north' of the Explorer
        self.e = self.mapp[self.row][self.col + 1]                      #Returns the value 'east' of the Explorer
        self.w = self.mapp[self.row][self.col - 1]                      #Returns the value 'west' of the Explorer
        self.s = self.mapp[self.row + 1][self.col]                      #Returns the value 'south' of the Explorer
        if self.n == 't' or self.e == 't' or self.w == 't' or self.s == 't':    #Checks for treasure
            self.get_treasure()                                         #Calls the method self.get_treasure


    def get_treasure(self):
        """
        This method checks for the location of the treasure. Once found, the treasure's location and path will be added
        to corresponding lists. It will also carry out the movement that is found in the self.order method.
        :return: Appends the location of the Treasure to self.treasure.
                Appends the path taken to the Treasure to self.treasure_path.
        """
        if self.n == 't':                                           #If the Treasure is located to the North
            self.row -= 1                                           #Sets the Explorers position to that of the Treasure
            self.treasure.append(self.get_pos())                    #Appends the location to the self.treasure list
            self.mapp[self.row][self.col] = 'm'                     #Changes the corresponding character to 'm' in mapp
            self.mapp[self.row + 1][self.col] = ','                 #Changes the previous location to a ','
            self.breadcrum.push('n')                                #Adds the movement to the breadcrum stack
            self.path.push("North")                                 #Adds the movement to the path stack
            self.treasure_path.append(self.path.get_items())        #Appends the path to the treasure to self.treasure_path
            self.path.clear_all()                                   #Resets the path stack to allow new path for Treasure
        elif self.e == 't':                                         #If the Treasure is located to the East
            self.col += 1
            self.treasure.append(self.get_pos())
            self.mapp[self.row][self.col] = 'm'
            self.mapp[self.row][self.col - 1] = ','
            self.breadcrum.push('e')
            self.path.push("East")
            self.treasure_path.append(self.path.get_items())
            self.path.clear_all()
        elif self.w == 't':                                         #If the Treasure is located to the West
            self.col -= 1
            self.treasure.append(self.get_pos())
            self.mapp[self.row][self.col] = 'm'
            self.mapp[self.row][self.col + 1] = ','
            self.breadcrum.push('w')
            self.path.push("West")
            self.treasure_path.append(self.path.get_items())
            self.path.clear_all()
        elif self.s == 't':                                         #If the Treasure is located to the South
            self.row += 1
            self.treasure.append(self.get_pos())
            self.mapp[self.row][self.col] = 'm'
            self.mapp[self.row - 1][self.col] = ','
            self.breadcrum.push('s')
            self.path.push("South")
            self.treasure_path.append(self.path.get_items())
            self.path.clear_all()
        return False                                                #Returns False


    def order(self):
        """
        This function contains the movement algorithm for the Explorer class. It checks each direction in order of
            'N' , 'E', 'W', then 'S'. This is to prevent from going the same direction everytime the method is called.
        :return: When a decision for a direction has been made, the Explorer will be moved in that direction, the location
            the Explorer was in will be replaced with a ',' to show that the Explorer has been to that location previously.
            It will also add the movement to the path and breadcrum to keep track of the movements.
        """
        if self.n == '.':                               #If the value to the 'North' is a valid path i.e. a '.'
            self.row -= 1                               #Sets the Explorers location to that of the '.'
            self.mapp[self.row][self.col] = 'm'         #Moves the 'm' in mapp to match the Explorers location
            self.mapp[self.row + 1][self.col] = ','     #Leaves a 'breadcrumb' to tell the Explorer that they have been here
            self.breadcrum.push('n')                    #Adds the movement to the breadcrum stack
            self.path.push("North")                     #Adds the movement to the path stack
            return False                                #Returns False to tell the explore method it could move.
        elif self.e == '.':                             #Else if the value to the East is a valid path i.e. a '.'
            self.col += 1
            self.mapp[self.row][self.col] = 'm'
            self.mapp[self.row][self.col - 1] = ','
            self.breadcrum.push('e')
            self.path.push("East")
            return False
        elif self.w == '.':                             #Else if the value to the West is a valid path i.e. a '.'
            self.col -= 1
            self.mapp[self.row][self.col] = 'm'
            self.mapp[self.row][self.col + 1] = ','
            self.breadcrum.push('w')
            self.path.push("West")
            return False
        elif self.s == '.':                             #Else if the value to the West is a valid path i.e. a '.'
            self.row += 1
            self.mapp[self.row][self.col] = 'm'
            self.mapp[self.row - 1][self.col] = ','
            self.breadcrum.push('s')
            self.path.push("South")
            return False
        elif self.s == ',' or self.s == 'w':            #This checks for a ',' or a 'w' to the South. If this is True,
            return True                                 #this tells the self.explore method that no valid path is available


    def print_mapp(self):
        """
        :return: Prints the current Map of the area in the console.
        """
        for row in self.mapp:                           #Iterates the the mapp nested list to print the rows correctly
            print ''.join(map(str, row))                #Removes the empty spaces and makes the map more readable
        print '\n\n'                                    #Adds space for readability


    def print_treasure(self):
        """
        :return: Returns the currently found Treasure
        """
        return self.treasure
