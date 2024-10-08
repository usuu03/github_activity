import requests
import sys
import pprint

# Github API
url = "https://api.github.com/users/"


def main():
    if len(sys.argv) < 2:
        print("Usage: github_activity <username>")
        return
    
    username = sys.argv[1]
    request = requests.get(f"https://api.github.com/users/{username}/events")
    print(request.json())
    
    
if __name__ == "__main__":
    main()