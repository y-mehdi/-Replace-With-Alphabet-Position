def alphabet_position(text):
    new_text=text.lower()
    n=0
    extra_text=""
    while n<len(new_text):
        letter_position=ord(new_text[n])-96
        if letter_position>0 & letter_position<24:
            extra_text=extra_text+str(letter_position)+" "
        n+=1
    z=len(extra_text)-1
    return extra_text[:z]
    pass
