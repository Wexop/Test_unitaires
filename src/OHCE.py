import time

hour = time.localtime().tm_hour
lang = 'fr'  # OU 'en'

time = 'jour'
if hour > 18:
    time = 'night'


def getHello():
    if time == 'jour':
        if lang == 'fr':
            return 'Bonjour !'
        else:
            return 'Hello !'
    elif time == 'night':
        if lang == 'fr':
            return 'Bonsoir !'
        else:
            return 'Good evening !'


def getGoodBye():
    if time == 'jour':
        if lang == 'fr':
            return 'Bonne journée !'
        else:
            return 'Have a good day !'
    elif time == 'night':
        if lang == 'fr':
            return 'Bonne soirée !'
        else:
            return 'Have a good evening !'


print(getHello())


def est_palindrome(mot):
    mot = mot.lower()
    mot = mot.replace(" ", "")
    return mot == mot[::-1]


def miroir(texte):
    return texte[::-1]


inputSentence = 'Ecrivez quelque chose : '
if lang != 'fr':
    inputSentence = 'Write something : '

sentence = input(inputSentence)
print(miroir(sentence))


def printPalindrome(string):
    if est_palindrome(string):
        if lang == 'fr':
            return 'Bien dit !'
        else:
            return 'Well said !'


print(printPalindrome(sentence))

print(getGoodBye())
