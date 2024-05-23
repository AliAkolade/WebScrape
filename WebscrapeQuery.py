# "IT OR Information Technology", "Engineering", "Teaching", "Health Care", "Social Care", "Health and Safety"
niches = ["Social Care"]

# "@gmail.com", "@yahoo.com", ".co.uk", "+44", "Tel"
scraped = ["@gmail.com", "+44"]

# Sites: "uk.linkedin.com/in", "uk.linkedin.com/company", "indeed.com"
sites = ["uk.linkedin.com/in"]
location = "UK OR United Kingdom OR England"

for site in sites:
    for niche in niches:
        for scrape in scraped:
            print("\"" + scrape + "\" + " + niche + " + " + location + " + site:" + site)
