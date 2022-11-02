from datetime import timedelta
import sys
sys.path.append("..")

from progress import *
from config import *
from constants import *

project = "containers"
dateStr = "2022-10-10"

progress = Progress( PROGRESS_URL, PROGRESS_KEY)

issues = progress.issues(project, [
    progress.filter_tracker(TRACKER_ACTION),
    progress.filter_date(DATE_UPDATED, 10, DATE_COMPARATION_LESS_THAN_DAYS_AGO)
])

issues.reloadJournals(progress)

print(f"Stats since {dateStr}")
start_date = datetime.strptime(dateStr, "%Y-%m-%d")
for d in range(10):
    date = start_date + timedelta(days=d)
    issues = issues.snapshot(date)
    print(date)
    print(issues.stats_status())