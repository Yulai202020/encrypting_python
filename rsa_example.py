import rsa
public_key, private_key = rsa.newkeys(1024)

message = b'Hello world'

chipted_message = rsa.encrypt(message, public_key)
print(chipted_message)
print(rsa.decrypt(chipted_message, private_key))
