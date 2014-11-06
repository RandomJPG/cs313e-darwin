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
        action = 0
        
        for instruction in self.program:
            
            # Action instructions           
            if instruction[0] == "hop"

            if instruction[0] == "left"

            if instruction[0] == "right"

            if instruction[0] == "infect"


            # Control instructions

            if instruction[0] == "if_empty"

            if instruction[0] == "if_wall"

            if instruction[0] == "if_random"

            if instruction[0] == "if_enemy"

            if instruction[0] == "go"
