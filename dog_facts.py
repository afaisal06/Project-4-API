import requests

# Retrieve 5 dog facts from the Dog API by kinduff
url = "https://dogapi.dog/api/v2/facts?limit=5"

response = requests.get(url, timeout=15)
response.raise_for_status()

# Extract the dog facts
data = response.json()
facts = [item["attributes"]["body"] for item in data["data"]]

# Calculate the average length of the facts
average = sum(len(fact) for fact in facts) / len(facts)

print("Total dog facts:", len(facts))
print("Average fact length:", round(average, 2))

# Find the 3 longest dog facts
print("\nThree longest dog facts:")
for fact in sorted(facts, key=len, reverse=True)[:3]:
    print("-", fact)
