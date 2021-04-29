import hashlib
#Wisa Terhune DePaul Computer Security course, HW: Password Hacking


#Dictionary Password Hack Attack
#We will read our first 3 hex files and strip spaces from the file just in case
hex1 = open("pw1.hex","r")
password1 = hex1.read().strip()
hex1.close()

hex2 = open("pw2.hex","r")
password2 = hex2.read().strip()
hex2.close()

hex3 = open("pw3.hex","r")
password3 = hex3.read().strip()
hex3.close()

#open the given dictionary file and read the fields
dictionaryFile = open("dic-0294.txt","r") 
dictionary = dictionaryFile.readlines()
dictionaryFile.close

#We will try various hashing alogrithms such as md5, sha1, and sha256
print ("Now Finding First Password from Hashes...")

for field in dictionary:
    field = field.strip('\n')

    hashtestOne_sha256 = hashlib.sha256(field.encode()).hexdigest()
    hashtestOne_md5 = hashlib.md5(field.encode()).hexdigest()
    hashtestOne_sha1 = hashlib.sha1(field.encode()).hexdigest()
    
    if hashtestOne_sha256 == password1:
        print ("Password 1 is ==> ", end = "" )
        print (field)    

    elif hashtestOne_md5 == password1:
        print ("Password 1 is ==> ", end = "" )
        print (field)

    elif hashtestOne_sha1 == password1:
        print ("Password 1 is ==> ", end = "" )
        print (field)


#Now testing for password 2 from the hashes
print ("Now Finding Second Password from Hashes....")

for field in dictionary:
    field = field.strip('\n')

    hashTestTwo_sha256 = hashlib.sha256(field.encode()).hexdigest()
    hashTestTwo_md5 = hashlib.md5(field.encode()).hexdigest()
    hashTestTwo_sha1 = hashlib.sha1(field.encode()).hexdigest()

    if hashTestTwo_sha256 == password2:
        print ("Password 2 is ==> ", end = "" )
        print (field)    

    elif hashTestTwo_md5 == password2:
        print ("Password 2 is ==> ", end = "" )
        print (field)

    elif hashTestTwo_sha1 == password2:
        print ("Password 2 is ==> ", end = "" )
        print (field)


#Now testing for password 3 from the hashes
print ("Now Finding 3rd Password from Hashes...")
for field in dictionary:
    field = field.strip('\n')

    hashTest3_sha256 = hashlib.sha256(field.encode()).hexdigest()
    hashTest3_md5 = hashlib.md5(field.encode()).hexdigest()
    hashTest3_sha1 = hashlib.sha1(field.encode()).hexdigest()

    if hashTest3_sha256 == password3:
        print ("Password 3 is ==> ", end = "" )
        print (field)    

    elif hashTest3_md5 == password3:
        print ("Password 3 is ==> ", end = "" )
        print (field)

    elif hashTest3_sha1 == password3:
        print ("Password 3 is ==> ", end = "" )
        print (field)


################################################################
#Salted Hash Password Cracking
        
#Reading our hash hex files
#Trimming the spaces for each hex
hash1 = open("spw1.hex","r")
passwordHash1 = hash1.read().strip()
hash1.close()

hash2 = open("spw2.hex","r")
passwordHash2 = hash2.read().strip()
hash2.close()

hash3 = open("spw3.hex","r")
passwordHash3 = hash3.read().strip()
hash3.close()

#Opening salt file and reading value
saltFile = open("salt.hex","r")
salt = saltFile.read()
saltFile.close()

saltByte = bytes.fromhex(salt) #Changing salt hex value to bytes

print("Now Finding Salted password 1....")
for field in dictionary:
    field = field.strip('\n')

    byteString = field.encode()

    saltedEntry = saltByte + byteString

    hash_sha256 = hashlib.sha256(saltedEntry).hexdigest()
    hash_sha1 = hashlib.sha1(saltedEntry).hexdigest()
    hash_md5 = hashlib.md5(saltedEntry).hexdigest()

    if hash_sha1 == passwordHash1:
        print ("Salted Password 1 is ==> ", end = "" )
        print (field)
   
    elif hash_md5 == passwordHash1:
        print ("Salted Password 1 is ==> ", end = "" )
        print (field)

    elif hash_sha256 == passwordHash1:
        print ("Salted Password 1 is ==> ", end = "" )
        print (field)

print("Now Finding Salted Password 2....")
for field in dictionary:

    field = field.strip('\n')
    byteString = field.encode()
    saltedEntry = saltByte + byteString

    hash_sha1 = hashlib.sha1(saltedEntry).hexdigest()
    hash_sha256 = hashlib.sha256(saltedEntry).hexdigest()
    hash_md5 = hashlib.md5(saltedEntry).hexdigest()

    if hash_sha256 == passwordHash2:
        print ("Salted Password 2 is ==> ", end = "" )
        print (field)
        
    elif hash_md5 == passwordHash2:
        print ("Salted Password 2 is ==> ", end = "" )
        print (field)

    elif hash_sha1 == passwordHash2:
        print ("Salted Password 2 is ==> ", end = "" )
        print (field)

print("Now Finding Salted Password 3....")
for field in dictionary:

    field = field.strip('\n')
    byteString = field.encode()
    saltedEntry = saltByte + byteString

    hash_sha256 = hashlib.sha256(saltedEntry).hexdigest()
    hash_md5 = hashlib.md5(saltedEntry).hexdigest()
    hash_sha1 = hashlib.sha1(saltedEntry).hexdigest()

    if hash_sha256 == passwordHash3:
        print ("Salted Password three is ==> ", end = "" )
        print (field)
        
    elif hash_md5 == passwordHash3:
        print ("Salted Password three is ==> ", end = "" )
        print (field)

    elif hash_sha1 == passwordHash3:
        print ("Salted Password three is ==> ", end = "" )
        print (field)
