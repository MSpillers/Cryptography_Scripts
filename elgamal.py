import math
from eu_ext import modinv
# EL Gamal Crypto
def eg_encrypt(p,g,a_private_key,plaintext,b_private_key):
    #p=26357
    #g=5
    #a_private_key=12345
    #plaintext = 14567
    #b_private_key = 4357

    a_public_key = pow(g,a_private_key,p)
    print("Plaintext is: " + str(plaintext))
    print("Alice's private key is :" + str(a_private_key))
    print("Alice's public key is :" + str(a_public_key))


    cipher = (plaintext*pow(a_public_key,b_private_key))%p
    mask = pow(g,b_private_key,p)
    print("Cipher is: " + str(cipher))
    print("Mask is: " + str(mask))

    x = pow(a_public_key,b_private_key,p)
    inv_x = modinv(x,p)
    if inv_x < 0:
        inv_x = inv_x % p

    dec_plain = (cipher*inv_x)%p
    print("Decrypted plaintext is: " + str(dec_plain))

#El Gamal Signing and Verification

def egsig(m_hash,p,g,k,a,a_public_key):

    #m_hash= 14234
    #p= 26357
    #g = 5
    #k = 4357
    #a = 12345
    #a_public_key= 4399

    r = pow(g,k,p)
    print("r is : " + str(r))

    inv_k = modinv(k,p-1)
    if inv_k < 1:
        inv_k = inv_k % (p-1)
    print("k is: " + str(inv_k))

    m_signature = int(((m_hash-(a*r)) * inv_k) % (p-1))
    print("Signature is: " + str(m_signature))

    left_side = (pow(a_public_key,r)*pow(r,m_signature)) % p
    print("Left-Side is: " + str(left_side))
    right_side = pow(g,m_hash,p) % p
    print("Right-Side is:" + str(right_side))

    if left_side == right_side:
        print("Hash Verified")
        return 0
    elif left_side != right_side:
        print("Hash not verified")
    else:
        print("Something happpened")
        return 1

