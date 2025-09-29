import sys
import json
import http.client


def user_name() -> str:
    """
    check the user name if it exist will be return
    """
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <username>")
        sys.exit()
    return args[1]


def get_latest_events(username: str) -> None:
    headers = {
    "Host": "api.github.com",
    "User-Agent": "python-http-client",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
    }

    conn = http.client.HTTPSConnection("api.github.com")
    # in python3.9 > if i write the headers directly in the parameter it will give me error
    # from the server (its bug in http.client)
    conn.request("GET", f"/users/{username}/events", headers=headers)
    response = conn.getresponse()

    data = response.read()
    dictData = json.loads(data.decode())

    print("\n==== GitHub Activity for USERNAME ====")
    for x, i in enumerate(dictData, 1):

        print(f"[{x}]")
        for j in i:
            if j == "type":
                print(f"Event: {i[j]}")
            elif j == "repo":
                print(f"Repo: {i[j]['name']}")
            elif j == "created_at":
                print(f"Date: {i[j]}")
        print("----------------------------")

    conn.close()


if __name__ == "__main__":
    try:
        user = user_name()
        get_latest_events(user)
    except Exception:
        print("API failures")
