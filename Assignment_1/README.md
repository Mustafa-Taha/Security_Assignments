# program to encrypt and decrypt classical ciphers as follows.

• The whole program in one solution.py file.
• The program supports encryption and decryption using shift, affine, andvigenere ciphers.

• callable from command line as follows:
  ◦ First argument is the cipher type [“shift”,”affine”,”vigenere”].
  ◦ Second argument is the operation type [“enc”, “dec”].
  ◦ The Third argument is the input file.
  ◦ The fourth argument is the output file.
  ◦ The last argument is the the list of encryption keys required for the cipher.
• Examples calls from terminal {all text case incensitive}:
   Case 1 :solution.py <cae|caeaser|shift|shi> <enc|encrypt> input.text output.text b
   Case 2 :solution.py <cae|caeaser|shift|shi> <dec|decrypt> input.text output.text b
   Case 3 :solution.py <aff|affine> <enc|encrypt> input.text output.text a b
   Case 4 :solution.py <aff|affine> <dec|decrypt> input.text output.text a b
   Case 5 :solution.py <vigenere|vig> <enc|encrypt> input.text output.text Key
   Case 6 :solution.py <vigenere|vig> <dec|decrypt> input.text output.text Key
