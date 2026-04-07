from data import sample_posts
import json


# Function returns True, if the word matches with the Banned Word
def flag_banned_words(word: str) -> bool:
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


def Moderator(posts: dict) -> bool:
    post = posts["post"]
    flagged = False

    words = post.split()
    for i in range(len(words)):
        w = words[i]
        # Flagged a Banned word

        if w.startswith("http") or w.startswith("https"):
            save_links(posts["user"], w)
            continue

        # Performs the WORD MASKING
        if flag_banned_words(w):
            sub_word = w[1 : len(w) - 1]
            replace_pat = "*" * len(sub_word)

            words[i] = w.replace(sub_word, replace_pat)
            flagged = True

    post = " ".join(words)
    posts["post"] = post

    return flagged


# This will save the link
def save_links(user: str, link: str):
    try:
        with open("links_found.txt", "a") as file:
            file.write(f"user: {user}, link: {link}\n")
    except Exception as e:
        print("Error while saving link")


users = {}
cleaning_summary = {"Total Posts Screened": 0, "Cleaned": 0, "Blocked": 0}

# Add all users:
for post in sample_posts:
    users[post["user"]] = 0

# Tracking the number of times the Moderator flagged the post:
for post in sample_posts:
    if Moderator(post):
        cleaning_summary["Cleaned"] += 1
        users[post["user"]] += 1
    cleaning_summary["Total Posts Screened"] += 1

try:
    with open("cleaned_data.txt", "w") as file:
        for post in sample_posts:
            file.write(json.dumps(post) + "\n")
        print("Cleaned Posts has been saved in 'cleaned_data.txt' file\n")
except Exception as e:
    print("Error while saving cleaned data")


# Displaying the Summary
print("Users Summary:")
for user in users:
    print(f"{user}: {users[user]}")

print(f"\nFinal Report")
for k in cleaning_summary:
    print(f"{k}: {cleaning_summary[k]}")
