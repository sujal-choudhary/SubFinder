# SubFinder

Subdomain Finder is a Python script that utilizes asyncio to asynchronously discover subdomains for a given target domain. It fetches potential subdomains from a list and checks their existence using HTTP requests. Discovered subdomains are saved in an HTML report.

## Features

- Asynchronously checks subdomains for a given target domain.
- Supports proxy usage for enhanced anonymity during subdomain discovery.
- Saves discovered subdomains in an HTML report for easy inspection.
- Customizable HTML report styling with CSS.
- Fastest Scanner.
- In this tool they have 10000+ subdomains for check.

## Prerequisites

- Python 3.7 or higher
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sujal-choudhary/subdomain-finder.git
   cd SubFinder
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```bash
   python finder.py
   ```

2. Follow the prompts:
   - Enter the target domain (e.g., example.com).
   - Provide a name for the HTML report file (optional, defaults to `results.html`).

3. Choose whether to use proxies (optional).

4. Monitor the script's progress in the terminal. Press `CTRL + C` to stop the process if needed.

5. Once completed, check the generated HTML report (`results.html` by default) for subdomain results.

## Example

Here's a brief example of how to use the script:

```bash
python finder.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Colorama](https://pypi.org/project/colorama/) - for terminal text color formatting.
- [Requests](https://docs.python-requests.org/en/master/) - for making HTTP requests.
- [Asyncio](https://docs.python.org/3/library/asyncio.html) - for asynchronous programming in Python.

---

**Note:** This script is intended for educational purposes only. Use responsibly and respect the privacy and security of others.



