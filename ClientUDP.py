import socket
import threading

server_ip='127.0.0.1'
udp_port=12346
buffer_size=1024


def gelen_mesajlar(udp_soket):

    while True:

        gelen_mesaj,server_adres=udp_soket.recvfrom(buffer_size)
        if gelen_mesaj:
            mesaj=gelen_mesaj.decode()
            print(mesaj)
        else:
            break

def client_olustur():

    client_udp_soket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    return  client_udp_soket   

client=client_olustur()


def mesajlari_goster(client_udp_soket):

    kullanici_adi=  input("Lütfen bir kullanici adi girebilir misiniz: ")
    mesaj=f"{kullanici_adi} [UDP] ile baglanmistir hosgeldiniz"

    client_udp_soket.sendto(mesaj.encode(),(server_ip,udp_port))
    gelen_mesaj,server_adres=client_udp_soket.recvfrom(buffer_size)
    gelen_mesaj=gelen_mesaj.decode()


    if gelen_mesaj=="Bu kullanıcı adı zaten alınmış, lütfen başka bir kullanıcı adı girin":
        
        while True:

            print(gelen_mesaj)
            kullanici_adi=  input("Lütfen bir kullanici adi girebilir misiniz: ")
            mesaj=f"{kullanici_adi} [UDP] ile baglanmistir hosgeldiniz"

            client_udp_soket.sendto(mesaj.encode(),(server_ip,udp_port))
            gelen_mesaj,server_adres=client_udp_soket.recvfrom(buffer_size)
            gelen_mesaj=gelen_mesaj.decode()

            if gelen_mesaj!="Bu kullanıcı adı zaten alınmış, lütfen başka bir kullanıcı adı girin":
                break

    print(gelen_mesaj)

    tcp_thread2 = threading.Thread(target=gelen_mesajlar,args=(client_udp_soket,)) 
    tcp_thread2.start()


    while True:
            
        mesaj=input("")

        gonderilen_mesaj=f"{kullanici_adi} [UDP]: {mesaj}"
        client_udp_soket.sendto(gonderilen_mesaj.encode(),(server_ip,udp_port))

        if mesaj=="Görüşürüz":
            client_udp_soket.close()
            break

mesajlari_goster(client)