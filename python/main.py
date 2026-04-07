from data import sample_posts
import json
from helper import Moderator

users = {}
cleaning_summary = {"Total Posts Screened": 0, "Cleaned": 0, "Blocked": 0}

# If a Post gets a flag count more than the threshold then the particular post is blocked.
threshold = 3

# Add all users:
for post in sample_posts:
    users[post["user"]] = 0

# Tracking the number of times the Moderator flagged the post:
for post in sample_posts:
    flag_count = Moderator(post)
    if flag_count > 0:
        # Incrementing the flagged post count for the user.
        users[post["user"]] += 1
        cleaning_summary["Cleaned"] += 1

    if flag_count >= threshold:
        cleaning_summary["Blocked"] += 1
    cleaning_summary["Total Posts Screened"] += 1

try:
    with open("cleaned_data.txt", "w") as file:
        for post in sample_posts:
            file.write(json.dumps(post) + "\n")
        print("Cleaned Posts has been saved in 'cleaned_data.txt' file\n")
except Exception as e:
    print(f"Error while saving cleaned data: {e}")


# Displaying the Summary
print("Users Summary:")
for user in users:
    print(f"{user}: {users[user]}")

print(f"\nFinal Report")
for k in cleaning_summary:
    print(f"{k}: {cleaning_summary[k]}")
