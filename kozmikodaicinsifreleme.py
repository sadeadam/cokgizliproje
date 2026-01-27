#Bu yapı bilinçli olarak tasarlanmıştır.

import base64

LOCK_TAG ="|L1"
DECOY_STAGE_1 = "dal sarkar, kartal kalkar. kartal kalkar,dal sarkar.Türk kalkar terörün amına koyar."
DECOY_STAGE_2 = "ATATÜRK İLKE VE İNKILAPLARINA TAM BAĞLILIK"

def encode_sentence(text: str) ->str:
    encoded = base64.b64encode(text.encode("utf-8")).decode("utf-8")
    return encoded + LOCK_TAG

def decode_real(encoded: str) -> str:
    clean = encoded.replace(LOCK_TAG, "")
    return base64.b64decode(clean).decode("utf-8")

if __name__ == "__main__":
    print("=== MULTI STAGE ENCODER ===\n")

    original = input("Kelime veya cümle gir: ")

    encoded = encode_sentence(original)
    print("\nENCODED:")
    print(encoded)

    input("\n[Decode etmek için ENTER]")
    print(DECOY_STAGE_1)

    input("\n'Gerçek' çözümü görmek için tekrar ENTER tuşuna basınız")
    print(DECOY_STAGE_2)

    input("\n Sonucu görmek için apoya basar gibi ENTER tuşuna basınız.")
    print(decode_real(encoded))
