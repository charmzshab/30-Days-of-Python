import json


def install_sort(package):  # sorting function that sorts in ascending
    return package["analytics"]["30d"]


with open("package_info.json", "r") as f:
    data = json.load(f)

data.sort(
    key=install_sort, reverse=True
)  # with reverse=True the results will b descending
data = [
    item for item in data if "video" in item["desc"]
]  # retrieves all packages with video in their description
data_str = json.dumps(data, indent=2)
print(data_str)
