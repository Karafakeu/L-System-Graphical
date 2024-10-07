import stringInterpreter, turtleGraphical

def main():
    colorCodes = {"0": "Black", "1": "Gray", "2": "Brown", "3": "Pink", "4": "Purple", "5": "Blue", "6": "Green", "7": "Yellow", "8": "Orange", "9": "Red"}

    choice = input("Do you want to see the basic commands of the graphical first (y/n)? ")
    while choice not in ["y", "n"]:
        choice = input("Please choose either y or n. ")

    if choice == "y":
        print("These are the following commands:")
        print("+  = rotates turtle (the graphical) to the right by the angle")
        print("-  = rotates turtle (the graphical) to the left by the angle")
        print("[  = stores the position and the heading of turtle (the graphical) to a stack")
        print("]  = restores the position and the heading of turtle (the graphical) from the top of the stack")
        print("C# = Changes color of the pen, to the color based on the color code replaced in place of '#'")
        print("Any other letter or symbol will be disregarded and represented as movement forward\n")
        print("Color codes:")
        for code in colorCodes:
            if colorCodes[code] == "Black":
                print(f"{code} - {colorCodes[code]} (default)")
                continue
            print(f"{code} - {colorCodes[code]}")
        print()

    # number of iterations
    try:
        iterations = int(input("What is the number of iterations? "))
    except:
        print("Input the correct form please!")
        iterations = "incorrect."
    while type(iterations) != int or iterations < 1:
        if iterations < 1:
            print("The input must be a positive, non-zero integer.")
        try:
            iterations = int(input("What is the number of iterations? "))
        except:
            print("Input the correct form please!")
            iterations = "incorrect."
    
    # number of angle
    try:
        angle = int(input("What is the angle of the turning? "))
    except:
        print("Input the correct form please!")
        angle = "incorrect."
    while type(angle) != int:
        try:
            angle = int(input("What is the angle of the turning? "))
        except:
            print("Input the correct form please!")
            angle = "incorrect."
    
    # axiom
    axiom = input("What is the axiom? ")

    # number of rules
    try:
        ruleNumber = int(input("What is the number of rules to be inputed? "))
    except:
        print("Input the correct form please!")
        ruleNumber = "incorrect."
    while type(ruleNumber) != int:
        try:
            ruleNumber = int(input("What is the number of rules to be inputed? "))
        except:
            print("Input the correct form please!")
            ruleNumber = "incorrect."

    rules = {}

    # the first rule so it can have a different message
    rule = input("What is the first rule? Remember, it must contain an equals sign!\n")
    while not 0 < rule.count("=") < 2:
        rule = input("There must be an equals sign!!!\n")
    rules[rule.split("=")[0]] = rule.split("=")[1]

    for i in range(ruleNumber - 1):
        rule = input("What is the next rule? Remember, it must contain an equals sign!\n")
        while not 0 < rule.count("=") < 2:
            rule = input("There must be an equals sign!!!\n")
        rules[rule.split("=")[0]] = rule.split("=")[1]

    # we have number of iterations, angle, axiom and rules
    # type iterations: int
    # type angle: int
    # type axiom: str
    # type rules: dict, key = to be replaced, value is the new string

    # create the L-system string
    LString = stringInterpreter.interpret(iterations, axiom, rules)
    print(f"The L-System string is: {LString}")

    # draw the L-system string
    turtleGraphical.drawSystem(LString, angle, 10, colorCodes)

if __name__ == "__main__":
    main()