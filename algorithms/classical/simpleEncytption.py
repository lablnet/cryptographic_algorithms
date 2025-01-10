def encode_decode(text, type="encode", key=1):
    """
    Simple encryption and decryption algorithm.
    :param text: str, the text to encode or decode.
    :param type: str, the type of operation to perform.
    :param key: int, the key to use for the operation.
    :return: str, the encoded or decoded text.
    """
    
    # check if the type is valid
    assert type in ["encode", "decode"]
    # check if the key is valid
    assert key in range(1, 255)
    # check if the text is valid
    assert isinstance(text, str)

    t = ""
    for char in text:
        # convert char to ascii
        a = ord(char)
        if type == "encode":
            # add key to ascii
            a += key
        elif type == "decode":
            # subtract key from ascii
            a -= key
        # convert back to char
        b = chr(a)
        t += b
    return t

if __name__ == "__main__":
    text = "Hello World"
    key = 254
    encode = encode_decode(text, "encode", key) # output: "Ifmmp Xpsme"
    decode = encode_decode(encode, "decode", key) # output: "Hello World"
    print("text: ", text, "\nencode: ", encode, "\ndecode: ", decode)
