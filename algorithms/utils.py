def str_to_int(text: str) -> int:
    """
    Convert a string to an integer.
    :param text: the string to convert
    :return: the integer representation of the string
    :type text: str
    :rtype: int
    :author: Muhammad Umer Farooq
    """
    return int.from_bytes(text.encode("utf-8"), "big")


def int_to_str(text: int) -> str:
    """
    Inverse of str_to_int.
    :param text: the integer to convert
    :return: the string representation of the integer
    :type text: int
    :rtype: str
    :author: Muhammad Umer Farooq
    """
    import math
    return text.to_bytes(math.ceil(text.bit_length() / 8), "big").decode("utf-8")
