import math
from eu_ext import modinv


#RSA
def rsa_encrypt(n,d,plain,e):
    #n = 1157942081
    #d= 463148717
    #plain = 412348710
    #e = 5 

    cipher  = (pow(plain,e)%n)
    print(cipher)
    dec_cipher = (pow(cipher,d)%n)
    #print(dec_cipher)
    return 0

# RSA Signing and Verification

def rsa_sv(m_hash,d,n,e):
    #m_hash = 321238888
    #d = 463148717
    #n = 1157942081
    #e=5

    m_signature = pow(m_hash,d,n)

    veri_hash = pow(m_signature,e,n)

    print("Message Hash is: " + str(m_hash))
    print("Message Signature is: " + str(m_signature))

    if m_hash == veri_hash: 
        print("M_Hash and V_Hash are: " + str(veri_hash))
        return 0
    elif m_hash != veri_hash:
        print("M_Hash and V_Hash do not equal!")
        return 0
    else:
        print("Something Happened")
        return 1

#Diffie-Hellman Key Exchange
def dhkeyx(g,p,a,b):

    #g = 5
    #p = 26357
    #a=12345
    #b=23456
    a_pub = pow(g,a,p)
    b_pub = pow(g,b,p)
    print("Alice public key:" + str(a_pub))
    print("Bob public key:" + str(b_pub))
    a_shared = pow(a_pub,b,p)
    b_shared = pow(b_pub,a,p)
    if b_shared == a_shared:
        print("Alice and Bob shared key:" + str(b_shared))
        return 0
    else:
        print("Something happened")
        return 1

