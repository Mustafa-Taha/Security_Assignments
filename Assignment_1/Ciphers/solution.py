import sys
import re

m = 26
text = ""
result = ""


# ***********************************************************************************************************************
def terminate():
    print(
        "<<Warning>> : Invalid format\n"
        "<--HELP-->\n"
        "solution.py <cipher> <mode> <inputfile>  <outputfile> (<a> <b>|<b>|<key>) \n"
        "-> encryption keys according to chosen cipher ")
    sys.exit()


def get_file_path(argv):
    x = argv[2].split(".")
    y = argv[3].split(".")
    x[1] = "txt"
    y[1] = "txt"
    argv[2] = ".".join(x)
    argv[3] = ".".join(y)


def formatCheck(argv):
    # print(argv)
    if (len(argv) == 5):
        if (bool(re.search("(shift|caesar|cae|shi)", argv[0], re.I))):
            if (bool(re.search("(enc|encrypt)", argv[1], re.I))) and (
                    bool(re.search("\w+.(txt|text)[\s\t]+\w+.(txt|text)$", " ".join(argv[2:4]), re.I))) and (
                    bool(re.search("\d+", str(argv[-1]), re.I))):
                get_file_path(argv)
                return 1
            elif (bool(re.search("(dec|decrypt)", argv[1], re.I))) and (
                    bool(re.search("\w+.(txt|text)[\s\t]+\w+.(txt|text)$", " ".join(argv[2:4]), re.I))) and (
                    bool(re.search("\d+", str(argv[-1]), re.I))):
                get_file_path(argv)
                return 2
            else:
                terminate()
        elif (bool(re.search("vigenere|vig", argv[0], re.I))):
            if (bool(re.search("(enc|encrypt)", argv[1], re.I))) and (
                    bool(re.search("\w+.(txt|text)[\s\t]+\w+.(txt|text)$", " ".join(argv[2:4]), re.I))) and (
                    bool(re.search("\w+", argv[-1], re.I))):
                get_file_path(argv)
                return 5
            elif (bool(re.search("(dec|decrypt)", argv[1], re.I))) and (
                    bool(re.search("\w+.(txt|text)[\s\t]+\w+.(txt|text)$", " ".join(argv[2:4]), re.I))) and (
                    bool(re.search("\w+", argv[-1], re.I))):
                get_file_path(argv)
                return 6
            else:
                terminate()

        else:
            terminate()

    elif (len(argv) == 6):
        if (bool(re.search("(affine|aff)", argv[0], re.I))):
            if (bool(re.search("(enc|encrypt)", argv[1], re.I))) and (
                    bool(re.search("\w+.(txt|text)[\s\t]+\w+.(txt|text)$", " ".join(argv[2:4]), re.I))) and (
                    bool(re.search("\d+[\s\t]+\d+", " ".join(map(str, argv[4:6])), re.I))):
                get_file_path(argv)
                return 3
            elif (bool(re.search("(dec|decrypt)", argv[1], re.I))) and (
                    bool(re.search("\w+.(txt|text)[\s\t]+\w+.(txt|text)$", " ".join(argv[2:4]), re.I))) and (
                    bool(re.search("\d+[\s\t]+\d+", " ".join(map(str, argv[4:6])), re.I))):
                get_file_path(argv)
                return 4
            else:
                terminate()
    else:
        if (len(argv) > 6 or len(argv) < 5) | (len(argv) == 1 and (argv[0] == "-h" or argv[0] == "-H")):
            terminate()


# ***********************************************************************************************************************
# ===================================================Casear_Cipher=======================================================
def encoding_message(msg, shift):  # encryption
    cipher = ""
    for c in msg:
        if c.isalpha():
            if c == c.upper():
                cipher += chr(((ord(c) - ord('A') + shift) % m) + ord('A'))
            else:
                cipher += chr(((ord(c) - ord('a') + shift) % m) + ord('a'))

        else:  # else simply append space character
            cipher += c
    return cipher


# -----------------------------------------------------------------------------------------------------------------------
def decoding_message(cipher, shift):  # decryption
    msg = ""
    b_inv = m - (shift % m)
    for c in cipher:
        if c.isalpha():
            if c == c.upper():
                msg += chr(((ord(c) - ord('A') + b_inv) % m) + ord('A'))
            else:
                msg += chr(((ord(c) - ord('a') + b_inv) % m) + ord('a'))
        else:  # else simply append space character
            msg += c
    return msg


