def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def mod_inv(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def encrypt(msg, pub_key, n):
    return pow(msg, pub_key, n)

def decrypt(cipher, priv_key, n):
    return pow(cipher, priv_key, n)

def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break

    d = mod_inv(e, phi)
    pub_key = (e, n)
    priv_key = (d, n)

    return pub_key, priv_key

p = 61
q = 53

# pub_key, priv_key = generate_keys(p, q)
pub_key, priv_key = (103, 697) , (87, 697)
msg = 65

cipher = encrypt(msg, pub_key[0], pub_key[1])
decrypted_msg = decrypt(cipher, priv_key[0], priv_key[1])

print("Original message:", msg)
print("Encrypted message:", cipher)
print("Decrypted message:", decrypted_msg)