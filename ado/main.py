# pylint: disable=missing-docstring

import os
import requests
from tqdm import tqdm


ORG = os.environ["ADO_ORG"]
PROJECT = os.environ["ADO_PROJECT"]
TOKEN = os.environ["ADO_TOKEN"]

def commit_details(repoid):
    com_url = f"https://dev.azure.com/{ORG}/{PROJECT}/_apis/git/repositories/{repoid}/commits?api-version=4.1"
    payload = {}
    headers = {"Authorization": TOKEN}

    response = requests.request("GET", com_url, headers=headers, data=payload, timeout=10)
    com_info = response.json()
    if com_info["count"] == 0:
        com_date = ""
        com_author = ""
        com_email = ""
    else:
        com_date = com_info["value"][0]["author"]["date"].split("T")[0]
        com_author = com_info["value"][0]["author"]["name"]
        com_email = com_info["value"][0]["author"]["email"]
    return com_date, com_author, com_email


def pull_repo_details():
    url = f"https://dev.azure.com/{ORG}/{PROJECT}/_apis/git/repositories?api-version=6.1-preview.1"
    payload = {}
    headers = {"Authorization": TOKEN}
    response = requests.get(url, headers=headers, data=payload, timeout=10)
    repo_info = response.json()
    num_repos = repo_info["count"]
    with tqdm(total=num_repos, desc="Processing repos", unit="repos") as pbar:
        for item in repo_info["value"]:
            repo_name = item["name"]
            repo_id = item["id"]
            com_date, com_author, com_email = commit_details(repo_id)
            with open("test_repos.csv", "a", encoding="utf-8") as repo_file:
                print(f"{repo_name},{com_date},{com_author},{com_email}", file=repo_file)
            pbar.update(1)


if __name__ == "__main__":
    with open("test_repos.csv", "w", encoding="utf-8") as file:
        print("Repo Name,Commit Date,Commit Author,Commit Email", file=file)
    pull_repo_details()
