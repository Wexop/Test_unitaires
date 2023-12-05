import time

hour = time.localtime().tm_hour

time = 'jour'
if hour > 18:
    time = 'night'


def getHello():
    if time == 'jour':
        return 'Bonjour !'
    elif time == 'night':
        return 'Bonsoir !'


def getGoodBye():
    if time == 'jour':
        return 'Bonne journée !'
    elif time == 'night':
        return 'Bonne soirée !'


print(getHello())


def est_palindrome(mot):
    mot = mot.lower()
    mot = mot.replace(" ", "")
    return mot == mot[::-1]


sentence = input('Ecrivez quelque chose : ')
print(sentence)
if (est_palindrome(sentence)):
    print('Bien dit !')

print(getGoodBye())
