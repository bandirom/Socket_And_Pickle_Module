import pickle
import socket

a = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1025))
s.listen(5)

List = [1,2,3,4,5]
Dictinary = {1:"Client", 2 : "Server", 3: "Maks", 4: "Nazarii", 5: "unknow", 6: "incognito"}

while True:
    clt, adr = s.accept()
    print(f'Connection to {adr} established')
    mymsg = pickle.dumps(Dictinary)
    mymsg = bytes(f'{len(mymsg):<{a}}', "utf-8") + mymsg
    clt.send(mymsg)

