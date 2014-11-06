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
         

    # Instructions

    # Action Instructions
    def hop(self, Creature):
        if Creature.d == "n":
            ahead == grid[Creature.x][Creature.y-1]
        if Creature.d == "e":
            ahead == grid[Creature.x+1][Creature.y]
        if Creature.d == "s":
            ahead == grid[Creature.x][Creature.y+1]
        if Creature.d == "w":
            ahead == grid[Creature.x-1][Creature.y]

        if ahead == ".":
            if 
            
        
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

    def execute(self):
        action = 0
        line = 0
        while (action == 0):
            
            # -------------------
            # Action instructions
            # -------------------
            
            if self.program[line][0] == "hop":
                Darwin.hop(Creature)    
                action = 1
                break

            if self.program[line][0] == "left":
                Darwin.left(Creature)
                action = 1
                break

            if self.program[line][0] == "right":
                Darwin.right(Creature)
                action = 1
                break
                
            if self.program[line][0] == "infect":
                Darwin.infect(Creature)
                action = 1
                break

            # --------------------
            # Control instructions
            # -------------------- 

            if self.program[line][0] == "if_empty":
                Darwin.if_empty(Creature)
                line = program[line][1]
                break

            if self.program[line][0] == "if_wall":
                Darwin.if_empty(Creature)
                line = program[line][1]
                break

            if self.program[line][0] == "if_random":
                Darwin.if_empty(Creature)
                line = program[line][1]
                break

            if self.program[line][0] == "if_enemy":
                Darwin.if_empty(Creature)
                line = program[line][1]
                break

            if self.program[line][0] == "go":
                Darwin.if_empty(Creature)
                line = program[line][1]
                break
