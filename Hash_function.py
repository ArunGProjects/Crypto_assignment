import hashlib
def compute_hash(message):
    hash_object = hashlib.sha256()
    hash_object.update(message.encode('utf-8'))
    return hash_object.hexdigest()
original_message = "Hello, world!"
print("Original message:", original_message)
original_hash = compute_hash(original_message)
print("Hash of the original message:", original_hash)
receiver_hash = compute_hash(original_message)
print("Receiver's hash of the original message:", receiver_hash)
if original_hash == receiver_hash:
    print("Original message is intact.")
else:
    print("Original message has been modified.")
modified_message = "Hello, world?"
print("\nModified message:", modified_message)
modified_hash = compute_hash(modified_message)
print("Hash of the modified message:", modified_hash)
receiver_modified_hash = compute_hash(modified_message)
print("Receiver's hash of the modified message:", receiver_modified_hash)
if modified_hash == receiver_modified_hash:
    print("Modified message is intact.")
else:
    print("Modified message has been tampered with.")
