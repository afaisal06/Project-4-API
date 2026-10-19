import requests

# Retreive dog breed information from the API
url = "https://dog.ceo/api/breeds/list/all"
response = requests.get(url)
response.raise_for_status()

# Extract dog breeds
data = response.json()
breeds = data["message"]

# Count the toral number of main breeds
print"Total dog breeds:", len(breeds))

# Calculate how many sub_breeds each bread has
subbreed_counts = {
  breed: len(subreeds)
  for breed, subbreeds in breeds.items()
}

# Find the 5 breeds with the most sub-breeds
top_five =sorted(
  subreed_counts.items(),
  key=lambda item: item[1],
  reverse=True
)[:5]

print("\nTop 5 breeds with the most sub-breeds:")

for breed, count in top_five:
  print(breed, "i", count, "sub-breeds")
