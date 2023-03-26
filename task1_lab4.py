country_capitals = {
  "France": "Paris",
  "United States": "Washington, D.C.",
  "India": "New Delhi",
  "Russia": "Moscow",
  "China": "Beijing"
}
sorted_country_capitals = {k: v for k, v in sorted(country_capitals.items())}
for country, capital in sorted_country_capitals.items():
  print(f"{country}: {capital}")
