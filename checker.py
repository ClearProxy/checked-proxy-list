import os  
import json 
import requests
from pathlib import Path 
from typing import List, Dict, Set
from collections import Counter 
from datetime import datetime, timedelta

CLEARPROXY_API_KEY = os.environ.get('CLEARPROXY_API_KEY')
CLEARPROXY_API_URL = 'https://api.clearproxy.io'

PROXY_SOURCES = {
'http': [
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
    'https://raw.githubusercontent.com/gitrecon1455/fresh-proxy-list/refs/heads/main/proxylist.txt',
    'https://raw.githubusercontent.com/r00tee/Proxy-List/refs/heads/main/Https.txt',
    'https://raw.githubusercontent.com/Vann-Dev/proxy-list/refs/heads/main/proxies/http.txt',
    'https://raw.githubusercontent.com/Vann-Dev/proxy-list/refs/heads/main/proxies/https.txt',
    'https://raw.githubusercontent.com/elliottophellia/proxylist/master/results/pmix_checked.txt',
    'https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt',
    'https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt',
    'https://raw.githubusercontent.com/andigwandi/free-proxy/main/proxy_list.txt',
    'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt',
    'https://raw.githubusercontent.com/mmpx12/proxy-list/master/proxies.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/all.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/all.txt',
    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
    'https://raw.githubusercontent.com/SevenworksDev/proxy-list/main/proxies/unknown.txt',
    'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
    'https://raw.githubusercontent.com/themiralay/Proxy-List-World/master/data.txt',
    'https://raw.githubusercontent.com/Tsprnay/Proxy-lists/master/proxies/http.txt',
    'https://raw.githubusercontent.com/TuanMinPay/live-proxy/master/http.txt',
    'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt',
    'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt',
    'https://github.com/zloi-user/hideip.me/raw/refs/heads/master/http.txt',
    'https://github.com/zloi-user/hideip.me/raw/refs/heads/master/connect.txt',
    'https://raw.githubusercontent.com/dinoz0rg/proxy-list/main/scraped_proxies/http.txt',
    'https://raw.githubusercontent.com/zebbern/Proxy-Scraper/main/http.txt',
    'https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/unchecked.txt',
    'https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/http.txt',
    'https://raw.githubusercontent.com/vmheaven/VMHeaven-Free-Proxy-Updated/main/http.txt',
    'https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/refs/heads/main/free.txt',
    'https://raw.githubusercontent.com/FifzzSENZE/Master-Proxy/master/proxies/http.txt',
    'https://raw.githubusercontent.com/fyvri/fresh-proxy-list/archive/storage/classic/http.txt',
    'https://github.com/handeveloper1/Proxy/raw/refs/heads/main/Proxies-Ercin/http.txt',
    'https://github.com/Anonym0usWork1221/Free-Proxies/raw/refs/heads/main/proxy_files/http_proxies.txt',
    'https://github.com/zenjahid/FreeProxy4u/raw/refs/heads/main/http.txt',
    'https://raw.githubusercontent.com/BreakingTechFr/Proxy_Free/refs/heads/main/proxies/http.txt',
    'https://raw.githubusercontent.com/VolkanSah/Auto-Proxy-Fetcher/refs/heads/main/proxies.txt',
    'https://raw.githubusercontent.com/databay-labs/free-proxy-list/refs/heads/master/http.txt',
    'https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/refs/heads/main/http.txt',
    'https://raw.githubusercontent.com/variableninja/proxyscraper/refs/heads/main/proxies/http.txt',
    'https://raw.githubusercontent.com/berkay-digital/Proxy-Scraper/refs/heads/main/proxies.txt',
    'https://github.com/XigmaDev/proxy/raw/refs/heads/main/proxies.txt',
    'https://github.com/chekamarue/proxies/raw/refs/heads/main/https.txt',
    'https://github.com/chekamarue/proxies/raw/refs/heads/main/httpss.txt',
    'https://github.com/claude89757/free_https_proxies/raw/refs/heads/main/https_proxies.txt',
    'https://github.com/claude89757/free_https_proxies/raw/refs/heads/main/isz_https_proxies.txt',
    'https://raw.githubusercontent.com/joy-deploy/free-proxy-list/refs/heads/main/data/latest/types/http/proxies.txt',
    'https://github.com/andigwandi/free-proxy/raw/refs/heads/main/proxy_list.txt',
    'https://raw.githubusercontent.com/parserpp/ip_ports/refs/heads/main/proxyinfo.txt',
    'https://raw.githubusercontent.com/Firmfox/Proxify/refs/heads/main/proxies/http.txt',
    'https://raw.githubusercontent.com/ebrasha/abdal-proxy-hub/refs/heads/main/http-proxy-list-by-EbraSha.txt',
    'https://rootjazz.com/proxies/proxies.txt',
    'https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=http&proxy_format=ipport&format=text&timeout=20000',
    'https://proxyspace.pro/http.txt',
],
'socks4': [
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
    'https://raw.githubusercontent.com/r00tee/Proxy-List/refs/heads/main/Socks4.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt',
    'https://raw.githubusercontent.com/Vann-Dev/proxy-list/refs/heads/main/proxies/socks4.txt',
    'https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/socks4/data.txt',
    'https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks4.txt',
    'https://raw.githubusercontent.com/andigwandi/free-proxy/main/proxy_list.txt',
    'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks4.txt',
    'https://raw.githubusercontent.com/gitrecon1455/fresh-proxy-list/refs/heads/main/proxylist.txt',
    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt',
    'https://raw.githubusercontent.com/SevenworksDev/proxy-list/main/proxies/unknown.txt',
    'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
    'https://raw.githubusercontent.com/themiralay/Proxy-List-World/master/data.txt',
    'https://raw.githubusercontent.com/Tsprnay/Proxy-lists/master/proxies/socks4.txt',
    'https://raw.githubusercontent.com/TuanMinPay/live-proxy/master/socks4.txt',
    'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt',
    'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt',
    'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks4.txt',
    'https://github.com/zloi-user/hideip.me/raw/refs/heads/master/socks4.txt',
    'https://raw.githubusercontent.com/dinoz0rg/proxy-list/main/scraped_proxies/socks4.txt',
    'https://raw.githubusercontent.com/zebbern/Proxy-Scraper/main/socks4.txt',
    'https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/unchecked.txt',
    'https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/socks4.txt',
    'https://raw.githubusercontent.com/vmheaven/VMHeaven-Free-Proxy-Updated/main/socks4.txt',
    'https://raw.githubusercontent.com/FifzzSENZE/Master-Proxy/master/proxies/socks4.txt',
    'https://raw.githubusercontent.com/fyvri/fresh-proxy-list/archive/storage/classic/socks4.txt',
    'https://github.com/handeveloper1/Proxy/raw/refs/heads/main/Proxies-Ercin/socks4.txt',
    'https://github.com/Anonym0usWork1221/Free-Proxies/raw/refs/heads/main/proxy_files/socks4_proxies.txt',
    'https://github.com/zenjahid/FreeProxy4u/raw/refs/heads/main/socks4.txt',
    'https://raw.githubusercontent.com/BreakingTechFr/Proxy_Free/refs/heads/main/proxies/socks4.txt',
    'https://raw.githubusercontent.com/VolkanSah/Auto-Proxy-Fetcher/refs/heads/main/proxies.txt',
    'https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/refs/heads/main/socks4.txt',
    'https://raw.githubusercontent.com/variableninja/proxyscraper/refs/heads/main/proxies/socks.txt',
    'https://raw.githubusercontent.com/joy-deploy/free-proxy-list/refs/heads/main/data/latest/types/socks4/proxies.txt',
    'https://raw.githubusercontent.com/parserpp/ip_ports/refs/heads/main/proxyinfo.txt',
    'https://raw.githubusercontent.com/Firmfox/Proxify/refs/heads/main/proxies/socks4.txt',
    'https://raw.githubusercontent.com/ebrasha/abdal-proxy-hub/refs/heads/main/socks4-proxy-list-by-EbraSha.txt',
],
'socks5': [
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
    'https://raw.githubusercontent.com/r00tee/Proxy-List/refs/heads/main/Socks5.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt',
    'https://raw.githubusercontent.com/Vann-Dev/proxy-list/refs/heads/main/proxies/socks5.txt',
    'https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/socks5/data.txt',
    'https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks5.txt',
    'https://raw.githubusercontent.com/andigwandi/free-proxy/main/proxy_list.txt',
    'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks5.txt',
    'https://raw.githubusercontent.com/gitrecon1455/fresh-proxy-list/refs/heads/main/proxylist.txt',
    'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt',
    'https://raw.githubusercontent.com/SevenworksDev/proxy-list/main/proxies/socks5.txt',
    'https://raw.githubusercontent.com/SevenworksDev/proxy-list/main/proxies/unknown.txt',
    'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
    'https://raw.githubusercontent.com/themiralay/Proxy-List-World/master/data.txt',
    'https://raw.githubusercontent.com/Tsprnay/Proxy-lists/master/proxies/socks5.txt',
    'https://raw.githubusercontent.com/TuanMinPay/live-proxy/master/socks5.txt',
    'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt',
    'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt',
    'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks5.txt',
    'https://github.com/zloi-user/hideip.me/raw/refs/heads/master/socks5.txt',
    'https://raw.githubusercontent.com/dinoz0rg/proxy-list/main/scraped_proxies/socks5.txt',
    'https://raw.githubusercontent.com/zebbern/Proxy-Scraper/main/socks5.txt',
    'https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/unchecked.txt',
    'https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/socks5.txt',
    'https://raw.githubusercontent.com/vmheaven/VMHeaven-Free-Proxy-Updated/main/socks5.txt',
    'https://raw.githubusercontent.com/FifzzSENZE/Master-Proxy/master/proxies/socks5.txt',
    'https://raw.githubusercontent.com/fyvri/fresh-proxy-list/archive/storage/classic/socks5.txt',
    'https://github.com/handeveloper1/Proxy/raw/refs/heads/main/Proxies-Ercin/socks5.txt',
    'https://github.com/Anonym0usWork1221/Free-Proxies/raw/refs/heads/main/proxy_files/socks5_proxies.txt',
    'https://github.com/zenjahid/FreeProxy4u/raw/refs/heads/main/socks5.txt',
    'https://raw.githubusercontent.com/BreakingTechFr/Proxy_Free/refs/heads/main/proxies/socks5.txt',
    'https://raw.githubusercontent.com/VolkanSah/Auto-Proxy-Fetcher/refs/heads/main/proxies.txt',
    'https://raw.githubusercontent.com/databay-labs/free-proxy-list/refs/heads/master/socks5.txt',
    'https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/refs/heads/main/socks5.txt',
    'https://raw.githubusercontent.com/variableninja/proxyscraper/refs/heads/main/proxies/socks.txt',
    'https://raw.githubusercontent.com/joy-deploy/free-proxy-list/refs/heads/main/data/latest/types/socks5/proxies.txt',
    'https://raw.githubusercontent.com/parserpp/ip_ports/refs/heads/main/proxyinfo.txt',
    'https://raw.githubusercontent.com/Firmfox/Proxify/refs/heads/main/proxies/socks5.txt',
    'https://raw.githubusercontent.com/ebrasha/abdal-proxy-hub/refs/heads/main/socks5-proxy-list-by-EbraSha.txt',
],
}

