import dns.resolver
import webbrowser
import sys

def resolve_shortlink(subdomain, domain="pcorral.es"):
    fqdn = f"{subdomain}.{domain}"
    try:
        answers = dns.resolver.resolve(fqdn, 'TXT')
        for rdata in answers:
            url = str(rdata.strings[0], "utf-8")
            print(f"Resolved {fqdn} → {url}")
            webbrowser.open(url)
            return
    except Exception as e:
        print(f"Error resolving {fqdn}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python shortener.py <shortcode>")
    else:
        resolve_shortlink(sys.argv[1])
