#7KY for noobs
#Complementary DNA
#https://www.codewars.com/kata/complementary-dna/


def DNA_strand(dna):
    dna_dict = {'T': 'A', 'A': 'T', 'G': 'C', 'C': 'G'}
    return  ''.join([dna_dict[letter] for letter in dna])

DNA_strand("AAAA")#"TTTT"
DNA_strand("ATTGC")# "TAACG"
DNA_strand("GTAT") #"CATA"
