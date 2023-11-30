# Importando as bibliotecas necessárias
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Função de criptografia AES
def encrypt_AES(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = cipher.iv
    return ct_bytes, iv

#Função de descriptografia AES
def decrypt_AES(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return pt

#Função principal e execução
def main():
    key_word = input("Digite a palavra a ser usada como chave de criptografia (de 2 a 32 caracteres): ").encode('utf-8')
    key_length = len(key_word)
    if key_length < 2 or key_length > 32:
        raise ValueError("O comprimento da chave deve estar entre 2 e 32 bytes.")

    # Preencha a chave para ter 32 bytes (256 bits)
    padded_key = key_word + b' ' * (32 - key_length)
    
    data = b'Mensagem secreta criptografada'
    
   

    encrypted_data, iv = encrypt_AES(data, padded_key)
    decrypted_data = decrypt_AES(encrypted_data, padded_key, iv)

    print(f"Dados criptografados: {encrypted_data}")
    print(f"Dados descriptografados: {decrypted_data}")
    print ('A mensagem escrita foi:',key_word)

if __name__ == '__main__':
    main()
