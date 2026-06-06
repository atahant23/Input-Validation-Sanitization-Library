from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from sanitizer import EnterpriseSecurityEngine, SecurityLevel

class AdvancedWafHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        html_form = """
        <html>
        <head>
            <title>BGT208 Next-Gen WAF Lab</title>
            <style>
                body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 40px; background-color: #1e1e24; color: #fff; }
                .container { max-width: 900px; margin: 0 auto; background: #2a2a35; padding: 30px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.5); }
                h2, h3 { color: #00adb5; }
                input[type="text"], select { width: 100%; padding: 12px; margin: 10px 0; border-radius: 6px; border: 1px solid #3f3f52; background: #1e1e24; color: #fff; font-size: 14px; }
                input[type="submit"] { background: #00adb5; color: #fff; border: none; padding: 14px 28px; border-radius: 6px; cursor: pointer; font-size: 16px; font-weight: bold; width: 100%; }
                input[type="submit"]:hover { background: #007a80; }
                .policy-box { background: #3f3f52; padding: 15px; border-radius: 6px; margin-bottom: 20px; border-left: 5px solid #ff414d; }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>🛡️ BGT208 Next-Gen WAF & Girdi Doğrulama Çekirdeği</h2>
                <p>Güvenlik motorunun katılık seviyesini seçin ve gerçek siber saldırı vektörlerini fırlatın.</p>
                
                <form method="POST" action="/submit">
                    <div class="policy-box">
                        <label><b>WAF Güvenlik Politikası Seviyesi (Security Policy Level):</b></label>
                        <select name="policy_level">
                            <option value="2">MEDIUM (Standart Filtreler Aktif)</option>
                            <option value="3" selected>HIGH (Agresif Bloklama ve SIEM Tetikleme)</option>
                            <option value="4">PARANOID (Sadece Alfanumerik Karakterler)</option>
                        </select>
                    </div>

                    <h3>1. Cross-Site Scripting (XSS) Alanı</h3>
                    <input type="text" name="xss_input" placeholder="<svg onload=alert(1)> veya polyglot yapılar...">

                    <h3>2. SQL Injection (SQLi) Alanı</h3>
                    <input type="text" name="sqli_input" placeholder="1' UNION SELECT @@version, null --">

                    <h3>3. OS Command Injection (RCE) Alanı</h3>
                    <input type="text" name="cmd_input" placeholder="127.0.0.1 ; cat /etc/passwd">

                    <br><br>
                    <input type="submit" value="Siber Saldırı Paketini WAF Engeline Gönder">
                </form>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html_form.encode("utf-8"))

    def do_POST(self):
        if self.path == "/submit":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            
            parsed_data = urllib.parse.parse_qs(post_data)
            policy_level = int(parsed_data.get('policy_level', [3])[0])
            xss_input = parsed_data.get('xss_input', [''])[0]
            sqli_input = parsed_data.get('sqli_input', [''])[0]
            cmd_input = parsed_data.get('cmd_input', [''])[0]
            
            # --- MOTOR ÇALIŞIYOR (SAVUNMA) ---
            clean_xss = EnterpriseSecurityEngine.sanitize_xss(xss_input, policy=policy_level)
            clean_sqli = EnterpriseSecurityEngine.sanitize_sqli(sqli_input, policy=policy_level)
            clean_cmd = EnterpriseSecurityEngine.sanitize_os_command(cmd_input, policy=policy_level)
            
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            
            response_html = f"""
            <html>
            <head>
                <style>
                    body {{ font-family: monospace; margin: 40px; background-color: #1a1a1a; color: #00ff00; }}
                    .card {{ background: #262626; padding: 20px; border-radius: 8px; border: 1px solid #333; margin-bottom: 20px; }}
                    table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
                    th, td {{ padding: 12px; border: 1px solid #444; text-align: left; }}
                    th {{ background: #333; color: #00adb5; }}
                    .blocked {{ color: #ff414d; font-weight: bold; }}
                </style>
            </head>
            <body>
                <h2>📊 WAF GÜVENLİK TELEMETRİSİ VE ANALİZ RAPORU</h2>
                <div class="card">
                    <h3>📦 Havada Yakalanan Ham HTTP POST Paketi:</h3>
                    <span style="color: #ffb400;">{post_data}</span>
                </div>
                
                <div class="card">
                    <h3>🛡️ Çekirdek Filtre Sonuçları (Politika Seviyesi: {policy_level}):</h3>
                    <table>
                        <tr><th>Saldırı Vektörü</th><th>Gelen Ham Veri</th><th>Kütüphane Güvenlik Çıktısı</th></tr>
                        <tr><td><b>XSS Savunması</b></td><td>{html.escape(xss_input)}</td><td><code>{clean_xss}</code></td></tr>
                        <tr><td><b>SQL Injection</b></td><td>{html.escape(sqli_input)}</td><td><code class="blocked">{clean_sqli}</code></td></tr>
                        <tr><td><b>OS Command Injection</b></td><td>{html.escape(cmd_input)}</td><td><code class="blocked">{clean_cmd}</code></td></tr>
                    </table>
                </div>
                <br>
                <a href="/" style="color: #00adb5; text-decoration: none; font-size: 16px;">[ ⬅️ Yeni Saldırı Simülasyonu Başlat ]</a>
            </body>
            </html>
            """
            self.wfile.write(response_html.encode("utf-8"))

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', 8080), AdvancedWafHandler)
    print("🚀 Kurumsal Seviye WAF Port 8080 üzerinde tetiklendi!")
    server.serve_forever()
