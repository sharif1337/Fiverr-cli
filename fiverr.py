import requests
import re, time

try:
    print (" ---------------------------------------------------------------------------")
    print (" | PG No: |" + " " * 4 + "Seller Name".ljust(15) + "|".ljust(20) + "Title".ljust(25) + "|")
    print (" ---------------------------------------------------------------------------")

    for i in range(1,21):
        headers = {
            'authority': 'www.fiverr.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'if-none-match': 'W/"123276-7VC9s9ZeH/ydfaqTywIkQoYF57U"',
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        }

        params = {
            'query': 'professional shopify store design',
            'page': i,
        }

        url = requests.get('https://www.fiverr.com/search/gigs', params=params, headers=headers).text
        pattern = r'"seller_name":"([^"]+)",.*?,"title":"([^"]+)"'

        matches = re.findall(pattern, url)
        for match in matches:
            seller_name = match[0]
            title = match[1]
            print(f" |    {i}   | {seller_name.ljust(17)} | {title}")
    print (" ---------------------------------------------------------------------------")
            
except KeyboardInterrupt:
    print (" ---------------------------------------------------------------------------")
    print("\n > Exit...")
    exit()
