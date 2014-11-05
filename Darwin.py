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

class Species:
    
    def __init__(self, name):
        assert type(name) is str
        
        self.name = name[0]
        self.program = []
                
    def addInstruction(self, instruction):
        assert type(instruction) is str
        
        self.program.append(instruction)
        