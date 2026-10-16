#Caesar Cipher
def caesar(text, shift, encrypt=True):
    # Ensure the shift value is an integer
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    # Validate that the shift is within the acceptable range
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    # Define the alphabet used for shifting
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # If decrypting, reverse the shift direction
    if not encrypt:
        shift = -shift
    
    # Create the shifted alphabet by slicing and concatenating
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # Build a translation table mapping each letter to its shifted counterpart
    # Includes both lowercase and uppercase versions
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    # Translate the text using the table
    return text.translate(translation_table)


def encrypt(text, shift):
    # Wrapper for encryption
    return caesar(text, shift)
    

def decrypt(text, shift):
    # Wrapper for decryption
    return caesar(text, shift, encrypt=False)


# Example usage
encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)
