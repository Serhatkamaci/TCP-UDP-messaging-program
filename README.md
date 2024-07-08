Bu çalışmada, TCP ve UDP soketleri kullanarak geliştirilen bir mesajlaşma uygulaması tanıtılmaktadır. Uygulamanın her bir kullanıcısı için özel bir soket oluşumu bulunmaktadır, böylece her kullanıcı kendi shell ekranı üzerinden mesajlaşma imkanı elde etmektedir.

Uygulamanın çalıştırılması için öncelikle Server.py adlı Python dosyasının başlatılması gerekmektedir. Bu dosya çalıştırıldığında, "UDP mesajları dinlemeye hazır..." ve "TCP mesajları dinlemeye hazır..." şeklinde iki bilgilendirme mesajı ekrana yansıyacaktır.

Daha sonra, istenildiği kadar shell ekranı açılarak ClientTCP.py ve ClientUDP.py dosyaları çalıştırılmak suretiyle kullanıcı girişi yapılacaktır. Bu noktada dikkat edilmesi gereken husus, aynı kullanıcı ismiyle birden fazla giriş yapılamayacağıdır. Eğer aynı kullanıcı adı ile giriş yapılmaya çalışılırsa, "Bu kullanıcı adı zaten alınmış, lütfen başka bir kullanıcı adı girin" şeklinde bir uyarı mesajı görüntülenecektir.

Her bir kullanıcı, "Görüşürüz" yazarak sohbetten ayrılabilecektir.


--------------------------------------------------

This study introduces a messaging application developed using TCP and UDP sockets. Each user of the application has a dedicated socket, allowing them to communicate through their own shell screen.

To run the application, the Server.py Python file must be executed first. When this file is run, two informational messages will appear on the screen: "Ready to listen for UDP messages..." and "Ready to listen for TCP messages..."

Subsequently, as many shell screens as desired can be opened to run the ClientTCP.py and ClientUDP.py files for user login. It is important to note that the same username cannot be used for multiple logins. If an attempt is made to log in with a username that is already in use, a warning message saying "This username is already taken, please enter a different username" will be displayed.

Each user can exit the chat by typing "Goodbye."
