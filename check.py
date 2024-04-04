import requests
import re

def main():
    domain = '129scales.com'
    try:
        response = requests.head(
            'http://' + domain,
            allow_redirects=True,
            timeout=30
        )
        print("Response: ", response.url)
    except Exception as e:
        
        host_match = re.search(r"host='(.*?)'", str(e))
        if host_match:
            host_value = host_match.group(1)
            print('1 - ',domain)
            print('2 - ',host_value)
            if host_value != domain:
                print('add redirection')
            
def main():
    domain = '129scales.com'
    try:
        response = requests.head('http://' + domain, allow_redirects=True, timeout=30)
        print("Response: ", response.url)
    except requests.exceptions.RequestException as e:
        host_match = re.search(r"host='(.*?)'", str(e))
        if host_match and host_match.group(1) != domain:
            print('1 - ',domain)
            print('2 - ',host_match.group(1))

if __name__ == "__main__":
    main()