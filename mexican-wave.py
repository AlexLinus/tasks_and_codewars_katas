#VAR1
def wave(str):
    result = [str[0:i] + str[i].upper() + str[i+1:] for i in range(0, len(str)) if str[i] != ' ']
    return result
    # Code here

#VAR2
def wave2(str):
    result = []
    if str:
        result.append(str.title())
        for i in range(0, len(str)):
            if str[i] != ' ':
                result.append(str[0:i] + str[i].upper() + str[i+1:])
    print(result)
    return result
    # Code here

wave2("hello")  # ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
wave("codewars")  # ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
wave("")  # []
wave("two words")  # ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
wave(" gap ")  # [" Gap ", " gAp ", " gaP "]