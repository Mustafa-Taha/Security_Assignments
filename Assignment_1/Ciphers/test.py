import re
# print((bool(re.search("\w*.(txt|text)[\s\t]*\w*.(txt|text)", "inpf5Ut.txt ov56fdsutput.text", re.I))))
# print((bool(re.search("\d*", "55", re.I))))
# print((bool(re.search("\d*[\s\t]*\d*", "55", re.I))))
# print((bool(re.search("\w+", "55", re.I))))

# print(bool(re.search("enc|encrypt", "encrypt", re.I)))
# print(bool(re.search("\w+.(txt|text)[\s\t]+\w+.(txt|text)$","input.text output.text" , re.I)))
# print(bool(re.search("\d+", str(55), re.I)))
# ls =["encrypt", "input.text", "output.text", 5, 6]
# print((bool(re.search("\d+[\s\t]+\d+"," 5  6 ", re.I))))
# print(' '.join(map(str, ls[3:5])))
#
# ll =["encrypt", "input.text", "output.text", 5, 6]
# # ll=str(ll)
# # import re
# # print((bool(re.search("enc|encrypt", ll[0], re.I))) and (bool(re.search("\w+.(txt|text)[\s\t]+\w+.(txt|text)$", " ".join(ll[1:3]), re.I))) and (bool(re.search("\d+[\s\t]+\d+", " ".join(str(ll[3:5])), re.I))))
# print((bool(re.search("(enc|encrypt)", ll[0], re.I))) and (bool(re.search("\w+.(txt|text)[\s\t]+\w+.(txt|text)$", " ".join(ll[1:3]), re.I))) and (bool(re.search("\d+[\s\t]+\d+", ' '.join(map(str, ll[3:5])), re.I))))
# print((bool(re.search("(enc|encrypt)", ll[0], re.I))) and (bool(re.search("\w+.(txt|text)[\s\t]+\w+.(txt|text)$", " ".join(ll[1:3]), re.I))) and (bool(re.search("\w+", ll[-1], re.I))))
# s = [1,2,3,4,5,6]
# print(s[-1])
# print(s[2:3])
# print(s[2:4])
import sys, getopt, re

print("MegaMore".upper())
# def main(argv):
#     print argv.__str__()
#     # if(len(argv) > 7 or len(argv) < 6) :
#     #     print("solution.py <cipher> <mode> <inputfile>  <outputfile> (<a> <b>|<b>|<key>) ->
#     encryption keys according to chosen cipher ")
#
# if __name__ == "__main__":
#     main(sys.argv[1:])
m = 26

