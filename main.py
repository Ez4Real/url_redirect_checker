import re
import csv
import requests
from urllib.parse import urlparse

def check_redirect(domain):
    url = 'http://' + domain
    print('URL ', url)
    try:
        response = requests.get(url, allow_redirects=True, timeout=30)
        final_url = urlparse(response.url).netloc
        print("Current URL: ", final_url)
        if domain != final_url:
            print('Redirect from ', domain, ' to ', final_url)
            return final_url, "Redirected"
        else:
            print('No redirect from ', domain)
            return None, "No Redirection"
    except requests.exceptions.RequestException as e:
        host_match = re.search(r"host='(.*?)'", str(e))
        if host_match and host_match.group(1) != domain:
            return host_match.group(1), f"Error: {e}"
        return None, f"Error: {e}"

def main():
    with open('domains.txt', 'r') as file:
        domains = file.read().splitlines()

    with open('output.csv', 'w', newline='') as csvfile:
        fieldnames = ['Domain', 'Redirect URL', 'Status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for index, domain in enumerate(domains):
            print(index+1, ' - ', domain)
            redirect_url, status = check_redirect(domain)
            writer.writerow({'Domain': domain, 'Redirect URL': redirect_url, 'Status': status})

if __name__ == "__main__":
    main()