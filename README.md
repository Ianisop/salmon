# 🐟 Salmon

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Version](https://img.shields.io/badge/version-1.0.0-blue)

Salmon is a command-line utility to upload and manage code snippets or file content on [Pastebin](https://pastebin.com). It supports batch uploads, recursive directory scanning, file-type filtering, and configurable privacy and expiration options.

## 🚀 Features

- ✅ Upload one or more files directly to Pastebin  
- 🔒 Set privacy options: Public or Unlisted  
- ⏳ Configure expiration: 10 minutes, 1 hour, 1 day, up to 1 year  
- 📁 Upload all files from a directory (with optional recursion)  
- 🎯 File type filtering (e.g., `.py`, `.cpp`)  
- 🔑 Load API key securely from `.env` or pass via CLI  

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/salmon.git
cd salmon
pip install -r requirements.txt
```
> **Pro-Tip:** Simply drop salmon.py outside the root directory of your project and pass -r and -d

> **Note:** Salmon requires Python 3.7+

---

## 🛠️ Setup

Create a `.env` file in the root directory with your Pastebin API key:

```env
API_KEY=your_pastebin_api_key
```

Alternatively, you can pass the API key via the `--key` flag.

---

## 🧪 Usage

### Upload specific files:
```bash
python salmon.py -f file1.py file2.py -p 1 -e 10M
```

### Upload files from a directory:
```bash
python salmon.py -d ./scripts -p 0 -e 1H --type py
```

### Recursive directory upload:
```bash
python salmon.py -d ./projects -r -p 1 -e 1D --type txt
```

### With API key passed directly:
```bash
python salmon.py -f main.cpp -p 1 -e 1W -k YOUR_API_KEY
```

---

## 🧾 CLI Options

| Flag               | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `-f`, `--files`     | List of individual files to upload                                          |
| `-p`, `--privacy`   | Privacy: `0` = public, `1` = unlisted                                       |
| `-e`, `--expiry`    | Expiration: `N`, `10M`, `1H`, `1D`, `1W`, `2W`, `1M`, `6M`, `1Y`             |
| `-d`, `--dir`       | Directory to scan for files (default: current dir)                          |
| `-r`, `--recursive` | Recursively scan subdirectories                                              |
| `-t`, `--type`      | File extension filter (e.g., `py`, `txt`)                                   |
| `-k`, `--key`       | Pastebin API key (overrides `.env` config)                                 |

---

## 📄 Example Output

```bash
API KEY FOUND: abc123...
Paste URLs:
https://pastebin.com/AbcD1234
https://pastebin.com/Xyz9876
```

---

## 📌 License

This project is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

---

## 🙋‍♂️ Author

Made by [somethingfishy](https://github.com/Ianisop)
