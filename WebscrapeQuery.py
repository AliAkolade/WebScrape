# niches: "IT OR Information Technology", "Engineering", "Teaching", "Health Care", "Social Care", "Health and Safety"
niches = ["IT OR Information Technology", "Engineering"]

scraped = ["@gmail.com", "@yahoo.com", ".co.uk", "+44", "Tel"]

# Sites: "uk.linkedin.com/in", "uk.linkedin.com/company", "indeed.com"
sites = ["uk.linkedin.com/company"]
location = "UK OR United Kingdom OR England"

for site in sites:
    for niche in niches:
        for scrape in scraped:
            print("\"" + scrape + "\" + " + niche + " + " + location + " + site:" + site)
