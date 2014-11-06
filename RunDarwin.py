# -------------------------------
# Jacob Garcia
# jg56492
# -------------------------------

# -------
# imports
# -------

from random import randrange, seed
import Darwin 
import sys

# ----
# food
# ----

food = Darwin.Species("food")
food.addInstruction("go 0")


# ------
# hopper
# ------

hopper = Darwin.Species("hopper")
hopper.addInstruction("hop")
hopper.addInstruction("go 0")

# -----
# rover
# -----

rover = Darwin.Species("rover")
rover.addInstruction("if_enemy 9")
rover.addInstruction("if_empty 7")
rover.addInstruction("if_random 5")
rover.addInstruction("left")
rover.addInstruction("go 0")
rover.addInstruction("right")
rover.addInstruction("go 0")
rover.addInstruction("hop")
rover.addInstruction("go 0")
rover.addInstruction("infect")
rover.addInstruction("go 0")

# ----
# trap
# ----

trap = Darwin.Species("trap")
trap.addInstruction("if_enemy 3")
trap.addInstruction("left")
trap.addInstruction("go 0")
trap.addInstruction("infect")
trap.addInstruction("go 0")

# ----
# best
# ----

best = Darwin.Species("best")
best.addInstruction("if_enemy 2")
best.addInstruction("hop")
best.addInstruction("infect"

# ----------
# darwin 8x8
# ----------

print("*** Darwin 8x8 ***")

grid = Darwin.Darwin(8, 8)
f1 = Darwin.Creature(food)
h1 = Darwin.Creature(hopper)
h2 = Darwin.Creature(hopper)
h3 = Darwin.Creature(hopper)
h4 = Darwin.Creature(hopper)
f2 = Darwin.Creature(food)

grid.addCreature(f1, 0, 0, 2)
grid.addCreature(h1, 3, 3, 1)
grid.addCreature(h2, 3, 4, 2)
grid.addCreature(h3, 4, 4, 3)
grid.addCreature(h4, 4, 3, 0)
grid.addCreature(f2, 7, 7, 1)

"""
Simulate 5 moves.
Print every grid.
"""

# ----------
# darwin 7x9
# ----------

print("*** Darwin 7x9 ***")

grid = Darwin.Darwin(7, 9)
t1 = Darwin.Creature(trap)
h1 = Darwin.Creature(hopper) 
r1 = Darwin.Creature(rover)
t2 = Darwin.Creature(trap)

grid.addCreature(t1, 0, 0, 3)
grid.addCreature(h1, 3, 2, 2)
grid.addCreature(r1, 5, 4, 1)
grid.addCreature(t2, 6, 8, 0)

"""
Simulate 5 moves.
Print every grid.
"""

# ------------
# darwin 72x72
# without best
# ------------

print("*** Darwin 72x72 without Best ***")
seed(0);

grid = Darwin.Darwin(72, 72)

# 10 Food
f1 = Darwin.Creature(food)
f2 = Darwin.Creature(food)
f3 = Darwin.Creature(food)
f4 = Darwin.Creature(food)
f5 = Darwin.Creature(food)
f6 = Darwin.Creature(food)
f7 = Darwin.Creature(food)
f8 = Darwin.Creature(food)
f9 = Darwin.Creature(food)
f10 = Darwin.Creature(food)

grid.addCreature(f1, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(f2, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(f3, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(f4, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(f5, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(f6, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(f7, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(f8, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(f9, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(f10, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))

# 10 Hopper
h1 = Darwin.Creature(hopper)
h2 = Darwin.Creature(hopper)
h3 = Darwin.Creature(hopper)
h4 = Darwin.Creature(hopper)
h5 = Darwin.Creature(hopper)
h6 = Darwin.Creature(hopper)
h7 = Darwin.Creature(hopper)
h8 = Darwin.Creature(hopper)
h9 = Darwin.Creature(hopper)
h10 = Darwin.Creature(hopper)

grid.addCreature(h1, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(h2, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(h3, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(h4, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(h5, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(h6, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(h7, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(h8, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(h9, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(h10, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))


# 10 Rover
r1 = Darwin.Creature(rover)
r2 = Darwin.Creature(rover)
r3 = Darwin.Creature(rover)
r4 = Darwin.Creature(rover)
r5 = Darwin.Creature(rover)
r6 = Darwin.Creature(rover)
r7 = Darwin.Creature(rover)
r8 = Darwin.Creature(rover)
r9 = Darwin.Creature(rover)
r10 = Darwin.Creature(rover)

grid.addCreature(r1, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(r2, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(r3, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(r4, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(r5, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(r6, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(r7, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(r8, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(r9, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(r10, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))

# Trap
t1 = Darwin.Creature(trap)
t2 = Darwin.Creature(trap)
t3 = Darwin.Creature(trap)
t4 = Darwin.Creature(trap)
t5 = Darwin.Creature(trap)
t6 = Darwin.Creature(trap)
t7 = Darwin.Creature(trap)
t8 = Darwin.Creature(trap)
t9 = Darwin.Creature(trap)
t10 = Darwin.Creature(trap)

grid.addCreature(t1, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(t2, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(t3, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(t4, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(t5, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(t6, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(t7, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(t8, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(t9, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(t10, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))

"""
Simulate 1000 moves.
Print the first 10 grids          (i.e. 0, 1, 2...9).
Print every 100th grid after that (i.e. 100, 200, 300...1000).
"""

# ------------
# darwin 72x72
# with best
# ------------

print("*** Darwin 72x72 with Best ***")
seed(0);

grid = Darwin.Darwin(72, 72)

# 10 Food
f1 = Darwin.Creature(food)
f2 = Darwin.Creature(food)
f3 = Darwin.Creature(food)
f4 = Darwin.Creature(food)
f5 = Darwin.Creature(food)
f6 = Darwin.Creature(food)
f7 = Darwin.Creature(food)
f8 = Darwin.Creature(food)
f9 = Darwin.Creature(food)
f10 = Darwin.Creature(food)

grid.addCreature(f1, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(f2, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(f3, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(f4, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(f5, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(f6, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(f7, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(f8, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(f9, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(f10, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))

# 10 Hopper
h1 = Darwin.Creature(hopper)
h2 = Darwin.Creature(hopper)
h3 = Darwin.Creature(hopper)
h4 = Darwin.Creature(hopper)
h5 = Darwin.Creature(hopper)
h6 = Darwin.Creature(hopper)
h7 = Darwin.Creature(hopper)
h8 = Darwin.Creature(hopper)
h9 = Darwin.Creature(hopper)
h10 = Darwin.Creature(hopper)

grid.addCreature(h1, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(h2, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(h3, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(h4, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(h5, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(h6, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(h7, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(h8, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(h9, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(h10, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))


# 10 Rover
r1 = Darwin.Creature(rover)
r2 = Darwin.Creature(rover)
r3 = Darwin.Creature(rover)
r4 = Darwin.Creature(rover)
r5 = Darwin.Creature(rover)
r6 = Darwin.Creature(rover)
r7 = Darwin.Creature(rover)
r8 = Darwin.Creature(rover)
r9 = Darwin.Creature(rover)
r10 = Darwin.Creature(rover)

grid.addCreature(r1, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(r2, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(r3, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(r4, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(r5, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(r6, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(r7, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(r8, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(r9, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(r10, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))

# Trap
t1 = Darwin.Creature(trap)
t2 = Darwin.Creature(trap)
t3 = Darwin.Creature(trap)
t4 = Darwin.Creature(trap)
t5 = Darwin.Creature(trap)
t6 = Darwin.Creature(trap)
t7 = Darwin.Creature(trap)
t8 = Darwin.Creature(trap)
t9 = Darwin.Creature(trap)
t10 = Darwin.Creature(trap)

grid.addCreature(t1, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(t2, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(t3, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(t4, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(t5, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(t6, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(t7, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(t8, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(t9, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(t10, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))

# Best
b1 = Darwin.Creature(best)
b2 = Darwin.Creature(best)
b3 = Darwin.Creature(best)
b4 = Darwin.Creature(best)
b5 = Darwin.Creature(best)
b6 = Darwin.Creature(best)
b7 = Darwin.Creature(best)
b8 = Darwin.Creature(best)
b9 = Darwin.Creature(best)
b10 = Darwin.Creature(best)

grid.addCreature(b1, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(b2, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(b3, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(b4, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(b5, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(b6, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(b7, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(b8, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(b9, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))
grid.addCreature(b10, random.randrange(0, 72), random.randrange(0, 72), random.randrange(0, 4))

"""
10 Best
Simulate 1000 moves.
Best MUST outnumber ALL other species for the bonus pts.
Print the first 10 grids          (i.e. 0, 1, 2...9).
Print every 100th grid after that (i.e. 100, 200, 300...1000).
"""
