import random

# Function to compute greatest common divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to compute modular inverse using Extended Euclidean Algorithm
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Function to test for primality
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to generate a random prime number
def generate_prime(start=100, end=300):
    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num

# Function to generate RSA key pairs
def generate_keys():
    p = generate_prime()
    q = generate_prime()
    while q == p:
        q = generate_prime()
    
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = modinv(e, phi)
    
    return (e, n), (d, n)

# Function to encrypt a message
def encrypt(message, public_key):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher

# Function to decrypt a message
def decrypt(ciphertext, private_key):
    d, n = private_key
    message = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return message

# Main function to test the RSA implementation
def rsa_demo():
    public_key, private_key = generate_keys()
    message = "HELLO RSA"
    
    print("Original Message:", message)
    encrypted_msg = encrypt(message, public_key)
    print("Encrypted Message:", encrypted_msg)
    decrypted_msg = decrypt(encrypted_msg, private_key)
    print("Decrypted Message:", decrypted_msg)

# Run the demo
rsa_demo()
