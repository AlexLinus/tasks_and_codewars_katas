#Get the Middle Character
#https://www.codewars.com/kata/get-the-middle-character/
#7 KY For Noobs

def get_middle(s):
    #your code here
    result = ''
    if len(s)%2 == 0:
        result += s[int(len(s)/2)-1:int(len(s)/2)+1]
    else:
        result += s[len(s)//2]
    return result

get_middle("test")  # "es")
get_middle("testing")  # "t")
get_middle("middle")  # "dd")
get_middle("A")  # "A")
get_middle("of")  # "of")