import requests, os, time, sys, argparse
from dotenv import load_dotenv


parser = argparse.ArgumentParser(description="Paste files to Pastebin")
parser.add_argument("-f", "--files", nargs='+', help="List of files to paste", required=True)
parser.add_argument("-p", "--privacy", type=int, choices=[0, 1], help="Privacy option: 0 for public, 1 for unlisted", required=True)
parser.add_argument("-e", "--expiry", type=str, help="Expiry time for the paste (N, 10M, 1H, 1D, 1W, 2W, 1M, 6M, 1Y)", required=True)
parser.add_argument("-d", "--dir", type=str, help="Directory containing files to paste", default=".")
parser.add_argument("-r", "--recursive", action='store_true', help="Recursively search for files in subdirectories")
parser.add_argument("-t", "--type", type=str, help="Type of files to paste (e.g., cpp, cs, py, txt)")
parser.add_argument("-k", "--key", type=str, help="API key for Pastebin (optional, will be loaded from .env file if not provided)")
args = parser.parse_args()

#handle the API key
if args.key:
    API_KEY = args.key
    print("API KEY PASSED AS PARAM:", API_KEY)
else:
    load_dotenv()
    API_KEY = os.getenv("API_KEY")

    if API_KEY:
        print("API KEY FOUND:", API_KEY)
    else:
        print("API KEY NOT FOUND. Configure it in a .env file in the root dir.")
        exit()


files = []
privacy = args.privacy  # Get the privacy argument
expiry = args.expiry  # Get the expiry argument

#Handle files from command line arguments
if args.files:
    for file in args.files:
        if os.path.isfile(file):
            if args.type:
                if file.endswith(f".{args.type}"):
                    files.append(file)
            else:
                files.append(file)
else:
    print("No files provided. Use -f or --files to specify files.")
    exit()

#if dir is provided, search for files in the directory
if args.dir:
    if args.recursive:
        for root, dirs, filenames in os.walk(args.dir):
            for filename in filenames:
                if args.type:
                    if filename.endswith(f".{args.type}"):
                        files.append(os.path.join(root, filename))
                else:
                    files.append(os.path.join(root, filename))

        

url = "https://pastebin.com/api/api_post.php"
pastedFiles = []


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
    for file in files:
        try:
            with open(file) as f:
                content = f.read()
                create_pastebin_url(file, content, privacy, expiry)
        except FileNotFoundError:
            print(f"File not found: {file}")
    
    print("Paste URLs:")
    print("\n".join(pastedFiles))
