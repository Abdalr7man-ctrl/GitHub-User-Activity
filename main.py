"""

"""
import sys
import json
import http.client

def user_name() -> str:
    args = sys.argv
    if   len(args) != 2:
        print("Usage: python main.py <username>")
        sys.exit()
    return args[1]

def get_latest_events(username):
    """
    PASS
    """
    headers = {
    "Host": "api.github.com",
    "User-Agent": "python-http-client"
    }
    conn = http.client.HTTPSConnection("api.github.com")
    # in python3.9 > if i write the headers directly in the parameter it will give me error
    # from the server (its bug in http.client)
    conn.request("GET", f"/users/{username}/events", headers=headers)
    response = conn.getresponse()
    data = response.read()

    print(response.status, response.reason)
    print("\nThe Headers: ")
    print(response.headers)
    print("\nThe data as a string:")
    
    dictData = json.loads(data.decode())

    for num, i in enumerate(dictData, start=1):
        print(f"The number = {num}")
        for j in i:
            print(j)
        print()

    conn.close()


if __name__ == "__main__":
    username = user_name()
    get_latest_events(username=username)
