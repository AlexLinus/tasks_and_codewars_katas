#Correct the mistakes of the character recognition software
# 8Ky for noobs

def correct(string):
    mistakes = {'5': 'S', '0': 'O', '1': 'I'}
    result = ''
    for letter in string:
        if letter not in mistakes:
            result += letter
        else:
            result += mistakes[letter]
    print(result)
    return result

def correct2(string):
    return string.replace('1','I').replace('0','O').replace('5','S')

correct("L0ND0N") # "LONDON"
correct("DUBL1N") #"DUBLIN"
correct("51NGAP0RE") #"SINGAPORE"
correct("BUDAPE5T") #"BUDAPEST"
correct("PAR15") #"PARIS"
