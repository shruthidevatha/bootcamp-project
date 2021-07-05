# Program to generate hashes of string data using algorithms from Hashlib
import hashlib
txt = input("enter text :")
result1 = hashlib.md5(txt.encode())  #generates MD5 of string data
result2 = hashlib.sha1(txt.encode())
result3 = hashlib.sha256(txt.encode())   #hashes of string data using other algorithms of hashlib
result4 = hashlib.sha512(txt.encode())
print("the equivalent hashes are : " ,end= "\n")
print(result1.hexdigest())
print(result2.hexdigest())
print(result3.hexdigest())
print(result4.hexdigest())
