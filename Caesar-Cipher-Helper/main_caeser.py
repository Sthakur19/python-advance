class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encode(self, word):
        '''function will retrun the encoded/encrypted word'''
        encoded_caesar_cipher_text = ""
        for letter in word:
            #isalpha() will check if all characters in word are alphabet letters 
            if letter.isalpha():
                if letter.isupper():
                    #ord() takes character as argument and returns as integer unicode point value  
                    #chr() takes integer as argument and returns as character at the unicode point value 
                    encoded_letter = chr((ord(letter) - ord('A') + self.shift) % 26 + ord('A'))
                else:
                    encoded_letter = chr((ord(letter) - ord('a') + self.shift) % 26 + ord('a'))
                encoded_caesar_cipher_text += encoded_letter
            else:
                encoded_caesar_cipher_text += letter
        # print(encoded_caesar_cipher_text)
        return encoded_caesar_cipher_text

    def decode(self, word):
        '''function will retrun the decoded/dcrypted word'''
        decoded_caesar_cipher_text = ""
        for letter in word:
            if letter.isalpha():
                if letter.isupper():
                    decoded_letter = chr((ord(letter) - ord('A') - self.shift) % 26 + ord('A'))
                else:
                    decoded_letter = chr((ord(letter) - ord('a') - self.shift) % 26 + ord('a'))
                decoded_caesar_cipher_text += decoded_letter
            else:
                decoded_caesar_cipher_text += letter
        # print(decoded_caesar_cipher_text)
        return decoded_caesar_cipher_text


c = CaesarCipher(5)
encoded = c.encode('chess').upper()
print(encoded)  # Output: HMJXX

decoded = c.decode('BFKKQJX').upper()
print(decoded)  # Output: WAFFLES
