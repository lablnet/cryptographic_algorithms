# Chapter 2 hashing.
import hashlib
# md5hasher = hashlib.md5(b'Alice')
# print(md5hasher.hexdigest())
# md5hasher = hashlib.md5(b'Bob')
# print(md5hasher.hexdigest())
# print(hashlib.algorithms_available)
# print(hashlib.md5(b'a'*100000).hexdigest())
# md5hasher = hashlib.md5(b'A')
# md5hasher.update(b'l')
# md5hasher.update(b'i')
# md5hasher.update(b'c')
# md5hasher.update(b'e')
# print(md5hasher.hexdigest())
# open file.txt in rb mode.
f = open("raw/file.txt", "rb")
hasher = hashlib.md5(f.read())
print(hasher.hexdigest())
f.close()