import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

years = list(range(2022, 2020, -1))
all_matches = []

# Get the standings page for the current year.
standings_url = "https://fbref.com/en/comps/9/Premier-League-Stats"
data = requests.get(standings_url)
soup = BeautifulSoup(data.text, features="lxml")

# Loop through all the teams in the standings and get their shooting data.
for year in years:

    # Get the href for the team's page.
    standings_table = soup.select('table.stats_table')[0]
    links = [l.get("href") for l in standings_table.find_all('a')]
    links = [l for l in links if '/squads/' in l]
    team_urls = [f"https://fbref.com{l}" for l in links]

    # Get the team's name.
    previous_season = soup.select("a.prev")[0].get("href")
    standings_url = f"https://fbref.com{previous_season}"

    for team_url in team_urls:

        # Get the team's match data.
        team_name = team_url.split("/")[-1].replace("-Stats", "").replace("-", " ")
        data = requests.get(team_url)
        matches = pd.read_html(data.text, match="Scores & Fixtures")[0]

        # Get the team's shooting data.
        soup = BeautifulSoup(data.text, features="lxml")
        links = [l.get("href") for l in soup.find_all('a')]
        links = [l for l in links if l and 'all_comps/shooting/' in l]
        data = requests.get(f"https://fbref.com{links[0]}")
        shooting = pd.read_html(data.text, match="Shooting")[0]
        shooting.columns = shooting.columns.droplevel()

        # Join the match data and shooting data on date.
        try:
            team_data = matches.merge(shooting[["Date", "Sh", "SoT", "Dist", "FK", "PK", "PKatt"]], on="Date")
        except ValueError:
            continue

        # Add the season and team name to the data.
        team_data["Season"] = year
        team_data["Team"] = team_name

        # Add the data to the list of all matches.
        all_matches.append(team_data)

        # Sleep for 1 second to avoid overloading the server.
        time.sleep(1)

# Combine all the match data into a single DataFrame.
match_df = pd.concat(all_matches)


match_df.columns = [c.lower() for c in match_df.columns]

# Print the DataFrame.
print(match_df)

# Save the DataFrame to a CSV file.
match_df.to_csv("matches.csv")
