import zlib, sys

def get_file_path_arg() -> str:
    return sys.argv[1]

def main():
    file_path = get_file_path_arg()
    with open(file_path, 'rb') as f:
        file_bytes = f.read()
    checksum = zlib.crc32(file_bytes)
    print(checksum)

if __name__ == "__main__":
    main()
