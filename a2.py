# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.
    def __init__(self, symbol, row, col):
        """ (Rat,str,int,int)->NoneType

        A Rat with symbol, row, col, and initialize num_sprouts_eaten to 0
        
        >>> Micky = Rat('M', 1, 4)
        >>> Micky.symbol
        'M'
        >>> Micky.row
        1
        >>> Micky.col
        4
        >>> Micky.num_sprouts_eaten
        0
        >>> Micky.eat_sprout()
        >>> Micky.num_sprouts_eaten
        1
        >>> print(Micky)
        """
        self.symbol = symbol
        self.set_location(row, col)
        self.num_sprouts_eaten = 0
        
    def set_location(self, row, col):
        #Set the rat's row and col instance variables to the given row and column.
        
        self.row = row
        self.col = col

    def get_location(self):
        return self.row, self.col
    
    def eat_sprout(self):
        # Add one to the rat's instance variable num_sprouts_eaten. Yuck.
        self.num_sprouts_eaten += 1
        
    def __str__(self):
       return "{0} at ({1}, {2}) ate {3} sprouts.".format(self.symbol, self.row, self.col, self.num_sprouts_eaten)

class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    def __init__(self, maze, rat_1,rat_2):
        
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.set_character_location(rat_1)
        self.set_character_location(rat_2)
        self.num_sprouts_left = self.get_sprouts_count()

    def get_sprouts_count(self):
        total = 0
        
        for each_row in self.maze:
            total += each_row.count(SPROUT)
            
        return total

    def set_character_location(self, rat):
        
        self.maze[rat.row][rat.col] = rat.symbol

    def is_wall(self, row, col):

        return self.maze[row][col] == WALL
    
    def remove_sprout(self, rat, row, col):
        rat.eat_sprout()
        self.num_sprouts_left -=1
        
    def get_character(self, row, col):

        return self.maze[row][col]

    def update_location(self, row, col):
        self.maze[row][col] = HALL
        
    def move(self, rat, vertical_dir, horizontal_dir):
        
        row, col = rat.get_location()
        cur_row, cur_col = row+vertical_dir, col+horizontal_dir
        
        if self.is_wall(cur_row, cur_col):
            return False
        if self.maze[cur_row][cur_col] == SPROUT:
            self.remove_sprout(rat, cur_row, cur_col )
            
        rat.set_location(cur_row, cur_col)
        self.set_character_location(rat)
        self.update_location(row, col)            

        return True
    
    def __str__(self):
        rstring = ''
        for e in self.maze:
           rstring +=  ''.join(e) + "\n"
        return "{0}{1}\n{2}".format(rstring, self.rat_1, self.rat_2)

    
    
