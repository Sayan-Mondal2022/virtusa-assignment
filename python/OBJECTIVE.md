## Core Python: The **SocialMedia** Content Sanitizer

**Business Case:**\
A startup is launching a safe social media platform for schools. They need a tool that automatically "screens" posts for banned words and links before they go live.

**Problem Statement:**\
Build a **`Content Moderator Script`** that scans a list of posts, replaces **Banned Words** with asterisks `(***)`, and extracts all web links for security clicking.

**Student Tasks:**
1.	**List Processing:** Start with a list of strings (Sample Posts).
2.	**Word Masking:** Use a `banned_words = ["bad", "toxic", "hate"]` list. If a post contains these, replace them using `.replace()`.
3.	**Link Extraction:** Use string slicing or the `.startswith('http')` method to find all URLs in the posts and save them to a `links_found.txt` file.
4.	**Summary Dictionary:** Create a dictionary that tracks how many times each user flagged the `"Moderator" (e.g., {'User123': 3, 'User456': 0})`.
5.	**User Report:** Print a final report: `Total Posts Screened: X | Cleaned: Y | Blocked: Z.`


**Deliverable:** A `Python script` that demonstrates `Cleaning` a messy text file into a `Safe` version.
