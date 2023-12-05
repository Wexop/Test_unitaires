import time

hour = time.localtime().tm_hour

time = 'jour'
if time > 18:
    time = 'night'

if time == 'jour':
    print('Bonjour !')
elif time == 'night':
    print('Bonsoir !')