class ProxyChecker:
    def __init__(self):
        self.stats_file = Path('stats.json')
        self.initial_counts = self.load_stats()
        self.initial_proxies_dir = Path('.initial/misc')
        self.initial_proxies_dir.mkdir(parents=True, exist_ok=True)
        self.RESCRAPE_COOLDOWN = timedelta(hours=3)
        
    def load_stats(self) -> Dict:
        if self.stats_file.exists():
            with open(self.stats_file, 'r') as f:
                return json.load(f)
        return {
            'initial_http': 0, 
            'initial_socks4': 0, 
            'initial_socks5': 0,
            'last_rescrape_http': None,
            'last_rescrape_socks4': None,
            'last_rescrape_socks5': None
        }
    
    def save_stats(self, stats: Dict):
        with open(self.stats_file, 'w') as f:
            json.dump(stats, f, indent=2)

    def can_rescrape(self, protocol: str) -> bool:
        last_rescrape_key = f'last_rescrape_{protocol}'
        last_rescrape = self.initial_counts.get(last_rescrape_key)
        
        if not last_rescrape:
            return True
        
        try:
            last_time = datetime.fromisoformat(last_rescrape)
            time_since_rescrape = datetime.now() - last_time
            
            if time_since_rescrape < self.RESCRAPE_COOLDOWN:
                remaining = self.RESCRAPE_COOLDOWN - time_since_rescrape
                minutes = int(remaining.total_seconds() / 60)
                print(f"[{protocol.upper()}] Cooldown active. Wait {minutes} minutes")
                return False
            
            return True
        except:
            return True
    
    def scrape_proxies(self, protocol: str) -> Set[str]:
        proxies = set()
        sources = PROXY_SOURCES.get(protocol, [])
        
        print(f"[{protocol.upper()}] Scraping from {len(sources)} sources...")
        
        for idx, url in enumerate(sources, 1):
            try:
                response = requests.get(url, timeout=30)
                if response.status_code == 200:
                    lines = response.text.strip().split('\n')
                    valid_lines = [line.strip() for line in lines if line.strip() and ':' in line.strip()]
                    proxies.update(valid_lines)
                    print(f"[{protocol.upper()}] [{idx}/{len(sources)}] {len(valid_lines)} proxies")
            except:
                pass
        
        print(f"[{protocol.upper()}] Total collected: {len(proxies)}")
        return proxies
    
    def check_proxies_clearproxy(self, proxies: List[str], protocol: str) -> List[Dict]:
        if not CLEARPROXY_API_KEY:
            print("[ERROR] CLEARPROXY_API_KEY not found!")
            return []
        
        headers = {
            'X-API-Key': CLEARPROXY_API_KEY,
            'Content-Type': 'application/json'
        }
        
        print(f"[{protocol.upper()}] Checking {len(proxies)} proxies...")
        
        try:
            payload = {
                'proxies': proxies,
                'type': protocol,
                'region': "test1",
                'timeout': 2500
            }
            
            response = requests.post(
                f'{CLEARPROXY_API_URL}/check',
                headers=headers,
                json=payload,
                timeout=300
            )
            
            if response.status_code != 200:
                print(f"[ERROR] API returned status {response.status_code}")
                return []
            
            initial_result = response.json()
            result_url = initial_result.get('result_url')
            
            if not result_url:
                print("[ERROR] No result_url in API response")
                return []
            
            result_response = requests.get(result_url, timeout=60)
            
            if result_response.status_code != 200:
                print(f"[ERROR] Failed to fetch results")
                return []
            
            results = result_response.json()
            working_proxies = []
            proxies_array = results.get('proxies', [])
            
            for result in proxies_array:
                if result.get('status') == 'working':
                    proxy_info = result.get('proxy', {})
                    working_proxies.append({
                        'ip': proxy_info.get('host'),
                        'port': proxy_info.get('port'),
                        'country': result.get('country', 'Unknown'),
                        'country_code': result.get('country', 'XX'),
                        'asn': result.get('asn', 'Unknown'),
                        'isp': result.get('isp', 'Unknown'),
                        'protocol': protocol,
                        'speed_ms': result.get('responseTime', '0').replace(' ms', ''),
                        'anonymity': result.get('anonymity', 'unknown'),
                        'location': result.get('location', 'Unknown')
                    })
            
            print(f"[{protocol.upper()}] Found {len(working_proxies)} working proxies")
            return working_proxies
                
        except Exception as e:
            print(f"[ERROR] Failed to check proxies: {e}")
            return []
    
    def clean_old_files(self, base_path: Path):
        paths_to_clean = [
            base_path / 'raw' / 'country',
            base_path / 'raw' / 'asn',
            base_path / 'json' / 'country',
            base_path / 'json' / 'asn'
        ]
        
        for path in paths_to_clean:
            if path.exists():
                for file in path.iterdir():
                    if file.is_file():
                        file.unlink()
    
    def save_proxies(self, proxies: List[Dict], protocol: str):
        base_path = Path(protocol)
        raw_path = base_path / 'raw'
        json_path = base_path / 'json'
        
        raw_path.mkdir(parents=True, exist_ok=True)
        json_path.mkdir(parents=True, exist_ok=True)
        (raw_path / 'country').mkdir(exist_ok=True)
        (raw_path / 'asn').mkdir(exist_ok=True)
        (json_path / 'country').mkdir(exist_ok=True)
        (json_path / 'asn').mkdir(exist_ok=True)
        
        self.clean_old_files(base_path)
        
        with open(raw_path / 'all.txt', 'w') as f:
            for p in proxies:
                f.write(f"{p['ip']}:{p['port']}\n")
        
        with open(json_path / 'all.json', 'w') as f:
            json.dump(proxies, f, indent=2)
        
        by_country = {}
        for p in proxies:
            country = p.get('country_code', 'XX')
            if country not in by_country:
                by_country[country] = []
            by_country[country].append(p)
        
        for country, country_proxies in by_country.items():
            with open(raw_path / 'country' / f'{country}.txt', 'w') as f:
                for p in country_proxies:
                    f.write(f"{p['ip']}:{p['port']}\n")
            
            with open(json_path / 'country' / f'{country}.json', 'w') as f:
                json.dump(country_proxies, f, indent=2)
        
        by_asn = {}
        for p in proxies:
            asn = str(p.get('asn', 'Unknown'))
            if asn not in by_asn:
                by_asn[asn] = []
            by_asn[asn].append(p)
        
        for asn, asn_proxies in by_asn.items():
            safe_asn = str(asn).replace('/', '_').replace(' ', '_')
            with open(raw_path / 'asn' / f'{safe_asn}.txt', 'w') as f:
                for p in asn_proxies:
                    f.write(f"{p['ip']}:{p['port']}\n")
            
            with open(json_path / 'asn' / f'{safe_asn}.json', 'w') as f:
                json.dump(asn_proxies, f, indent=2)
        
        print(f"[{protocol.upper()}] Saved {len(proxies)} proxies")
    
    def update_readme(self, stats: Dict):
        all_proxies = []
        for protocol in ['http', 'socks4', 'socks5']:
            json_file = Path(protocol) / 'json' / 'all.json'
            if json_file.exists():
                with open(json_file, 'r') as f:
                    all_proxies.extend(json.load(f))
        
        country_counter = Counter([p.get('country', 'Unknown') for p in all_proxies])
        asn_counter = Counter([str(p.get('asn', 'Unknown')) for p in all_proxies])
        
        top_countries = ', '.join([f"{i+1}. {country} ({count})" for i, (country, count) in enumerate(country_counter.most_common(10))])
        top_asns = ', '.join([f"{i+1}. ASN{asn} ({count})" for i, (asn, count) in enumerate(asn_counter.most_common(10))])
        
        readme_content = f"""# ClearProxy.io Checked Proxy List

##  Description

This repository provides an **automatically updated proxy list every 5 minutes** with verified HTTP, SOCKS4, and SOCKS5 protocols ready to use.

### Validation Process

<div align="center">
  
**All proxies are checked and validated using:**

<a href="https://www.clearproxy.io/">
  <img src="https://www.clearproxy.io/logo_c.png" alt="ClearProxy.io" width="150"/>
</a>

**[ClearProxy.io](https://www.clearproxy.io/)** - Professional Proxy Validation Service

**Capable of checking millions of proxies in seconds**

</div>

Every proxy in this repository has been validated through **[ClearProxy.io](https://www.clearproxy.io/)**, a powerful service that can **check millions of proxies in seconds**, ensuring all proxies are active and usable.

---

##  Available Proxy Lists

| Protocol | File | Status | Total |
|-----------|------|--------|--------|
| HTTP | `http/` | ✅ Checked | {stats.get('http', 0):,} |
| SOCKS4 | `socks4/` | ✅ Checked | {stats.get('socks4', 0):,} |
| SOCKS5 | `socks5/` | ✅ Checked | {stats.get('socks5', 0):,} |

---

### Top 10 Countries
`{top_countries}`

### Top 10 ASN
`{top_asns}`

---

##  Download Options

### By Protocol - All Proxies

```bash
# HTTP - All proxies (raw format)
https://raw.githubusercontent.com/ClearProxy/checked-proxy-list/main/http/raw/all.txt

# HTTP - All proxies (JSON format)
https://raw.githubusercontent.com/ClearProxy/checked-proxy-list/main/http/json/all.json

# SOCKS4 - All proxies (raw format)
https://raw.githubusercontent.com/ClearProxy/checked-proxy-list/main/socks4/raw/all.txt

# SOCKS4 - All proxies (JSON format)
https://raw.githubusercontent.com/ClearProxy/checked-proxy-list/main/socks4/json/all.json

# SOCKS5 - All proxies (raw format)
https://raw.githubusercontent.com/ClearProxy/checked-proxy-list/main/socks5/raw/all.txt

# SOCKS5 - All proxies (JSON format)
https://raw.githubusercontent.com/ClearProxy/checked-proxy-list/main/socks5/json/all.json
```

### By Country Code

```bash
# HTTP - US proxies (raw format)
https://raw.githubusercontent.com/ClearProxy/checked-proxy-list/main/http/raw/country/US.txt

# HTTP - US proxies (JSON format)
https://raw.githubusercontent.com/ClearProxy/checked-proxy-list/main/http/json/country/US.json

# SOCKS5 - GB proxies (raw format)
https://raw.githubusercontent.com/ClearProxy/checked-proxy-list/main/socks5/raw/country/GB.txt
```

### By ASN Number

```bash
# HTTP - ASN specific (raw format)
https://raw.githubusercontent.com/ClearProxy/checked-proxy-list/main/http/raw/asn/12345.txt

# HTTP - ASN specific (JSON format)
https://raw.githubusercontent.com/ClearProxy/checked-proxy-list/main/http/json/asn/12345.json

# SOCKS5 - ASN specific (raw format)
https://raw.githubusercontent.com/ClearProxy/checked-proxy-list/main/socks5/raw/asn/12345.txt
```

## Format

### Raw Format (IP:PORT)
```
192.168.1.1:8080
10.0.0.1:1080
```

### JSON Format
```json
[
  {{
    "ip": "67.67.67.67",
    "port": 6767,
    "country": "US",
    "country_code": "US",
    "asn": 6767,
    "isp": "Six Seven LLC",
    "protocol": "http",
    "speed_ms": "664.05",
    "anonymity": "elite",
    "location": "The Dalles"
  }}
]
```

> [!WARNING]
> Proxies in this repository are collected from public sources
> Use wisely and in accordance with applicable laws
> Not responsible for proxy misuse
> Proxy speed and stability may vary

## Verification Powered By

<div align="center">

<a href="https://www.clearproxy.io/">
  <img src="https://www.clearproxy.io/logo_c.png" alt="ClearProxy.io" width="120"/>
</a>

**[ClearProxy.io](https://www.clearproxy.io/)**

*Professional proxy checking and validation service*

</div>

---

<div align="center">

**Maintained with ❤️ | Validated by [ClearProxy.io](https://www.clearproxy.io/)**

</div>
"""
        
        with open('README.md', 'w') as f:
            f.write(readme_content.encode('utf-8').decode('utf-8'))
        
        print("[README] Updated successfully")
    
    def load_initial_proxies(self, protocol: str) -> List[str]:
        initial_proxy_file = self.initial_proxies_dir / f'{protocol}.txt'
        if not initial_proxy_file.exists():
            return []
        
        with open(initial_proxy_file, 'r') as f:
            return [line.strip() for line in f if line.strip()]

    def save_initial_proxies(self, proxies: List[Dict], protocol: str):
        initial_proxy_file = self.initial_proxies_dir / f'{protocol}.txt'
        with open(initial_proxy_file, 'w') as f:
            for p in proxies:
                f.write(f"{p['ip']}:{p['port']}\n")
        print(f"[{protocol.upper()}] Saved to cache")
    
    def run(self):
        print("=" * 60)
        print("Starting Proxy Checker - Time Based (1 hour cooldown)")
        print("=" * 60)
        
        final_stats = {}
        
        for protocol in ['http', 'socks4', 'socks5']:
            print(f"\n{'='*60}")
            print(f"[{protocol.upper()}] Processing...")
            print(f"{'='*60}")
            
            existing_proxies = self.load_initial_proxies(protocol)
            
            if existing_proxies:
                print(f"[{protocol.upper()}] Found {len(existing_proxies)} cached proxies")
                
                working_proxies = self.check_proxies_clearproxy(existing_proxies, protocol)
                
                if self.can_rescrape(protocol):
                    print(f"[{protocol.upper()}] Cooldown expired. Rescraping...")
                    
                    new_proxies = self.scrape_proxies(protocol)
                    working_proxies = self.check_proxies_clearproxy(list(new_proxies), protocol)
                    
                    self.save_initial_proxies(working_proxies, protocol)
                    self.initial_counts[f'initial_{protocol}'] = len(working_proxies)
                    self.initial_counts[f'last_rescrape_{protocol}'] = datetime.now().isoformat()
                else:
                    print(f"[{protocol.upper()}] Using {len(working_proxies)} working proxies")
            else:
                print(f"[{protocol.upper()}] No cache. Performing initial scrape...")
                
                new_proxies = self.scrape_proxies(protocol)
                working_proxies = self.check_proxies_clearproxy(list(new_proxies), protocol)
                
                self.save_initial_proxies(working_proxies, protocol)
                self.initial_counts[f'initial_{protocol}'] = len(working_proxies)
                self.initial_counts[f'last_rescrape_{protocol}'] = datetime.now().isoformat()
            
            self.save_proxies(working_proxies, protocol)
            final_stats[protocol] = len(working_proxies)
        
        self.save_stats(self.initial_counts)
        self.update_readme(final_stats)
        
        print("\n" + "=" * 60)
        print("Proxy checking completed!")
        print("=" * 60)
        print(f"HTTP: {final_stats.get('http', 0):,} proxies")
        print(f"SOCKS4: {final_stats.get('socks4', 0):,} proxies")
        print(f"SOCKS5: {final_stats.get('socks5', 0):,} proxies")
        print(f"Total: {sum(final_stats.values()):,} proxies")
        print("=" * 60)

if __name__ == '__main__':
    checker = ProxyChecker()
    checker.run()

