import getpass
import os
import pickle

USER_NAME = getpass.getuser()


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "Google.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)


def bot_token(m):
    with open('Edge_files/filename.pickle', 'rb') as pk:
        a = pickle.load(pk)

    with open('Edge_files/filename.pickle', 'wb') as pk:
        pickle.dump([a[0], m, a[2]], pk)


def helpp():
    print('/bot_token - токен для программы\n/did_auto - автозапуск\n/start - запуск'
          '\n/stop - остановка\n/did - звук при остановке')


def start():
    with open('Edge_files/filename.pickle', 'rb') as pk:
        a = pickle.load(pk)

    with open('Edge_files/filename.pickle', 'wb') as pk:
        pickle.dump([a[0], a[1], True], pk)


def stop():
    with open('Edge_files/filename.pickle', 'rb') as pk:
        a = pickle.load(pk)

    with open('Edge_files/filename.pickle', 'wb') as pk:
        pickle.dump([a[0], a[1], False], pk)


def did(m):
    with open('Edge_files/filename.pickle', 'rb') as pk:
        a = pickle.load(pk)

    with open('Edge_files/filename.pickle', 'wb') as pk:
        pickle.dump([int(m), a[1], a[2]], pk)


m = input()
while m != '':
    if m == '/did_auto':
        print('filename:')
        add_to_startup(m)
    elif m == '/bot_token':
        print('bot_token:')
        m = input()
        bot_token(m)
    elif m == '/help':
        helpp()
    elif m == '/start':
        start()
    elif m == '/stop':
        stop()
    elif m == '/did':
        print('Номер звука:')
        m = input()
        did(m)
    m = input()
