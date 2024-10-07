import requests


def extract(
    data="biopics.csv",
    file_path="data/biopics.csv",
):
    with requests.get(data) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
        return file_path
