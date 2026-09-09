import os

folder = "Cloud_Backups"

if not os.path.exists(folder):
    os.makedirs(folder)
    print("🎉 Success! Created folder: " + folder)
else:
    print("⚠️ Notice: Folder already exists.")
# Define the path for a new backup file
file_path = os.path.join(folder, "system_log.txt")

# Open the file and write a simulated backup message
with open(file_path, "w") as f:
    f.write("Backup Status: SUCCESS\n")
    f.write("All cloud systems are operating normally.\n")

print("📄 File automation complete: Created system_log.txt inside folder.")

