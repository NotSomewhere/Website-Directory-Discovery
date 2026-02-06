# Website Directory Discovery (WDD)

A fast, lightweight command-line tool for discovering hidden directories and paths on websites using wordlists.

Website Directory Discovery (WDD) is designed for **penetration testing, security research, and reconnaissance** workflows.  
It provides a simple, efficient way to enumerate common and custom paths on a target web server.

---

## ✨ Features

- 🚀 Fast directory enumeration
- 📄 Custom wordlist support
- 🧵 Optional multi-threaded scanning
- 📊 HTTP status code detection
- ⏱️ Configurable timeout and delay
- 🖥️ Clean CLI output
- 🐍 Written in Python, easy to extend

---

## 📦 Installation

Clone the repository and install it locally:

```bash
git clone https://github.com/NotSomewhere/Website-Directory-Discovery.git
cd Website-Directory-Discovery
python -m pip install -e .
```

Python 3.9+ recommended

## 🚀 Usage

Basic scan with a target domain and a wordlist:

```bash
wdd example.com wordlist.txt
```

Example

```bash
wdd https://example.com common.txt
```

Output example:

```
found: https://example.com/admin (200)
found: https://example.com/login (302)
found: https://example.com/dashboard (403)
```

## ⚙️ Options

| Option | Description |
| --- | --- |
| -o, --output | Save results to a file |
| --status | Filter by HTTP status codes |
| --timeout | Request timeout (seconds) |
| --delay | Delay between requests |
| --user-agent | Custom User-Agent |

## 📁 Wordlists

You can use any wordlist you want.

Example:

```
admin
login
dashboard
uploads
backup
api
```

For best results, use curated wordlists from SecLists or your own custom lists.

## 🧠 Use Cases

- Web application reconnaissance
- Directory brute forcing
- CTF challenges
- Security testing labs
- Learning web enumeration techniques

## ⚠️ Legal Disclaimer

This tool is intended for educational and authorized security testing only.

You are responsible for ensuring you have explicit permission to test any target.
The author is not responsible for misuse or illegal activity.

## 🛠️ Development

Contributions are welcome.

- Fork the repository
- Create a new branch
- Commit your changes
- Open a Pull Request
- Clean code, clear commits, and meaningful descriptions are appreciated.

## 📄 License

This project is licensed under the MIT License.
See the LICENSE file for more details.

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub.


