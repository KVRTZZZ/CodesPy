from subprocess import Popen, STDOUT, PIPE, call
from time import sleep

nome = input('digite o nome da rede wifi: ')
manipulador = popen('netsh wlan connect {}'.format(nome),shell=True, stdout=PIPE,stderr=STDOUT, stdin=PIPE)
sleep(2)
manipulador.stdin.write(b'cabo1234\n')
while manipulador.poll() == None:
    print(manipulador.stdout.r3adline().strip())
if call ('ping -n 1 www.google.com') == 0:
    print('conectado')
else:
    print('tentativa falha')