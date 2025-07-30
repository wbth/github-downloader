import os
import requests

GITHUB_API = "https://api.github.com/repos/PacktPublishing/CompTIA-A-Certification-Core-1---220-1101/contents/Slide%20Handout%20PDFs%201101"
OUTPUT_DIR = "slide_handouts_1101"

def list_files():
    """Dapatkan daftar file di direktori GitHub via GitHub Contents API."""
    resp = requests.get(GITHUB_API)
    resp.raise_for_status()
    entries = resp.json()
    return [e for e in entries if e.get("type") == "file"]

def download_file(file_entry):
    """Download file PDF dari download_url di entry."""
    url = file_entry['download_url']
    name = file_entry['name']
    print(f"→ Mengunduh: {name}")
    r = requests.get(url)
    r.raise_for_status()
    with open(os.path.join(OUTPUT_DIR, name), "wb") as f:
        f.write(r.content)

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    files = list_files()
    print(f"Ditemukan {len(files)} file dalam direktori:")
    for f in files:
        print(" -", f['name'])
    for f in files:
        download_file(f)
    print("Selesai.")

if __name__ == "__main__":
    main()

