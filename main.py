
def encrypt(msg):
    words = msg.split(" ")
    encrypt_msg = []
    for word in words:
        if(len(word)>3):
            r1 = "tyi"
            r2 = "nxl"
            tempword = r1+ word[1:]+ word[0]+ r2
            encrypt_msg.append(tempword)
        else:
            encrypt_msg.append(word[::-1]) # to reverse the element of the list

    encrypt_msg = " ".join(encrypt_msg)
    return encrypt_msg
def decrypt(msg):
    words = msg.split(" ")
    decrypt_msg = []
    for word in words:
        if(len(word)>3):
            tempword = word[-4]+ word[3:-4]     # it is the subtitute of the below two lines, but it is complecated to understand.
            # tempword = word[3:-3]  # Strip "tyi" from the start and "nxl" from the end
            # tempword = tempword[-1]+ tempword[:-1]  # Move the last character to the front
            decrypt_msg.append(tempword)
        else:
            decrypt_msg.append(word[::-1]) # to reverse the element of the list

    decrypt_msg = " ".join(decrypt_msg)
    return decrypt_msg

def salect(msg):            #will ask to encrypt or decrypt the message
    option = int(input("To Encrypt the msg please enter 1\nTo Dycrypt the msg please enter 0  "))
    if(option == 1):
        message = (encrypt(msg))
    elif(option == 0):
        message = (decrypt(msg))
    else:
        message = "Envalid option. Please enter 1 for encryption or 0 for decryption."

    return message

def run(msg):
    print(salect(msg))   


# if("__name__" == "__main__"):

msg = input("Enter your message: ")
run(msg)

# option = int(input("To Encrypt the msg please enter 1\nTo Dycrypt the msg please enter 0  "))
# if(option == 1):
#     print(encrypt(msg))
# elif(option == 0):
#     print(decrypt(msg))
# else:
#     message = "Envalid option. Please enter 1 for encryption or 0 for decryption."
# # print(encrypt(msg))
# # print(decrypt(encrypt(msg)))