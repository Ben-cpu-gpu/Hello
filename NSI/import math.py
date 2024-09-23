# import math

# def exo_1():
#     a = 12
#     a *= 3
#     a -= 17
#     a **= 4
#     a /= 5
#     a += 23
#     a = math.sqrt(a)
#     print (f"Le résultat final est: {a} ")

# exo_1()

# # Exercice 
# def exo_2():
#     a = float(input("Entrer un nombre quelconque : "))
#     b = a
#     a *= 2
#     a *= 23
#     a /= 3
#     a **= 2
#     a +=25
#     a = a = math.sqrt(a)
#     print (f"Pour la valeur de {b} Le résultat final est: {a} ")

# exo_2()

# def is_even (n):
#     if n % 2 == 0:
#         return True
#     else:
#         n % 2 == 0
#         return not (n % 2 == 1)

# def is_odd (n):
#     return not (is_even (n))

def b3 (b1, b2):
    if b1 == True:
        if b2 == True:
            return True
        else:
            return False
    else:
        return False