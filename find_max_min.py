import requests

repository_owner = "nivi30"
repository_name = "dashboard"
access_token = "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"

url=f"https://api.github.com/repos/{repository_owner}/{repository_name}/actions/workflows/check.yml/runs"
headers = { "Authorization": f"token {access_token}" }
response = requests.get(url, headers=headers)
workflow_runs = response.json()["workflow_runs"]

max_run_time = None
min_run_time = None

for run in workflow_runs:
  duration = run["run_duration"]
  if max_run_time is None or duration > max_run_time:
    max_run_time = duration
  if min_run_time is None or duration < min_run_time:
    min_run_time = duration

print(f"Maximum run time : {max_run_time} seconds")
print(f"Minimum run time : {min_run_time} seconds")
