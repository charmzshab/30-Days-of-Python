import json
import time
import requests

url = "https://formulae.brew.sh/api/formula.json"
r = requests.get(url)

packages_json = r.json()
packages_str = json.dumps(packages_json, indent=2)  # json containing all packages
# we use dumps --> when we writing to a string

results = []

t1 = time.perf_counter()

for package in packages_json:
    package_name = package["name"]
    package_desc = package["desc"]

    package_url = f"https://formulae.brew.sh/api/formula/{package_name}.json"

    r = requests.get(package_url)  # response
    package_json = r.json()

    installs_30 = package_json["analytics"]["install_on_request"]["30d"][package_name]
    installs_90 = package_json["analytics"]["install_on_request"]["90d"][package_name]
    installs_365 = package_json["analytics"]["install_on_request"]["365d"][package_name]

    data = {
        "name": package_name,
        "desc": package_desc,
        "analytics": {"30d": installs_30, "90d": installs_90, "365d": installs_365},
    }

    results.append(data)
    time.sleep(
        r.elapsed.total_seconds()
    )  # sleeps the program for the duration it took to get back a response to prevent multiple api request hammering the server
    # the time lag defined is the total number of seconds it took to get back the response(r)
    print(f"Got {package_name} in {r.elapsed.total_seconds()} seconds")

    break

t2 = time.perf_counter()
print(f"Finished in {t2-t1} seconds")

with open("packages_info.json", "w") as f:
    json.dump(results, f, indent=2)
