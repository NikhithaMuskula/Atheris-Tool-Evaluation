import sys

import atheris


def fuzz_test(data: atheris.FuzzedDataProvider):
    try:
        print(type(data))
        bytes_data = data.peel_bytes()
        string_data = bytes_data.decode('utf-8')
        print(f"Consumed String: {string_data}")
    except UnicodeDecodeError:
        print("Error: Unable to decode bytes to string.")


# Atheris setup
atheris.Setup(sys.argv, fuzz_test)
atheris.Fuzz()
