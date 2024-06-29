import os
import asyncio
import requests
from colorama import Fore, Style, init

init(autoreset=True)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_terminal()
    banner = f"""
{Fore.CYAN}
     _____       _     ______ _           _
  / ____|     | |   |  ____(_)         | |
 | (___  _   _| |__ | |__   _ _ __   __| | ___ _ __
  \___ \| | | | '_ \|  __| | | '_ \ / _` |/ _ \ '__|
  ____) | |_| | |_) | |    | | | | | (_| |  __/ |
 |_____/ \__,_|_.__/|_|    |_|_| |_|\__,_|\___|_|

{Style.RESET_ALL}
    """
    print(banner)

async def request(url, html_file, proxy=None):
    try:
        if proxy:
            result = await asyncio.get_event_loop().run_in_executor(None, requests.get, f"https://{url}", {"proxies": proxy})
        else:
            result = await asyncio.get_event_loop().run_in_executor(None, requests.get, f"https://{url}")

        if result.status_code == 200:
            print(f"{Fore.GREEN}[+] SubDomain found ----->> {url} [OK]{Style.RESET_ALL}")
            save_subdomain(url, html_file)
            return url
    except Exception as e:
        pass
    return None

def save_subdomain(subdomain, html_file):
    with open(html_file, "a") as file:
        file.write(f'<li><a href="https://{subdomain}" target="_blank">{subdomain}</a></li>\n')

def get_proxies():
    response = requests.get("https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc")
    if response.status_code == 200:
        proxies = response.json()["data"]
        formatted_proxies = [
            {"http": f"socks4://{proxy['ip']}:{proxy['port']}", "https": f"socks4://{proxy['ip']}:{proxy['port']}"}
            for proxy in proxies if "socks4" in proxy["protocols"]
        ]
        return formatted_proxies
    return []

async def main():
    print_banner()
    
    total_subdomains = 10000
    target_url = str(input(f"{Fore.CYAN}[+] Enter Url ---->> {Style.RESET_ALL}"))
    html_file_name = str(input(f"{Fore.CYAN}[+] Enter the name for the HTML results file ---->> {Style.RESET_ALL}"))

    if not html_file_name.endswith(".html"):
        html_file_name += ".html"

    with open(html_file_name, "w") as html_file:
        html_file.write(f"""
        <html>
        <head>
            <title>Subfinder Results</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    color: #333;
                    margin: 0;
                    padding: 20px;
                }}
                h1 {{
                    color: #4CAF50;
                }}
                h2 {{
                    color: #333;
                }}
                ol {{
                    list-style-type: none;
                    padding: 0;
                }}
                li {{
                    background: #e2e2e2;
                    margin: 5px 0;
                    padding: 10px;
                    border-radius: 5px;
                }}
                .container {{
                    max-width: 800px;
                    margin: auto;
                    background: #fff;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }}
                .footer {{
                    text-align: center;
                    margin-top: 20px;
                    color: #888;
                }}
                .warning {{
                    color: #ff0000;
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Subfinder Results</h1>
                <h2>Created by Sujal Choudhury</h2>
                <p class="warning">This is for educational purposes only. Please do not try for illegal purposes. If you try this for illegal purposes, the developer is not responsible.</p>
                <p><strong>Target URL:</strong> {target_url}</p>
                <p><b>List Of Subdomains :</b></p>
                
                <ol>
        """)

    use_proxy = str(input(f"{Fore.CYAN}[+] Do you want to use proxies? (yes/no) ---->> {Style.RESET_ALL}")).strip().lower()
    proxies = get_proxies() if use_proxy == 'yes' else None

    try:
        print(f"{Fore.YELLOW}[+] All Sub Domains are saved in {html_file_name}.html")
        print(f"{Fore.YELLOW}[+] If you want to stop process in mid, click 'CTRL + c'")
        
        with open("subdomains.txt", "r") as subdomains:
            tasks = []
            for domain in subdomains:
                subdomain = domain.strip()
                target_domain = subdomain + "." + target_url
                proxy = proxies.pop() if proxies else None
                task = asyncio.create_task(request(target_domain, html_file_name, proxy))
                tasks.append(task)

            await asyncio.gather(*tasks)

        print(f"{Fore.GREEN}[+] Process completed. Please see the HTML file: {html_file_name}")
        
    except KeyboardInterrupt:
        pass

        with open(html_file_name, "a") as html_file:
            html_file.write("""
                </ol>
                <div class="footer">
                    <p>&copy; 2024 Subfinder by Sujal Choudhury</p>
                </div>
            </div>
        </body>
        </html>
        """)

if __name__ == "__main__":
    asyncio.run(main())