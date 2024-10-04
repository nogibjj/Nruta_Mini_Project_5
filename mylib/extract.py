import requests


def extract(
    url="https://github.com/fivethirtyeight/data/raw/refs/heads/master/biopics/biopics.csv",
    file_path="data/Biopics.csv",
):
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
        return file_path
