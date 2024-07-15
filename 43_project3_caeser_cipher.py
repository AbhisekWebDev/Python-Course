characters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
    '😀', '😁', '😂', '🤣', '😃', '😄', '😅', '😆', '😉', '😊', '😋', '😎', '😍', '😘', '🥰', '😗', '😙', '😚', '🙂', '🤗', 
    '🤩', '🤔', '🤨', '😐', '😑', '😶', '🙄', '😏', '😣', '😥', '😮', '🤐', '😯', '😪', '😫', '😴', '😌', '😛', '😜', '😝', 
    '🤤', '😒', '😓', '😔', '😕', '🙃', '🤑', '😲', '☹️', '🙁', '😖', '😞', '😟', '😤', '😢', '😭', '😦', '😧', '😨', '😩', 
    '🤯', '😬', '😰', '😱', '🥵', '🥶', '😳', '🤪', '😵', '😡', '😠', '🤬', '😷', '🤒', '🤕', '🤢', '🤮', '🤧', '😇', '🥳', 
    '🥴', '🥺', '🤠', '🤡', '🤥', '🤫', '🤭', '🧐', '🤓', '😈', '👿', '👹', '👺', '💀', '👻', '👽', '👾', '🤖'
]

def encrypt(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in characters:
            position = characters.index(char)
            new_position = (position + shift_key) % len(characters)
            cipher_text += characters[new_position]
        else:
            cipher_text += char
    print(f"The text after encryption: {cipher_text}")

def decrypt(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in characters:
            position = characters.index(char)
            new_position = (position - shift_key) % len(characters)
            plain_text += characters[new_position]
        else:
            plain_text += char
    print(f"The text after decryption: {plain_text}")

wanna_end = False

while not wanna_end:
    choice = input("Type E to encrypt or Type D to decrypt: ")
    text_input = input("Enter text: ")
    shift = int(input("Enter shift number key: "))

    if choice.lower() == "e":
        encrypt(plain_text=text_input, shift_key=shift)
    elif choice.lower() == "d":
        decrypt(cipher_text=text_input, shift_key=shift)
    
    play_again = input("Type Y to continue or Type N to exit: ")

    if play_again.lower() == "n":
        wanna_end = True
        print("Thanks...")
