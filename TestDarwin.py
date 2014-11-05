# -------------------------------
# Jacob Garcia
# jg56492
# -------------------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase
import Darwin

#------------
# TestDarwin
#------------

class TestDarwin (TestCase) :

    # -------
    # Species
    # -------
    
    def test_species_1(self):
        # Short name
        a = Darwin.Species("a")
        self.assertEqual(a.name, "a") 

    def test_species_2(self):
        # Long name
        a = Darwin.Species("Bob")
        self.assertEqual(a.name, "B")
        
    def test_species_3(self):
        # No commands
        a = Darwin.Species("a")
        self.assertEqual(a.program, [])
        
    def test_species_4(self):
        # Length of program list
        a = Darwin.Species("a")
        a.addInstruction("1")
        self.assertEqual(len(a.program), 1)
    
    # ------
    # Darwin
    # ------
    
    def test_darwin_1(self):
        # Same height/width, small grid
        game = Darwin.Darwin(8,8)
        self.assertEqual(game.h, 8)
        self.assertEqual(game.w, 8)
        
    def test_darwin_2(self):
        # Different height/width, small grid
        game = Darwin.Darwin(7, 9)
        self.assertEqual(game.h, 7)
        self.assertEqual(game.w, 9)
        
    def test_darwin_3(self):
        # Same height/width, big grid
        game = Darwin.Darwin(72, 72)
        self.assertEqual(game.h, 72)
        self.assertEqual(game.w, 72)
        
    def test_darwin_4(self):
        # Different height/width, big grid
        game = Darwin.Darwin(90, 100)
        self.assertEqual(game.h, 90)
        self.assertEqual(game.w, 100)
          
# ----
# main
# ----

main()