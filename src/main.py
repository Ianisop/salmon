import requests, os, time
from dotenv import load_dotenv

files = ["file1.txt", "file2.txt"]  

url = "https://pastebin.com/api/api_post.php"
pastedFiles = []

load_dotenv()
API_KEY = os.getenv("API_KEY")

if API_KEY:
    print("API KEY FOUND:", API_KEY)
else:
    print("API KEY NOT FOUND. Configure it in a .env file in the root dir.")
    exit()

def create_pastebin_url(pasteName, contents, privacy, expiry):
    payload = {
        'api_dev_key': API_KEY,
        'api_option': 'paste',
        'api_paste_code': contents,
        'api_paste_name': pasteName,
        'api_paste_private': str(int(privacy)),     
        'api_paste_expire_date': expiry            
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        pastedFiles.append(response.text)
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    privacy = input("What privacy option would you like? (0:PUBLIC | 1:UNLISTED): ").strip()
    expiry = input("What expiry time would you like? (N, 10M, 1H, 1D, 1W, 2W, 1M, 6M, 1Y): ").strip()

    for file in files:
        try:
            with open(file) as f:
                content = f.read()
                create_pastebin_url(file, content, privacy, expiry)
        except FileNotFoundError:
            print(f"File not found: {file}")
    
    print("Paste URLs:")
    print("\n".join(pastedFiles))
