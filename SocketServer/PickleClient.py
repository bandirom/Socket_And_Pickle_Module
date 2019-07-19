import pickle
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1025))

a = 10
while True:
    completeInfo = b''
    rec_msg = True
    while True:
        mymsg = s.recv(16)
        if rec_msg:
            print(f"The len message of message = {mymsg[:a]}")
            x = int(mymsg[:a])
            rec_msg = False
        completeInfo += mymsg
        if len(completeInfo)-a == x:
            print("Recieved the complete info")
            print(completeInfo[a:])
            m = pickle.loads(completeInfo[a:])
            print(m)
            rec_msg = True
            completeInfo = b''
    print(completeInfo)


