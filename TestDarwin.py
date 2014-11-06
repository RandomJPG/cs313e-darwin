# -------------------------------
# Jacob Garcia
# jg56492
# -------------------------------

# -------
# imports
# -------

from io       import StringIO
import re
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
    
    def test_species_5(self):
        # Control commands
        a = Darwin.Species("a")
        a.addInstruction("if_empty 1")
        self.assertEqual(a.program[0],["if_empty", 1])
        
    def test_species_6(self):
        # Program navigation
        a = Darwin.Species("a")
        a.addInstruction("if_wall 3")
        a.addInstruction("hop")
        a.addInstruction("go 0")
        a.addInstruction("left")
        a.addInstruction("go 0")
        self.assertEqual(a.program[0], ["if_wall", 3])
        self.assertEqual(a.program[1], ["hop"])
        self.assertEqual(a.program[2], ["go", 0])
        self.assertEqual(a.program[3], ["left"])
        self.assertEqual(a.program[4], ["go", 0])
        
    # --------
    # Creature
    # --------
    
    def test_creature_1(self):
        # X/Y coordinates
        a = Darwin.Species("a")
        b = Darwin.Creature(a)
        self.assertIsNone(b.x)
        self.assertIsNone(b.y)
        
    def test_creature_2(self):
        # Direction
        a = Darwin.Species("a")
        b = Darwin.Creature(a)
        self.assertIsNone(b.d)
        
    def test_creature_3(self):
        # Counter
        a = Darwin.Species("a")
        b = Darwin.Creature(a)
        self.assertIsNone(b.c)
        
    def test_creature_4(self):
        # Species
        a = Darwin.Species("a")
        b = Darwin.Creature(a)
        self.assertEqual(type(b.species),Darwin.Species)
        
    def test_creature_5(self):
        # Species name
        a = Darwin.Species("a")
        b = Darwin.Creature(a)
        self.assertEqual(b.species.name,"a")
        
    def test_creature_6(self):
        # Program
        a = Darwin.Species("a")
        b = Darwin.Creature(a)
        self.assertEqual(a.program,b.program)

    def test_creature_7(self):
        # Execute Action- Hop
        a = Darwin.Species("a")
        a.addInstruction("hop")
        b = Darwin.Creature(a)
        game = Darwin.Darwin(4, 4)
        game.addCreature(b, 0, 0, 2)
        b.execute(game)
        self.assertEqual(b.x, 1)
        self.assertEqual(b.y, 0)

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
    
    def test_darwin_4(self):
        # Different height/width, big grid
        game = Darwin.Darwin(90, 100)
        self.assertEqual(game.h, 90)
        self.assertEqual(game.w, 100)

    def test_darwin_5(self):
        # Test Grid
        game = Darwin.Darwin(2, 3)
        self.assertEqual(game.grid, [[".",".","."],[".",".","."]])
          
    
    def test_darwin_6(self):
        # Test addCreature
        game = Darwin.Darwin(2, 3)
        a = Darwin.Species("a")
        b = Darwin.Creature(a)
        game.addCreature(b, 1, 2, 1)
        self.assertEqual(game.grid, [[".",".","."],[".",".", b.species.name]])

    # --------
    # is_empty
    # --------

    def test_is_empty(self):
        game = Darwin.Darwin(7, 7)
        a = Darwin.Species("a")
        b1 = Darwin.Creature(a)
        b2 = Darwin.Creature(a)
        b3 = Darwin.Creature(a)
        b3 = Darwin.Creature(a)
        b4 = Darwin.Creature(a)
        game.addCreature(b1, 0, 0, 1)
        game.addCreature(b2, 0, 6, 1)
        game.addCreature(b3, 6, 6, 1)
        game.addCreature(b4, 6, 0, 1)
        self.assertTrue(game.is_empty(1,1))
        self.assertTrue(game.is_empty(0,1))
        self.assertTrue(game.is_empty(5,6))
        self.assertTrue(game.is_empty(4,3))
        self.assertFalse(game.is_empty(0, 0))
        self.assertFalse(game.is_empty(0, 6))
        self.assertFalse(game.is_empty(6, 6))
        self.assertFalse(game.is_empty(6, 0))

    # -------
    # is_wall
    # -------

    def test_is_wall_1(self):
        game = Darwin.Darwin(7, 7)
        self.assertTrue(game.is_wall(6, 7))

    def test_is_wall_2(self):
        game = Darwin.Darwin(7, 7)
        self.assertTrue(game.is_wall(0, 0))

    def test_is_wall_3(self):
        game = Darwin.Darwin(7, 7)
        self.assertTrue(game.is_wall(7, 7))

    def test_is_wall_4(self):
        game = Darwin.Darwin(7, 7)
        self.assertTrue(game.is_wall(8, 7))

    def test_is_wall_5(self):
        game = Darwin.Darwin(7, 7)
        self.assertTrue(game.is_wall(-1, -7))

    def test_is_not_wall_1(self):
        game = Darwin.Darwin(7, 7)
        self.assertFalse(game.is_wall(3, 3))

    def test_is_not_wall_2(self):
        game = Darwin.Darwin(7,7)
        self.assertFalse(game.is_wall(5,4))

    # --------
    # is_enemy
    # --------

    def test_is_enemy_1(self):
        game = Darwin.Darwin(7, 7)
        a = Darwin.Species("a")
        a1 = Darwin.Creature(a)
        game.addCreature(a1, 0, 1, 1)
        b = Darwin.Species("b")
        b1 = Darwin.Creature(b)
        game.addCreature(b1, 0, 0, 1)
        self.assertTrue(game.is_enemy(0, 0, a))
        self.assertFalse(game.is_enemy(4, 3, a))

    def test_is_enemy_2(self):
        game = Darwin.Darwin(7, 7)
        a = Darwin.Species("a")
        a1 = Darwin.Creature(a)
        a2 = Darwin.Creature(a)
        a3 = Darwin.Creature(a)
        game.addCreature(a1, 0, 1, 1)
        game.addCreature(a2, 0, 2, 1)
        game.addCreature(a3, 0, 3, 1)
        b = Darwin.Species("b")
        b1 = Darwin.Creature(b)
        game.addCreature(b1, 0, 0, 1)
        self.assertTrue(game.is_enemy(0, 0, a))
        self.assertFalse(game.is_enemy(0, 3, a))
    
# ----
# main
# ----

main()
