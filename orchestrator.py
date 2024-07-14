import requests
import sys
import base64
import json

# Variables
org_name = "amsilf"
project_name = "SC-Assignment"
pipeline_id_1 = 4
pipeline_id_2 = 6
pipeline_id_3 = 5
personal_access_token = sys.argv[2]

# Determine which pipeline to trigger based on your logic
def decide_pipeline():
    # Implement your logic here
    result = sys.argv[1]  # Replace this with your actual condition logic
    if result == "terraform":
        return pipeline_id_1
    elif result == "docker":
        return pipeline_id_2
    elif result == "helm":
        return pipeline_id_3

selected_pipeline_id = decide_pipeline()

# Trigger the selected pipeline
authorization = str(base64.b64encode(bytes(':'+ personal_access_token, 'ascii')), 'ascii')

url = f"https://dev.azure.com/{org_name}/{project_name}/_apis/pipelines/{selected_pipeline_id}/runs?api-version=6.1-preview.1"
response = requests.post(
    url,
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Basic {authorization}"
    },
    data=json.dumps({})
)

print(response.text)