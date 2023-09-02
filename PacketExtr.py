import sys, io


def main():
    payload = read_next_packet()
    while payload is not None:
        sys.stdout.buffer.write(payload)
        sys.stdout.buffer.flush()
        payload = read_next_packet()



def read_packet_size() -> int:
    """Returns packet size. If no more packets, returns `-1`."""
    HEADER_PREFIX_BYTES = b'Size: '

    # Extract header.
    header_prefix = sys.stdin.buffer.read1(len(HEADER_PREFIX_BYTES))
    if has_no_more_packets := (header_prefix == b''):
        return -1
    assert header_prefix == HEADER_PREFIX_BYTES, \
        f'Expected 0x{HEADER_PREFIX_BYTES.hex()}, got 0x{header_prefix.hex()}.'

    # Read byte-by-byte until b"B" is found, to get the size.
    data = sys.stdin.buffer.read1(1)
    with io.BytesIO() as size_buffer:
        while data != b'B':
            size_buffer.write(data)
            data = sys.stdin.buffer.read1(1)
        size_bytes = size_buffer.getvalue()
        size = int(size_bytes.decode())

    return size


def read_next_packet() -> bytes | None:
    """Returns payload of next packet. If no more packets, returns `None`."""
    packet_size = read_packet_size()
    if has_no_more_packets := (packet_size == -1):
        return None
    payload = sys.stdin.buffer.read1(packet_size)
    return payload



if __name__ == "__main__":
    main()
