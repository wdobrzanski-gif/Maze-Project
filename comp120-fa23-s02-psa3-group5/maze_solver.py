"""
module: maze_solver

Implementation of the SquareType, Square, and Maze classes as well as the
maze_solver function.
"""
from enum import Enum
from agenda import StackAgenda, QueueAgenda, Agenda
from sys import argv


class SquareType(Enum):
    WALL = '#'
    OPEN_SPACE = '.'
    START = 'o'
    FINISH = '*'


class Square:
    """ representation of a square in the maze

    >>> s = Square('#', 3, 5)
    >>> str(s)
    '#'
    >>> b = Square('.', 3, 5)
    >>> str(b)
    '.'
    >>> k = Square('o', 3, 5)
    >>> str(k)
    'o'
    >>> v = Square('*', 3, 5)
    >>> str(v)
    '*'
    """
    type: SquareType # The type of square (enum)
    visited: bool # Indicates whether the square has been visited
    location: tuple[int, int] # The location (x, y) of the square

    def __init__(self, rep: str, x: int, y: int) -> None:
        """ Your initializer/constructor"""
        """ Initialize a square with its representation and location.

        Args:
            rep (str): The character representation of the square.
            x (int): The x-coordinate of the square's location.
            y (int): The y-coordinate of the square's location.
        """
  
        self.visited = False
        self.location = (x, y)

        # Determine the type of square based on its representation
        if rep == '#':
            self.type = SquareType.WALL
        elif rep == '.':
            self.type = SquareType.OPEN_SPACE
        elif rep == 'o':
            self.type = SquareType.START
        elif rep == '*':
            self.type = SquareType.FINISH
        else:
            raise ValueError("Wrong Type string")

    def __str__(self) -> str:
        """ Convert the square to a string representation.

        Returns:
            str: The string representation of the square, which can be a wall ('#'),
            open space ('.'), start point ('o'), finish point ('*'), or visited open
            space ('x').
        """

        if self.type == SquareType.OPEN_SPACE and self.visited:
            return 'x'
        else:
            return self.type.value



class BadMazeFileFormat(Exception):
    """ Raise when the given file
    does not have the correct format"""
    pass


class Maze:
    """store the logical layout of a maze. 
      """
    _locations: list[list[Square]]
    width: int  # X
    height: int  # y

    def __init__(self, filename: str) -> None:
        """ Your initializer/constructor"""
        
        self._locations = []# Initialize an empty list to store maze locations

        with open(filename) as f: # Open and read the maze file

            line = f.readline().split() # Read the first line and split it into tokens
            
            if len(line) != 2:
                raise BadMazeFileFormat # Check for correct file format (width and height)
            self.width = int(line[0]) # Extract and store the maze width
            self.height = int(line[1]) # Extract and store the maze height
            
            row_count = 0 # Initialize a row count to keep track of the rows in the maze
            
            for line in f: # Iterate through the lines in the file
                line = line.strip() # Remove leading/trailing white space from the line
                if len(line) != self.width:
                    raise BadMazeFileFormat # Check for consistent row width
                row_lst = [] # Initialize an empty list to store squares in the current row
                col_count = 0 # Initialize a column count to keep track of columns in the row
                for ch in line:  # Iterate through the characters in the line
                    try:
                        square = Square(ch, col_count, row_count)
                    except ValueError:
                        raise BadMazeFileFormat # Check for valid characters in the maze
                    col_count += 1
                    row_lst.append(square)
                row_count += 1
                self._locations.append(row_lst) # Add the row of squares to the maze locations
            if len(self._locations) != self.height:
                raise BadMazeFileFormat # Check for consistent maze height in the file

    def __str__(self) -> str:
        """ Covert your maze to a string"""
        s = "" # Initialize an empty string to store the maze representation
        for row in self._locations: # Iterate through each row in the maze
            
            for square in row: # Iterate through each square in the current row
                
                s += str(square) # Add the string representation of the square to the string
            
            s += "\n" # Add a newline character to separate rows
        
        return s # Return the complete string representation of the maze

    def starting_square(self) -> Square:
        """
        Returns the square in the maze that represents the starting point.

        """
        for row in self._locations: # Iterate through each row in the maze
            for square in row: # Iterate through each square in the current row
                if square.type == SquareType.START: # Check if the square is of type 'START'
                    return square # Return the square representing the starting point

    def finish_square(self) -> Square:
        """
        Returns the square in the maze that represents the starting point.

        """
        for row in self._locations: # Iterate through each row in the maze
            for square in row: # Iterate through each square in the current row
                if square.type == SquareType.FINISH: # Check if the square is of type 'FINISH'
                    return square # Return the square representing the finishing point

    def get_square(self, x: int, y: int) -> Square:
        """
        Returns the square at the given (x,y) location.

        """
        return self._locations[y][x]

    def get_neighbors(self, x: int, y: int) -> list[Square]:
        '''
        Returns the list of
        neighboring Squares in the north, south, east, and west directions from the location
        (x,y).
        '''
        nb_list = [] # Initialize an empty list to store neighboring squares

        if y - 1 >= 0:
            north = self.get_square(x, y - 1) # Get the square to the north
            nb_list.append(north) # Add it to the list of neighbors

        if y + 1 < self.height:
            south = self.get_square(x, y + 1) # Get the square to the south
            nb_list.append(south) # Add it to the list of neighbors

        if x + 1 < self.width:
            east = self.get_square(x+1, y) # Get the square to the east
            nb_list.append(east) # Add it to the list of neighbors

        if x - 1 >= 0:
            west = self.get_square(x-1, y) # Get the square to the west
            nb_list.append(west) # Add it to the list of neighbors

        return nb_list # Return the list of neighboring squares




def maze_solver(maze: Maze, agenda: Agenda, wait_for_user: bool = True) -> bool:
    """
    Determine whether a maze has a solution by navigating from the start to the finish,
    avoiding walls if any are present.

    Args:
        maze (Maze): The maze object representing the environment.
        agenda (Agenda): The agenda data structure used for navigation.
        wait_for_user (bool, optional): If True, pause and display the maze between steps
        for user interaction. Defaults to True.

    Returns:
        bool: True if a solution exists, False otherwise.
    """

    # Clear the agenda and add the starting square to it
    while not agenda.is_empty():
        agenda.pop()
    agenda.add(maze.starting_square())

    while not agenda.is_empty():
        if wait_for_user:
            # Display the maze and wait for user input to continue
            print(maze)
            _ = input(" Press enter to continue ")
        
        # Remove the current square from the agenda
        cur = agenda.remove()

        if not cur.visited:
            if cur.location == maze.finish_square().location:
                return True
            else:
                # Get the neighboring squares and add them to the agenda if they are not walls
                nb_lst = maze.get_neighbors(cur.location[0], cur.location[1])
                for n in nb_lst:
                    if n.type != SquareType.WALL:
                        agenda.add(n)
            cur.visited = True # Mark the current square as visited

    # No solution found
    return False


def main(maze_filename: str, agenda_type: str) -> None:
    """

    """
    assert agenda_type in [
        "stack", "queue"], 'Agenda type must be "stack" or "queue"'
    maze = Maze(maze_filename)

    if agenda_type == "stack":
        agenda = StackAgenda()
    else:
        agenda = QueueAgenda()

    maze_result = maze_solver(maze, agenda)

    if maze_result == True:
        print("Maze solution found")
    else:
        print('Maze solution does not exist')


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print('Usage: python3 maze_solver.py <maze_filename> <agenda_type>')
    else:
        maze_filename = sys.argv[1]
        agenda_type = sys.argv[2]

        main(maze_filename, agenda_type)