def flag_banned_words(word: str) -> bool:
    """
    Function returns True, if the word matches with the Banned Word
    """
    word = word.lower()
    banned_words = {"bad", "toxic", "hate"}

    # This will be used to remove special chars, spaces, numbers and repeated chars.
    cleaned_word = ""
    last_char = ""
    for ch in word:
        if ch.isalpha() and ch != last_char:
            cleaned_word += ch
            last_char = ch

    # WIll return True if the word exist in the SET
    return cleaned_word in banned_words
