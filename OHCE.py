import time

hour = time.localtime().tm_hour
lang = 'en'  # OU 'en'

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
if lang != inputSentence:
    inputSentence = 'Write something : '

sentence = input(inputSentence)
print(miroir(sentence))
if est_palindrome(sentence):
    if lang == 'fr':
        print('Bien dit !')
    else:
        print('Well said !')

print(getGoodBye())
