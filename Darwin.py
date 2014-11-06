# -------------------------------
# Jacob Garcia
# jg56492
# -------------------------------

class Darwin:
    
    def __init__(self, height, width):
        assert type(height) is int
        assert type(width) is int
        
        self.h = height
        self.w = width
        self.creatures = []
        self.grid = [["."]*width for i in range(height)]

    def addCreature(self, Creature, x, y, d):
        # d is a direction
        # n, e, s, or w
        assert type(d) is str        

        self.creatures.append(Creature)
        self.grid[x][y] = Creature
        Creature.pos = self.grid[x][y]
         
class Species:
    
    def __init__(self, name):
        assert type(name) is str
        
        self.name = name[0]
        self.program = []
                
    def addInstruction(self, instruction):
        assert type(instruction) is str
        
        instruction = instruction.split()
        
        # Control Instruction conversion
        if len(instruction) > 1:
            line = instruction[1]
            line = int(line)
            instruction[1] = line
            
        self.program.append(instruction)
        
class Creature:

    def __init__(self, Species):
        self.species = Species
        self.x = None
        self.y = None
        self.d = None
        self.c = None
        self.program = Species.program 

    def execute(self, grid)
        turn_over = False
        line = 0
        current = program[line]        

        while (turn_over == False):
                        

            # -------------------
            # Action instructions  
            # -------------------

            # Hop - If the space ahead is empty, move forward, otherwise, do nothing.
            if current == "hop":
                if self.d == "n":
                    ahead == grid[self.x, self.y-1]
                if self.d == "e":
                    ahead == grid[self.x+1, self.y]
                if self.d == "s":
                    ahead == grid[self.x, self.y+1]
                if self.d == "w":
                    ahead == grid[self.x-1, self.y]
                
                if ahead == ".":
                
                line += 1
                turn_over = True

            # Left - Turn to face left
            if current == "left":
                if self.d == "n":
                    self.d = "w"
                if self.d == "e":
                    self.d = "n"
                if self.d == "s":
                    self.d = "w"
                if self.d == "w":
                    self.d = "n"

                line += 1
                turn_over = True

            # Right - Turn to face right.
            if current == "right":
                if self.d == "n":
                    self.d = "e"
                if self.d == "e":
                    self.d = "s"
                if self.d == "s":
                    self.d = "e"
                if self.d == "w":
                    self.d = "s"

                line += 1
                turn_over = True

            # Infect - If the space ahead contains a creature of a different species
            # change that creature to be of same species 
            # reset the program counter, but leave the direction unchanged
            # otherwise, do nothing.
            if current == "infect":
                
                line += 1
                turn_over = True


            # --------------------
            # Control instructions
            # --------------------

            # If the space ahead is empty, go to line n, otherwise, go to the next line.
            if current == "if_empty":

            # If the space ahead is a wall, go to line n, otherwise, go to the next line.
            if current == "if_wall":

            # Randomly choose between going to line n or the next line. 
            # If random.randrange(0, 2) returns an odd number, go to line n. 
            # Call random.seed(0) at the start of every test case that uses random.randrange().
            if current == "if_random":

            # If the space ahead contains a creature of a different species, go to line n
            # otherwise, go to the next line.
            if current == "if_enemy":

            # Go to line n.
            if current == "go":
