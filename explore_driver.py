#battoed, bentleyj, L2
#for csc236, dr. jan pearce


from explore import * #calls our explore class which handles all the data
from player import *
import turtle


wn = turtle.Screen()
wn.bgpic("rock_box.gif")
wn.register_shape("player.gif")

def get_dimensions(map_name):
    '''This method is used to read in the map's first line and establish its
    dimensions.
    pre: correctly formatted map name with the first line containing the map's coordinates formatted rr cc
    post: cartesian coordinates telling the software how big the map is
    note: this method is not used in the current version of the program'''
    #read the map
    dimensions = [] #creates empty list to store how big the map it
    with open(map_name) as f: #opens file with the name that is passed to it
        for i,line in enumerate(f): #looks at the lines of the file
            if i == 0: #but only the first line
                height = int(line[:2]) #the height is everything up to the third entry
                width = int(line[3:5]) # but the width is the second number
                dimensions.append(width) # width is added to the list
                dimensions.append(height) #height is added to the lise
    return dimensions #the list is made usable by the method

def get_map(map_name):
    '''A method used to make the map readable by the explore class
    pre: a text file depicting an ASCII art map consisting only of periods, w's and t's
    post: a map that is formatted in such a way that explore can use it
    '''
    mapp = [] #creates an empty list called mapp
    with open(map_name) as f: #opens a file with the name passed to this method
        for i,line in enumerate(f): #reads the file line by line
            if i > 0: #for all lines that are not the first line, it nests those, essentially making our rows
                item_list = []
                for l in line:
                    item_list.append(l.lower().strip('\n').replace(' ', '')) #removes spaces and returns from the file
                mapp.append(item_list) #adds those lists to the list
    return mapp #sends a usable map file to wherever this is initally called in main



def find_me(mapp):
    '''This method finds the initial position of the cursor in the map that represents our explorer
    pre: a map with a single m somewhere in it
    post: coordinates that point to that m
    '''
    r = 0 #sets row variable as 0
    for col in mapp: #each item in that mapp will basically represent a row
        c = 0 #starts counting columns at 0
        for item in col: #each item in that row will be represent a column
            if item == "m": #once it finds the m, it returns its location
                return (r,c)
            c += 1 #counts columns
        r += 1 #counts columns


def main():
    map_name = raw_input("Enter the map you would like to use:\n")
    dimensions =  get_dimensions(map_name)
    mapp = get_map(map_name)
    me_loc = find_me(mapp)
    #call to map draw goes here, ask David to explain later
    player = Player(me_loc, mapp, dimensions)
    player.draw_map()
    wn.onkey(player.north, "Up")
    wn.onkey(player.west, "Left")
    wn.onkey(player.south, "Down")
    wn.onkey(player.east, "Right")
    wn.listen()
    wn.exitonclick()

    #explorer = Explorer(me_loc, mapp, dimensions)
    #answer = explorer.explore(False)
    #if answer == True:
       # print "Every part of the cave that is accessible has been explored.\n"
        #print "You found " + str(len(explorer.treasure)) + " treasure(s) at these locations:\n"
        #for treasure in explorer.treasure:
                # print treasure
               #  print "To get to the treasure you followed this path:"
               #  print explorer.treasure_path[explorer.treasure.index(treasure)]
                # print "\n"




main()
