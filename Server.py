import socket
import threading

server_ip='127.0.0.1'
udp_port=12346
tcp_port=12345
buffer_size=1024

udp_kullanicilari={}
tcp_kullancilar={}
kullanicilar={}
udp_adress={}


def mesaj_gonder(gelen,mesaj,gelen_baglanti):

    for kullanici in kullanicilar.keys():
        
        baglanti_deger=""
        isim=""

        for baglanti in kullanicilar[kullanici].keys():
                 
            baglanti_deger=baglanti.split(" ")[1] # TCP mi UDP mi
            isim=baglanti.split(" ")[0]

        if gelen_baglanti=="TCP":

            if baglanti_deger=="TCP":
                
                if kullanici!=gelen:
                    isim=isim+" "+"TCP"
                    gonderilecek=gelen+"[TCP]:"+mesaj
                    kullanicilar[kullanici][isim].send(gonderilecek.encode())
            else:
                if kullanici!=gelen:
                    
                    for i in udp_adress.keys():

                        if i==kullanici:
                            isim=isim+" "+"UDP"
                            gonderilecek=gelen+"[TCP]:"+mesaj
                            kullanicilar[kullanici][isim].sendto(gonderilecek.encode(),udp_adress[kullanici])
            
        else:
            if baglanti_deger=="TCP":
                if kullanici!=gelen:
                    isim=isim+" "+"TCP"
                    gonderilecek=gelen+"[UDP]:"+mesaj
                    kullanicilar[kullanici][isim].send(gonderilecek.encode())
            else:
                if kullanici!=gelen:
                    isim=isim+" "+"UDP"
                    gonderilecek=gelen+"[UDP]:"+mesaj
                    kullanicilar[kullanici][isim].sendto(gonderilecek.encode(),udp_adress[kullanici])
              

def udp_dinle(udp_server_soket):

    while True:

        try:
            mesaj,client_adres=udp_server_soket.recvfrom(buffer_size)
            mesaj=mesaj.decode()

            gelen_mesaj=mesaj.split(" ")

            kullanici_adi=gelen_mesaj[0]

            kontrol=""

            for i in mesaj.split(" ")[1:]:

                kontrol+=i

            if kontrol=="[UDP]ilebaglanmistirhosgeldiniz":

                if (kullanici_adi not in tcp_kullancilar) and (kullanici_adi not in udp_kullanicilari):
                    
                    udp_adress[kullanici_adi]=client_adres

                    tutt={}
                    deneme=kullanici_adi+" "+"UDP"
                    tutt[deneme]=udp_server_soket
                    kullanicilar[kullanici_adi]=tutt

                    udp_kullanicilari[kullanici_adi]=mesaj
                    print(mesaj)
                    udp_ekranina_basilacak=f"Hosgeldiniz {kullanici_adi} UDP ile baglisiniz"
                    udp_server_soket.sendto(udp_ekranina_basilacak.encode(),client_adres)

                else:

                    udp_server_soket.sendto("Bu kullanıcı adı zaten alınmış, lütfen başka bir kullanıcı adı girin".encode(),client_adres)
                
            else:

                mesajimiz=gelen_mesaj[2]
                
                mesaj_gonder(kullanici_adi,mesajimiz,"UDP")

                if mesajimiz!="Görüşürüz":

                        udp_kullanicilari[kullanici_adi]=mesajimiz
                        print(mesaj)
                    
                if mesajimiz=="Görüşürüz":
                    print("{} isimli kullanıcı sohbet odasından ayrıldı".format(kullanici_adi))
                    del udp_kullanicilari[kullanici_adi]
                    del kullanicilar[kullanici_adi]
                    break

        except Exception as e:
            continue
            



def tcp_dinle(connection_soket):

    while True:
        try: 
            mesaj=connection_soket.recv(buffer_size).decode()   

            gelen_mesaj=mesaj.split(" ")

            kullanici_adi=gelen_mesaj[0]
            kontrol=""
            
            for i in mesaj.split(" ")[1:]:
                kontrol+=i
            
            if kontrol=="[TCP]ilebaglanmistirhosgeldiniz":
                        
                    if (kullanici_adi not in udp_kullanicilari) and (kullanici_adi not in tcp_kullancilar):
                        
                        tutt={}
                        
                        deneme=kullanici_adi+" "+"TCP"
                        tutt[deneme]=connection_soket
                        kullanicilar[kullanici_adi]=tutt

                        tcp_kullancilar[kullanici_adi]=mesaj
                        print(mesaj)
                        tcp_ekranina_basilacak=f"Hosgeldiniz {kullanici_adi} TCP ile baglisiniz"
                        connection_soket.send(tcp_ekranina_basilacak.encode())

                    else:

                        connection_soket.send("Bu kullanıcı adı zaten alınmış, lütfen başka bir kullanıcı adı girin".encode())

            else:
                
                mesajimizz=gelen_mesaj[2]
                mesaj_gonder(kullanici_adi,mesajimizz,"TCP")

                if mesajimizz!="Görüşürüz": 

                        tcp_kullancilar[kullanici_adi]=mesajimizz
                        print(mesaj)
                    
                if mesajimizz=="Görüşürüz":

                    print("{} isimli kullanıcı sohbet odasından ayrıldı".format(kullanici_adi))
                    del tcp_kullancilar[kullanici_adi]
                    del kullanicilar[kullanici_adi]
                    connection_soket.close()

        except Exception as e:
            continue

def tcp_olustur():

    tcp_server_soket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_soket.bind((server_ip,tcp_port))
    tcp_server_soket.listen(5)
    print("TCP mesajları dinlemeye hazır...")
    while True:
         connection_soket,adres=tcp_server_soket.accept()
         tcp_thread2 = threading.Thread(target=tcp_dinle,args=(connection_soket,)) 
         tcp_thread2.start()

def udp_olustur():
     
    udp_server_soket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_server_soket.bind((server_ip,udp_port))
    print("UDP mesajları dinlemeye hazır...")
    
    while True:
        udp_dinle(udp_server_soket)

def server_baslat():

    udp_thread = threading.Thread(target=udp_olustur)
    tcp_thread = threading.Thread(target=tcp_olustur)

    udp_thread.start()
    tcp_thread.start()

    udp_thread.join()
    tcp_thread.join()

server_baslat()    