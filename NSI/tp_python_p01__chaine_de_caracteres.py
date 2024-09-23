import string
# Ecrire une fonction python qui prend en entrée une chaine 
# de caractères, et qui renvoie le nombre de caractères de
# cette chaine (PUFS).

def count_characters(chain):
    s=0
    for i in chain:
        s+=1
    return f"This chain has {s} characters"

print(count_characters("le poste d'ingénieur en génie civil"))

# Ecrire une fonction python qui prend en entrée deux paramètres:
#   - une chaine de caractères de nom chain,
#   - un caractère de nom char,
# et qui renvoie le nombre d'occurence de char dans chain.  (PUFS)

def count_occurences(chain, char):
    s=0
    for i in chain:
        if i == char:
            s+=1
    return f"The character '{char}' has {s} occurrences in '{chain}' "

print(count_occurences("le poste d'ingénieur en génie civil est très prisé chez les enfants de moins de 9 ans ", "u"))
# Ecrire une fonction python qui prend en entrée une chaine de caractères
# de nom chain, qui ne contient que des voyelles ou des consonnes, et qui 
# renvoie deux listes. 
#   - L'une contiendra les voyelles contenues dans chain,
#   - l'autre les consonnes contenues dans chain.  (PUFS)


    
def is_vowel(char):
    if (char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "y" ):
        return True
    else:
        return False

def is_consonant(char):
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "u", "v", "w", "x", "z"]
    if consonants.count(char) >= 1:
        return True
    else:
        return False

def vowels_and_consonants(chain):
    vowel_list = []
    consonants_list = []
    for i in chain:
            if is_vowel(i):
                vowel_list.append(i)
            elif is_consonant(i):
                consonants_list.append(i)
            else:
                return "Please enter a list of letters"

    return vowel_list, consonants_list

print(vowels_and_consonants("lesamismangentuneglaceetouitonton"))
                
            
# Ecrire un programme python qui prend en entrée une chaine de caractère chain,
# et qui permet de réaliser la tâche suivante:
#   - on demande à l'utilisateur de rentrer la chaine chain,
#   - s'il rentre la bonne chaine alors on affiche un texte de remerciement,
#   - s'il ne rentre pas exactement la chaine attendue alors on lui demande
#     de réessayer...Jusqu'à ce qu'il rentre la bonen chaine. (PUFS)

def check_right_chain (chain):
    
    is_chain = False
    while is_chain == False:
        check = input ("Enter a chain ! ")
        if chain == check:
            is_chain = True
            print ("You entered the right chain !")
        else:
            is_chain = False
            print ("Wrong chain ! Try again")
    

check_right_chain ("loubouloulou")
