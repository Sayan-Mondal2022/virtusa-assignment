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

    # Will return True if the word exist in the SET
    return cleaned_word in banned_words


def Moderator(posts: dict) -> int:
    """
    This function will clean teh post, if it contains any Banned Words

    This will return the number of times the post was flagged.
    """
    post = posts["post"]
    flag_count = 0

    words = post.split()
    for i, w in enumerate(words):
        if w.startswith("http") or w.startswith("https"):
            save_links(posts["user"], w)
            continue

        # Flagged a Banned word and then Performs the WORD MASKING
        if flag_banned_words(w):
            words[i] = w.replace(w, "*" * len(w))
            flag_count += 1

    post = " ".join(words)
    posts["post"] = post

    return flag_count


# This will save the link
def save_links(user: str, link: str):
    """
    This function is used to save the HTTP or HTTPS links into a txt file.
    """
    try:
        with open("links_found.txt", "a") as file:
            file.write(f"user: {user}, link: {link.strip(",.!?")}\n")
    except Exception as e:
        print(f"Error while saving link: {e}")
