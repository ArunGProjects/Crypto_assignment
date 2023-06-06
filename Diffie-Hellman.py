def calculate_public_key(g, p, private_key):
    return pow(g, private_key, p)
def calculate_shared_secret(public_key, private_key, p):
    return pow(public_key, private_key, p)
g = 2  
p = 23  
x = 6  
y = 15  
A = calculate_public_key(g, p, x)
B = calculate_public_key(g, p, y)
shared_secret_alice = calculate_shared_secret(B, x, p)
shared_secret_bob = calculate_shared_secret(A, y, p)
print("Alice's public key (A):", A)
print("Bob's public key (B):", B)
print("\nShared secret key (Alice):", shared_secret_alice)
print("Shared secret key (Bob):", shared_secret_bob)
