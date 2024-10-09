# L-Systems Graphical Representation
A program that takes the basic parameters of a generic L-System (based on the inputs below), and creates the graphical representation of that L-System using turtle in python. 

To download turtle on windows, use:
```bash 
pip install turtle
```

## Inputs
The program itself, when ran using main.py, will ask (in terminal) for several inputs. Firstly, it asks if you want the summary of the graphical rules, which can also be seen under. It then asks the following:
* Number of iterations: non-zero integer, representing the number of iterations for the L-System string function
* Angle of rotation: integer between 0 to 360, representing the angle turtle will rotate when it is told to do so.
* Axiom: string, the axiom (starting symbol or symbols) for the L-System
* Number of rules: non zero-integers, representing the number of rules the L-System will have. This is mainly for making the whole system easier to code.
* Rules: strings, in the format of {to be replaced}={new string}. For example, the rule 'X=X+X' will replace X with X+X.
* Randomly: bool (inputed as y or n by the user), if you want the angles to be randomized or not (they are randomized by around +-10%)

## Graphical Rules
**These are the following commands:**

* "+"  = rotates turtle (the graphical) to the right by the angle
* "-"  = rotates turtle (the graphical) to the left by the angle
* "["  = stores the position and the heading of turtle (the graphical) to a stack
* "]"  = restores the position and the heading of turtle (the graphical) from the top of the stack
* C# = Changes color of the pen, to the color based on the color code replaced in place of '#'
* Any other letter or symbol will be disregarded and represented as movement forward

**Color codes:**
* 0 - Black (default)
* 1 - Gray
* 2 - Brown
* 3 - Pink
* 4 - Purple
* 5 - Blue
* 6 - Green
* 7 - Yellow
* 8 - Orange
* 9 - Red

## Limitations
The only limitation so far found is that the turtle takes a long time to draw the shape. While turtle is set to speed of 9999, the algorithm still has to decide which move to make for the turtle for each command in the L-System string, which is what makes the time loss.

## Flow of the program
Firtsly, the program asks for the inputs from the user inside the terminal. These are described above. 

Then, it takes these inputs and creates a L-System string, which the program also prints to the terminal for the user (I added this mainly for debugging but I can see it being helpful to other areas). 

Then, it goes to drawing the graphical. Firstly, initializes the turtle and screen from the library, and then draws the graphical based on the Graphical rules mentioned above. Lastly, it scales the screen based on the size of the graphical, so that it will always fit perfectly on the turtle screen window.
