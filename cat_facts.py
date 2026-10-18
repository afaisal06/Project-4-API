
import requests

# Retrieve 10 cat facts
url = "https://catfact.ninja/facts?limit=10"
response = requests.get(url)
response.raise_for_status()

data = response.json()
facts = [item["fact"] for item in data["data"]]

# Calculate average length
average = sum(len(fact) for fact in facts) / len(facts)

print("Average length:", round(average, 2))

# Display the three longest facts
print("\nThree longest cat facts:")
for fact in sorted(facts, key=len, reverse=True)[:3]:
    print("-", fact)
