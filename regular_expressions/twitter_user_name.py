
# In this program what we trying to do is extracting user name from twitter url

"""
url = input("URL: ").strip()

#username = url.replace("https://twitter.com/", "")


username = url.removeprefix("https://twitter.com/")
# Remove prefix here removes https:///twitter.com/ but only when it comes at start and it is better approach for multiple occurences than replace

print(f"Username: {username}")

# But this program using such functions like replace and removeprefix is not effective for the issues like http instead of https, www and others

"""
# To address more issues we need to use re library here again
import re

url = input("URL: ").strip()

# username = re.sub("^(https?://)?(www\.)?twitter\.com/", "", url)

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))



