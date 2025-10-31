from flask import Flask, redirect, abort
import dns.resolver

app = Flask(__name__)

BASE_DOMAIN = "pcorral.es"

@app.route("/<shortcode>")
def redirect_from_dns(shortcode):
    fqdn = f"{shortcode}.{BASE_DOMAIN}"
    try:
        answers = dns.resolver.resolve(fqdn, 'TXT')
        for rdata in answers:
            txt_value = b''.join(rdata.strings).decode('utf-8')
            if txt_value.startswith("http"):
                return redirect(txt_value, code=302)
        abort(404)
    except Exception as e:
        print(f"Error resolving {fqdn}: {e}")
        abort(404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
