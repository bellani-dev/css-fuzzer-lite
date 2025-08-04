# ⚔️ XSS-Fuzzer-Lite

Uma ferramenta leve de fuzzing para identificar possíveis vulnerabilidades de Cross-Site Scripting (XSS) em URLs com parâmetros.

## ✨ O que ela faz?

Essa ferramenta realiza testes automatizados de XSS utilizando uma wordlist básica de payloads diretamente pela linha de comando.

## 🧠 Como funciona?

- O usuário informa a URL com parâmetro vulnerável (ex: `https://site.com/page?q=`)
- O script injeta diversos payloads XSS conhecidos
- Se um payload for refletido na resposta, ele marca como possível XSS

## 🚀 Uso

```bash
python3 xss-fuzzer-lite.py
```

Digite a URL com parâmetro vulnerável quando solicitado. Exemplo:

```
https://vulnsite.com/search?q=
```

## 🧪 Exemplo de payloads utilizados

```html
<script>alert(1)</script>
'><svg/onload=alert(1)>
<img src=x onerror=alert(1)>
<iframe src='javascript:alert(1)'></iframe>
```

## ⚠️ Aviso

Use apenas para fins educacionais e em ambientes autorizados. Testar sem permissão pode ser considerado ilegal.
