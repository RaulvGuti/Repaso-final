def fnv1_64(data: bytes) -> str:
    FNV_offset_basis = 0xcbf29ce484222325
    FNV_prime = 0x100000001b3
    hash_ = FNV_offset_basis
    for byte in data:
        hash_ = (hash_ * FNV_prime) % (1 << 64)
        hash_ ^= byte
    return format(hash_, '016x')


def rle_encode(text: str) -> str:
    if not text:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed.append(text[i - 1] + str(count))
            count = 1
    compressed.append(text[-1] + str(count))
    return ''.join(compressed)


def main():
    mensaje = input("Ingrese un mensaje de texto: ")

    hash_result = fnv1_64(mensaje.encode('utf-8'))
    print("Hash FNV-1 (64 bits):", hash_result)

    comprimido = rle_encode(mensaje)
    print("Tamaño que tenia antes de comprimir:", len(mensaje.encode('utf-8')), "bytes")
    print("Tamaño que tiene despues de comprimir:", len(comprimido.encode('utf-8')), "bytes")


if __name__ == "__main__":
    main()
