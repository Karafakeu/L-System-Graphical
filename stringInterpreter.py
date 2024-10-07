def interpret(iters, axiom, rules):
    newString, temp = axiom, ""
    # run iters times
    for i in range(iters):
        # go through each letter of the current string
        for letter in newString:
            # if letter in rules, replace the letter with the rule
            if letter in rules.keys():
                temp += rules[letter]
            else: # if not, just add the letter (important for +, -, [, ], maybe colors)
                temp += letter

        # important so the iterations run on the same string and add to it later
        newString = temp
        temp = ""
    
    return newString