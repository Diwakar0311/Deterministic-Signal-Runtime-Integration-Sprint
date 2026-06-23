import json

with open("traffic.json", "r") as file:
    signals = json.load(file)

for run in [100, 500, 1000]:

    count = 0

    while count < run:

        for signal in signals:

            count += 1

            if count >= run:
                break

    print(f"Load Test Passed : {run}")