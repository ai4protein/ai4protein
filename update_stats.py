import requests
from huggingface_hub import HfApi

USERNAME = "ai4protein"
README_PATH = "README.md"

def get_total_forks(username):
    url = f"https://api.github.com/users/{username}/repos?per_page=100"
    response = requests.get(url)
    repos = response.json()
    return sum(repo["forks_count"] for repo in repos)

def get_hf_downloads(username):
    api = HfApi()
    models = api.list_models(author=username)
    datasets = api.list_datasets(author=username)
    return sum(m.downloads for m in models) + sum(d.downloads for d in datasets)

def update_readme(forks, downloads):
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.readlines()

    for i, line in enumerate(content):
        if line.startswith("**Total Forks**:"):
            content[i] = f"**Total Forks**: {forks}\n"
        if line.startswith("**Total Model & Dataset Downloads**:"):
            content[i] = f"**Total Model & Dataset Downloads**: {downloads}\n"

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.writelines(content)

if __name__ == "__main__":
    forks = get_total_forks(USERNAME)
    downloads = get_hf_downloads(USERNAME)
    update_readme(forks, downloads)
