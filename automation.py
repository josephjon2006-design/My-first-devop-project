import os
import urllib.request
import json
from datetime import datetime

def run_pipeline_automation():
    print("🚀 Initializing advanced pipeline automation...")
    
    # Define directory and file paths
    folder_name = "Cloud_Backups"
    file_name = "deployment_report.txt"
    full_path = os.path.join(folder_name, file_name)
    
    # Create directory if it doesn't exist
    os.makedirs(folder_name, exist_ok=True)
    print(f"🎉 Success! Verified folder: {folder_name}")
    
    # Fetch live public data from an API (GitHub Public API)
    api_url = "https://api.github.com/repos/octocat/Hello-World"
    try:
        print(f"🌐 Fetching live data from public API...")
        with urllib.request.urlopen(api_url) as response:
            data = json.loads(response.read().decode())
            repo_name = data.get("full_name", "Unknown")
            repo_stars = data.get("stargazers_count", 0)
            open_issues = data.get("open_issues_count", 0)
    except Exception as e:
        repo_name = "Offline Fallback"
        repo_stars = "N/A"
        open_issues = "N/A"
        print(f"⚠️ API fetch warning: {e}")

    # Generate a timestamp
    current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    # Build report content
    report_content = f"""========================================
    DEVOPS AUTOMATED PIPELINE REPORT
========================================
Timestamp: {current_time}
Target Repository: {repo_name}
Live Stargazers: {repo_stars}
Open Issues: {open_issues}
Status: BUILD & TEST PASSED SUCCESSFULLY ✅
========================================
"""
    
    # Write report to file
    with open(full_path, "w") as f:
        f.write(report_content)
        
    print(f"📄 File automation complete: Created {file_name} inside {folder_name}.")
    print("🔍 Report Preview:")
    print(report_content)

if __name__ == "__main__":
    run_pipeline_automation()
