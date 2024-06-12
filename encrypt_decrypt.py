from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

KEY = os.urandom(32)  # Use uma chave consistente em produção
IV = os.urandom(16)   # Use um IV consistente em produção


def encrypt_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()

    cipher = Cipher(algorithms.AES(KEY), modes.CFB(IV),
                    backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data) + encryptor.finalize()

    with open(file_path, 'wb') as f:
        f.write(IV + encrypted_data)


def decrypt_file(file_path):
    with open(file_path, 'rb') as f:
        iv = f.read(16)
        encrypted_data = f.read()

    cipher = Cipher(algorithms.AES(KEY), modes.CFB(iv),
                    backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    with open(file_path, 'wb') as f:
        f.write(decrypted_data)


def encrypt_file(file_path):
    # Implementação da função de criptografia aqui
    pass


def decrypt_file(file_path):
    # Implementação da função de descriptografia aqui
    pass
