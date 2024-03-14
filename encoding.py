from nacl.public import Box, PrivateKey, PublicKey
import nacl.encoding
import nacl.utils

# Replace PUBLIC_KEY and SECRET_VALUE with the values obtained from the GitHub API
public_key_str = 'nyQhEgz25eW2kzkqnmpL/58xJtkZgiCCVRg46WpYLkg='
secret_value = 'encoded'

# Decode the base64-encoded public key
public_key = PublicKey(public_key_str, encoder=nacl.encoding.Base64Encoder)

# Generate a new randomly generated private key
private_key = PrivateKey.generate()

# Get the corresponding public key
public_key_from_private = private_key.public_key

# Create a Box using the public key obtained from the private key and the GitHub's public key
box = Box(private_key, public_key)

# Encrypt the secret value using the Box
encrypted_value = box.encrypt(secret_value.encode(), encoder=nacl.encoding.Base64Encoder)

# Print the encrypted value
print("Encrypted value:", encrypted_value.ciphertext.decode())
