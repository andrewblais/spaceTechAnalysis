import csv
import os
import pandas as pd

from new_csv_entries_list import new_csv

new_len = range(len(new_csv))

cwd = os.getcwd()  # E:\nowGitRepos\spaceTechAnalysis
dir_path = f"{cwd}\scrapeStuff"

csv_file = "E:/nowGitRepos/spaceTechAnalysis/scrapeStuff/mission_launches_old.csv"
df_old = pd.read_csv(csv_file)
df_old = df_old.drop(["Unnamed: 0"], axis=1)

df_new = pd.DataFrame(new_csv)

df_complete = pd.concat([df_new, df_old], ignore_index=True)
# This keeps popping up, so I'll drop it:
df_complete = df_complete.drop(["Unnamed: 0.1"], axis=1)
df_complete = df_complete.reindex(columns=[
                                  "Organisation", "Location", "Date", "Detail", "Rocket_Status", "Price", "Mission_Status"])
# Add the mysterious duplicate index column:
# df_complete.insert(0, "Unnamed: 0", df_complete.index)
df_complete.to_csv(f"{dir_path}\mission_launches.csv", index=True)

# Everything looks good now, the CSV is updated after the scrape and concatenation!
