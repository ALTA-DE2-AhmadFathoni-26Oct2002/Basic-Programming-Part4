def ubah_huruf(sentence):
    pattern = ""
    for karakter in sentence:
        if 'A' <= karakter <= 'Z':
            huruf = ord(karakter) - ord('A')
            huruf_baru = (huruf + 10) % 26
            karakter_baru = chr(ord('A') + huruf_baru)
        else:
            karakter_baru = karakter
        pattern += karakter_baru
    return pattern

if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA")) # SXNYXOCSK
    print(ubah_huruf("GOLANG")) # QYVKXQ
    print(ubah_huruf("PROGRAMMER")) # ZBYQBKWWOB

