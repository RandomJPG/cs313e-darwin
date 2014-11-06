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
        self.creatures.append(Creature)
        self.grid[x][y] = Creature
        Creature.x = x
        Creature.y = y
        Creature.d = d
        
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

    def execute(self, Darwin):
        action = 0
        line = 0
        while (action == 0):
            
            # -------------------
            # Action instructions
            # -------------------
            

            #hHop - If the space ahead is empty, move forward, otherwise, do nothing.
            if self.program[line][0] == "hop":
                if self.d == 0:
                    ahead = Darwin.grid[self.x - 1][self.y]
                    if ahead == ".":
                        Darwin.grid[self.x][self.y] = "."
                        self.x = self.x -1
                        Darwin.addCreature(self, self.x, self.y, self.d)
                if self.d == 1:
                    ahead = Darwin.grid[self.x][self.y - 1]
                    if ahead == ".":
                        Darwin.grid[self.x][self.y] = "."
                        self.y = self.y -1
                        Darwin.addCreature(self, self.x, self.y, self.d)
                if self.d == 2:
                    ahead = Darwin.grid[self.x+1][self.y]
                    if ahead == ".":
                        Darwin.grid[self.x][self.y] = "."
                        self.x = self.x + 1
                        Darwin.addCreature(self, self.x, self.y, self.d)
                if self.d == 3: 
                    ahead = Darwin.grid[self.x][self.y+1]
                    if ahead == ".":
                        Darwin.grid[self.x][self.y] = "."
                        self.y = self.y + 1
                        Darwin.addCreature(self, self.x, self.y, self.d)
                action = 1
                break

            # left - turn to face left
            if self.program[line][0] == "left":
                if self.d == 0:
                    self.d = 3
                if self.d == 1:
                    self.d = 0
                if self.d == 2:
                    self.d = 1
                if self.d == 3:
                    self.d = 0
                action = 1
                break
                
            # right - turn to face right
                if self.d == 0:
                    self.d = 1
                if self.d == 1:
                    self.d = 2
                if self.d == 2:
                    self.d = 3
                if self.d == 3:
                    self.d = 2
                action = 1
                break
                
            # infect - If the space ahead contains a creature of a different species
            # change that creature to be of your species
            # reset the program counter, but leave the direction unchanged
            # otherwise, do nothing.
            if self.program[line][0] == "infect":
                if self.d == 0:
                    ahead = Darwin.grid[self.x - 1][self.y]
                    if ahead not ".":
                        Creature
                if self.d == 1:
                    ahead = Darwin.grid[self.x][self.y - 1]
                    if ahead == ".":
                        Darwin.grid[self.x][self.y] = "."
                        self.y = self.y -1
                        Darwin.addCreature(self, self.x, self.y, self.d)
                if self.d == 2:
                    ahead = Darwin.grid[self.x+1][self.y]
                    if ahead == ".":
                        Darwin.grid[self.x][self.y] = "."
                        self.x = self.x + 1
                        Darwin.addCreature(self, self.x, self.y, self.d)
                if self.d == 3: 
                    ahead = Darwin.grid[self.x][self.y+1]
                    if ahead == ".":
                        Darwin.grid[self.x][self.y] = "."
                        self.y = self.y + 1
                        Darwin.addCreature(self, self.x, self.y, self.d)
                action = 1
                break

            # --------------------
            # Control instructions
            # -------------------- 

            # If the space ahead is empty, go to line n, otherwise, go to the next line.
            if self.program[line][0] == "if_empty":
                if self.d == 0:
                    ahead = Darwin.grid[self.x - 1][self.y]
                    if ahead == ".":
                        line = self.program[line][1]
                    else:
                        line +=1
                        continue
                if self.d == 1:
                    ahead = Darwin.grid[self.x][self.y - 1]
                    if ahead == ".":
                        line = self.program[line][1]
                    else:
                        line +=1
                        continue
                if self.d == 2:
                    ahead = Darwin.grid[self.x+1][self.y]
                    if ahead == ".":
                        line = self.program[line][1]
                    else:
                        line +=1
                        continue
                if self.d == 3: 
                    ahead = Darwin.grid[self.x][self.y+1]
                    if ahead == ".":
                        line = self.program[line][1]
                    else:
                        line +=1
                        continue

            # if_wall - If the space ahead is a wall, go to line n, otherwise, go to the next line.
            if self.program[line][0] == "if_wall":
                Darwin.if_empty(Creature)
                line = program[line][1]
                break

            # if_random - Randomly choose between going to line n or the next line. 
            # If random.randrange(0, 2) returns an odd number, go to line n. 
            # Call random.seed(0) at the start of every test case that uses random.randrange().
            if self.program[line][0] == "if_random":
                Darwin.if_empty(Creature)
                line = program[line][1]
                break

            # if_enemy - If the space ahead contains a creature of a different species, go to line n,           
            # otherwise, go to the next line.
            if self.program[line][0] == "if_enemy":
                Darwin.if_empty(Creature)
                line = program[line][1]
                break

            # go - Go to line n.
            if self.program[line][0] == "go":
                line = self.program[line][1]
                continue
