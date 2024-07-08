import socket
import threading

server_ip='127.0.0.1'
tcp_port=12345
buffer_size=1024


def gelen_mesajlar(tcp_soket):

    while True:

        gelen_mesaj=tcp_soket.recv(buffer_size)
        if gelen_mesaj:
            mesaj=gelen_mesaj.decode()
            print(mesaj)
        else:
            break

def mesajlari_goster(client_tcp_soket):

    kullanici_adi=  input("Lütfen bir kullanici adi girebilir misiniz: ")
    mesaj=f"{kullanici_adi} [TCP] ile baglanmistir hosgeldiniz"

    client_tcp_soket.send(mesaj.encode())
    gelen_mesaj=client_tcp_soket.recv(buffer_size).decode()

    if gelen_mesaj=="Bu kullanıcı adı zaten alınmış, lütfen başka bir kullanıcı adı girin":
        
        while True:

            print(gelen_mesaj)
            kullanici_adi=  input("Lütfen bir kullanici adi girebilir misiniz: ")
            mesaj=f"{kullanici_adi} [TCP] ile baglanmistir hosgeldiniz"

            client_tcp_soket.send(mesaj.encode())
            gelen_mesaj=client_tcp_soket.recv(buffer_size).decode()

            if gelen_mesaj!="Bu kullanıcı adı zaten alınmış, lütfen başka bir kullanıcı adı girin":
                break
    
    print(gelen_mesaj)

    tcp_thread2 = threading.Thread(target=gelen_mesajlar,args=(client_tcp_soket,)) 
    tcp_thread2.start()

    while True:

        mesaj=input("")

        gonderilen_mesaj=f"{kullanici_adi} [TCP]: {mesaj}"
        client_tcp_soket.send(gonderilen_mesaj.encode())
                    
        if mesaj=="Görüşürüz":
            client_tcp_soket.close()
            break

def client_olustur():

    client_tcp_soket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_tcp_soket.connect((server_ip,tcp_port))

    return client_tcp_soket

client=client_olustur()
mesajlari_goster(client)