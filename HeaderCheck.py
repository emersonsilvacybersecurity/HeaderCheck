import requests

def analisar_cabecalhos(url):
    # Garante que a URL comece com http ou https
    if not url.startswith('http'):
        url = 'https://' + url

    print(f"\n" + "="*60)
    print(f"🕵️  ANALISANDO CABEÇALHOS DE SEGURANÇA: {url}")
    print("="*60)

    try:
        # Define um User-Agent para simular um navegador comum
        headers_simulados = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Cybersecurity-Student-Scanner'
        }
        
        response = requests.get(url, timeout=10, headers=headers_simulados)
        headers = response.headers

        # Dicionário de cabeçalhos de segurança essenciais
        security_headers = {
            "Strict-Transport-Security": "HSTS: Obriga o uso de HTTPS. Protege contra Downgrade Attacks.",
            "Content-Security-Policy": "CSP: Controla fontes de conteúdo. Defesa principal contra XSS.",
            "X-Frame-Options": "Protege contra Clickjacking (frames maliciosos).",
            "X-Content-Type-Options": "Previne o navegador de interpretar arquivos incorretamente (MIME Sniffing).",
            "X-XSS-Protection": "Filtro básico de segurança contra scripts maliciosos (Cross-Site Scripting)."
        }

        print(f"\n[+] Status da Resposta: {response.status_code}")
        print(f"[+] Servidor detectado: {headers.get('Server', 'Não informado')}\n")

        for header, desc in security_headers.items():
            if header in headers:
                print(f"✅ {header}: ATIVADO")
                print(f"   ↳ {desc}")
            else:
                print(f"❌ {header}: AUSENTE!")
                print(f"   ↳ Risco: Configuração de segurança incompleta.")
            print("-" * 50)

    except requests.exceptions.RequestException as e:
        print(f"[!] ERRO ao conectar: Verifique se a URL está correta.")

if __name__ == "__main__":
    # Aqui é onde o programa pede para você inserir a URL
    print("--- Verificador de Segurança de Cabeçalhos HTTP ---")
    url_usuario = input("Digite a URL do site (ex: google.com): ")
    analisar_cabecalhos(url_usuario)
    
    # Mantém a janela aberta para você ler o resultado
    input("\nPressione Enter para sair...")
    