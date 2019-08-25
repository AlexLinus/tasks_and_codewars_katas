def is_merge(s, part1, part2):
    return True if list(sorted(list(s))) == list(sorted([letter for letter in part1+part2])) else False

#is_merge('codewars', 'code', 'wars')
#is_merge('codewars', 'cdw', 'oears')
#is_merge('codewars', 'cod', 'wars')
print(is_merge('codewars', 'cwdr', 'oeas'))