def print_upper_words(words,must_start_with="e"):
    """given a word or iterable of words and a letter or iterable of letters,
    print_upper_words will print all of the words provided, in upper case, that begin
    with one of the letters provided 
    example: 
    
    print_upper_words(words=["hello", "hey", "goodbye", "yo", "yes"],must_start_with={"G", "g", "y"})
    will return:
    GOODBYE
    YO
    YES
    """


    for word in words:
        for letter in must_start_with:
            if word.upper().startswith(letter.upper()):
                print(word.upper())
                break

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],must_start_with={"G", "g", "y"})