def get_letters_list(text):
    letters_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    text = text.lower().strip()
    total = 0

    for i in range(len(text)):
        if text[i].isalpha():
            total += 1
            letters_list[ord(text[i])-97] = letters_list[ord(text[i])-97] + 1

    for i in range(len(letters_list)):
        letters_list[i] = letters_list[i]/total

    return letters_list