#
# def encoding_message(msg, shift):  # encryption
#     cipher = ""
#     for c in msg:
#         if c.isalpha():
#             if c == c.upper():
#                 cipher += chr(((ord(c) - ord('A') + shift) % m) + ord('A'))
#             else:
#                 cipher += chr(((ord(c) - ord('a') + shift) % m) + ord('a'))
#
#         else:  # else simply append space character
#             cipher += c
#     return cipher
#
#
# # --------------------------------------------------------------------------------------
# def decoding_message(cipher, shift):  # decryption
#     msg = ""
#     b_inv = m - (shift % m)
#     for c in cipher:
#         if c.isalpha():
#             if c == c.upper():
#                 msg += chr(((ord(c) - ord('A') + b_inv) % m) + ord('A'))
#             else:
#                 msg += chr(((ord(c) - ord('a') + b_inv) % m) + ord('a'))
#         else:  # else simply append space character
#             msg += c
#     return msg
#
#
# # --------------------------------------------------------------------------------------
# print(encoding_message("MegaMore_Gonna @Drive $the %world ^to Madness+_+)+_(_(_&*&^(!*&@%<>", 5))
# print(decoding_message(encoding_message("MegaMore_Gonna @Drive $the %world ^to Madness+_+)+_(_(_&*&^(!*&@%<>", 5), 5))
#
#
# # ------------------------------------------------------------------------------------------
# def encrypt_message(msg, a, b):  # encryption
#     # Cipher Text initially empty
#     cipher = ""
#     for c in msg:
#         if c.isalpha():
#             if c == c.upper():
#                 cipher += chr((((a * (ord(c) - ord('A'))) + b) % 26) + ord('A'))
#             else:
#                 cipher += chr((((a * (ord(c) - ord('a'))) + b) % 26) + ord('a'))
#         else:  # else simply append space character
#             cipher += c
#     return cipher
#
#
# # --------------------------------------------------------------------------------------
# def input_check_a(a):  # check if it has multiplicative inverse
#     a_inv = 0
#     flag = 0
#
#     for i in range(m):
#         flag = (a * i) % 26
#         # Check if (a * i) % 26 == 1,
#         # then i will be the multiplicative inverse of a
#         if flag == 1:
#             a_inv = i
#             break
#     if flag == 1:
#         return a_inv
#     else:
#         return 0
#
#
# # --------------------------------------------------------------------------------------
# def decrypt_cipher(cipher, a_inverse, b):  # decryption a_inverse is the multiplicative inverse of a
#     if a_inverse == 0:
#         print(
#             "<<<<<<<<<<<<<<<<<<<<<<<<"
#             "--Given a parameter doesn't have multiplicative inverse--"
#             ">>>>>>>>>>>>>>>>>>>>>>>>>>>")
#         return
#     msg = ""
#     b_inv = m - (b % m)
#     # flag = 0
#     # #Find a^-1 (calcu multiplicative inverse)
#     # for i in m:
#     #     flag = (a * i) % 26
#     #     # Check if (a * i) % 26 == 1,
#     #     # then i will be the multiplicative inverse of a
#     #     if flag == 1:
#     #         a_inv = i
#     #         break
#     # if flag == 1:
#     #     return a_inv
#     # else:
#     #     return 0
#     for c in cipher:
#         if c.isalpha():
#             if c == c.upper():
#                 msg += chr(((a_inverse * (ord(c) + ord('A') + b_inv)) % 26) + ord('A'))
#             else:
#                 msg += chr(((a_inverse * (ord(c.upper()) + ord('A') + b_inv)) % 26) + ord('A')).lower()
#         else:
#             msg += c
#     return msg
#
#
# # --------------------------------------------------------------------------------------
# a_inverse_key = input_check_a(5)
# print(encrypt_message("MegaMore_Gonna @Drive $the %world ^to Madness+_+)+_(_(_&*&^(!*&@%<>", 5, 6))
# print(decrypt_cipher(encrypt_message("MegaMore_Gonna @Drive $the %world ^to Madness+_+)+_(_(_&*&^(!*&@%<>", 5, 6),
#                      a_inverse_key, 6))
#
# print("\n\n")
# # ------------------------------------------------------------------------------------------
# def generateKey(string, key):
#     key_ = ""
#     if len(string) == len(key):
#         return(key)
#     else:
#         for i in range(len(string)):
#             key_ += (key[i % len(key)])
#     return key_
# # -----------------------------------------------------------------------------------------------------------------------
# def cipherText(string, key):
#     cipher_text = ""
#     for i in range(len(string)):
#         if string[i].isalpha():
#             if string[i] == string[i].upper():
#                 cipher_text += chr(((ord(string[i]) + ord(key[i].upper())) % 26) + ord('A'))
#             else:
#                 cipher_text +=  chr(((ord(string[i].upper()) + ord(key[i].upper())) % 26) + ord('a')).lower()
#         else:
#             cipher_text += string[i]
#
#     return cipher_text
# # -----------------------------------------------------------------------------------------------------------------------
# def originalText(cipher_text, key):
#     orig_text = ""
#     for i in range(len(cipher_text)):
#         if cipher_text[i].isalpha():
#             if cipher_text[i] == cipher_text[i].upper():
#                 orig_text += chr(((ord(cipher_text[i]) - ord(key[i].upper())) % 26) + ord('A'))
#             else:
#                 orig_text += chr(((ord(cipher_text[i].upper()) - ord(key[i].upper()) ) % 26) + ord('a')).lower()
#         else:
#             orig_text += cipher_text[i]
#
#     return orig_text
# # ----------------------------------------------------------------------------------------------------------------------
# print(cipherText("MegaMore_Gonna @Drive $the %world ^to Madness+_+)+_(_(_&*&^(!*&@%<>",generateKey("MegaMore_Gonna @Drive $the %world ^to Madness+_+)+_(_(_&*&^(!*&@%<>","LEMon")))
# print(originalText(cipherText("MegaMore_Gonna @Drive $the %world ^to Madness+_+)+_(_(_&*&^(!*&@%<>",generateKey("MegaMore_Gonna @Drive $the %world ^to Madness+_+)+_(_(_&*&^(!*&@%<>","LEMON")),generateKey("MegaMore_Gonna @Drive $the %world ^to Madness+_+)+_(_(_&*&^(!*&@%<>","LEMon")))

# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# print(decodingMessage(encodingMessage("Go to hell", 5), 5))
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# x = "Alpha_Beta_Camma"
# words = x.split("_")
# for word in words:
#     if word[0] == word[0].upper() and word[1:] == word[1:].lower():
#         print (ord(word[0])+1, "is conformant")
#     else:
#         print (ord(word[0])+1, "is non conformant")
