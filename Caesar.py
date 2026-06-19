def encrypt(text, shift):
    result=""
    for char in text:
        #Handle uppercase letters
        if char.isupper():
            result += chr((ord(char)- 65 + shift) % 26 + 65)
        #Handle Lowercase letters 
        elif char.islower():   
            result += chr ((ord(char)- 97 + shift) % 26 + 97)
            #Leave spaces and punctuation alone
        else:
            result += char
    return result
        
def  decrypt(text, shift):
    result=""
    for char in text:
        #Handle uppercase letters(subtract shift)
        if char.isupper():
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        #Handle Lowercase letters (subtract shift)
        elif char.islower():   
            result += chr((ord(char) - 97 - shift) % 26 +97)
            #Leave spaces and punctuation alone
        else:
            result+=char
    return result
        
# test program
secret_key = 4
original_message=" I am from pakistan."

#run Encryption
scrambled_text =encrypt(original_message,secret_key)
print("1,ENCRYPTED CTPHERTEXT:")
print(scrambled_text)
print("-"*30)

#run  Decryption
restored_text =decrypt(scrambled_text,secret_key)
print("2. DECRYPTED PLANETEXT(REVERSED):")
print(restored_text)