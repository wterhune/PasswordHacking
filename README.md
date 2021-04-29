# PasswordHacking
Computer Security class at DePaul University

Writing a Dictionary-based Password Cracker
Background

You must write a program that uses a dictionary to recover passwords from hash values. You may use any language, but I will help you with debugging only if you use Python, Java, C#, or C/C++.

Although you may choose any dictionary that you wish, a dictionary file is supplied with the assignment. NOTE: All of the passwords used in this assignment are contained in the supplied dictionary file.

Your code should be able to recover the passwords from three ordinary hashes that are provided.

Additionally, three hashes were created by concatenating a salt value with the password. The salt value is supplied with the assignment. Your code should be able to recover the passwords from these three salted hashes, as well.

Your code need not perform any other type of password cracking, such as testing permuted user names or utilizing a Rainbow table.

Code Specification

The Java java.security.MessageDigest class provides all of the functionality required for computing hash values for this assignment.

Standard names for hash algorithms can be found in the Java Standard Algorithm Name documentation.
The hash values of the passwords were computed using the Java MessageDigest class.
The Python hashlib module provides all of the functionality required for computing hash values for this assignment.
The dictionary file is named dic-0294.txt.

Password Hashes
The three regular hash values provided are as follows:
pw1.hex
pw2.hex
pw3.hex

The salt value is contained in the file salt.hex
The salt value is stored in the file as a sequence of hex character pairs.

NOTE: Each pair of hex characters comprise a single byte of salt value that you must use. For example, the hex pair a9 must be converted to the byte value 169 (decimal) in order to be used as a salt byte.

The three salted hash values provided are as follows:
spw1.hex
spw2.hex
spw3.hex