# ===================================================Affine_Cipher=======================================================
def input_check_a(a):  # check if it has multiplicative inverse
    a_inv = 0
    flag = 0

    for i in range(m):
        flag = (a * i) % 26
        # Check if (a * i) % 26 == 1,
        # then i will be the multiplicative inverse of a
        if flag == 1:
            a_inv = i
            break
    if flag == 1:
        return a_inv
    else:
        print(
            "<<<<<<<<<<<<<<<<<<<<<<<<"
            "--Given <a> parameter doesn't have multiplicative inverse--"
            ">>>>>>>>>>>>>>>>>>>>>>>>>>>")
        sys.exit()


# -----------------------------------------------------------------------------------------------------------------------
def encrypt_message(msg, a, b):  # encryption
    # Cipher Text initially empty
    input_check_a(a)
    cipher = ""
    for c in msg:
        if c.isalpha():
            if c == c.upper():
                cipher += chr((((a * (ord(c) - ord('A'))) + b) % 26) + ord('A'))
            else:
                cipher += chr((((a * (ord(c) - ord('a'))) + b) % 26) + ord('a'))
        else:  # else simply append space character
            cipher += c
    return cipher


# -----------------------------------------------------------------------------------------------------------------------
def decrypt_cipher(cipher, a_inverse, b):  # decryption a_inverse is the multiplicative inverse of a
    if a_inverse == 0:
        print(
            "<<<<<<<<<<<<<<<<<<<<<<<<"
            "--Given a parameter doesn't have multiplicative inverse--"
            ">>>>>>>>>>>>>>>>>>>>>>>>>>>")
        sys.exit()
    msg = ""
    b_inv = m - (b % m)
    # flag = 0
    # #Find a^-1 (calcu multiplicative inverse)
    # for i in m:
    #     flag = (a * i) % 26
    #     # Check if (a * i) % 26 == 1,
    #     # then i will be the multiplicative inverse of a
    #     if flag == 1:
    #         a_inv = i
    #         break
    # if flag == 1:
    #     return a_inv
    # else:
    #     return 0
    for c in cipher:
        if c.isalpha():
            if c == c.upper():
                msg += chr(((a_inverse * (ord(c) + ord('A') + b_inv)) % 26) + ord('A'))
            else:
                msg += chr(((a_inverse * (ord(c.upper()) + ord('A') + b_inv)) % 26) + ord('A')).lower()
        else:
            msg += c
    return msg


# =================================================Vigenere_Cipher=======================================================
# def generateKey(string, key):
#     key_ = ""
#     if len(string) == len(key):
#         return key.upper()
#     else:
#         for i in range(len(string)):
#             key_ += (key[i % len(key)]).upper()
#     return key_


# -----------------------------------------------------------------------------------------------------------------------
def cipherText(string, key):
    cipher_text = ""
    j = 0
    for i in range(len(string)):
        if string[i].isalpha():
            if string[i] == string[i].upper():
                cipher_text += chr(((ord(string[i]) + ord(key[(j % len(key))].upper())) % 26) + ord('A'))
                j += 1
            else:
                cipher_text += chr(
                    ((ord(string[i].upper()) + ord(key[(j % len(key))].upper())) % 26) + ord('a')).lower()
                j += 1
        else:
            cipher_text += string[i]

    return cipher_text


# -----------------------------------------------------------------------------------------------------------------------
def originalText(cipher_text, key):
    orig_text = ""
    j = 0
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            if cipher_text[i] == cipher_text[i].upper():
                orig_text += chr(((ord(cipher_text[i]) - ord(key[(j % len(key))].upper())) % 26) + ord('A'))
                j += 1
            else:
                orig_text += chr(
                    ((ord(cipher_text[i].upper()) - ord(key[(j % len(key))].upper())) % 26) + ord('a')).lower()
                j += 1
        else:
            orig_text += cipher_text[i]

    return orig_text


# =======================================================================================================================
# ***********************************************************************************************************************
def main(argv):
    process = formatCheck(argv)
    input = open(argv[2], "r")
    output = open(argv[3], "w")
    text = input.read()
    input.close()

    if process == 1:  # Shift Encrypt
        result = encoding_message(text, int(argv[-1]))
    elif process == 2:  # Shift Decrypt
        result = decoding_message(text, int(argv[-1]))
    elif process == 3:  # Affine Encrypt
        result = encrypt_message(text, int(argv[-2]), int(argv[-1]))
    elif process == 4:  # Affine Decrypt
        result = decrypt_cipher(text, input_check_a(int(argv[-2])), int(argv[-1]))
    elif process == 5:  # Vigenere Encrypt
        result = cipherText(text, argv[-1])
    elif process == 6:  # Vigenere Decrypt
        result = originalText(text, argv[-1])
    else:
        terminate()
        sys.exit()
    print("Result :>>\n" + result)
    output.write(result)
    output.close()


if __name__ == "__main__":
    main(sys.argv[1:])
