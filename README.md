# 🕵️ Python HTTP Security Header Analyzer

Ferramenta de análise de segurança que verifica a presença de cabeçalhos HTTP essenciais para proteção de aplicações web.

---

## 🎯 Objetivo

Identificar falhas de configuração em cabeçalhos de segurança HTTP, auxiliando na detecção de vulnerabilidades comuns em aplicações web, como XSS, Clickjacking e ataques Man-in-the-Middle.

---

## ⚙️ Funcionalidades

- 🔎 Verificação automática de headers de segurança.
- 🌐 Suporte a qualquer domínio (com ou sem HTTPS).
- 🧠 Análise de cabeçalhos críticos como CSP, HSTS e X-Frame-Options.
- ⚠️ Identificação de configurações inseguras ou ausentes.
- 📊 Exibição clara de status (ATIVADO / AUSENTE).
- 🛡️ Apoio a atividades de Pentest, AppSec e Bug Bounty.

---

## 🧰 Tecnologias Utilizadas

- Python 3.x
- requests

---

## 🚀 Como executar

Siga os passos abaixo para rodar o projeto localmente:

### 📥 1. Clonar o repositório
```bash
git clone https://github.com/emersonsilvacybersecurity/HeaderCheck.git
```

### 📂 2. Acessar a pasta do projeto
```bash
cd HeaderCheck
```

### ▶️ 3. Executar o script

#### 💻 Windows
```bash
python headercheck.py
```

#### 🐧 Linux
```bash
python3 headercheck.py
```

---

## 🛡️ Headers analisados

- 🔐 **Strict-Transport-Security (HSTS)** → Força uso de HTTPS  
- 🧱 **Content-Security-Policy (CSP)** → Proteção contra XSS  
- 🪟 **X-Frame-Options** → Defesa contra Clickjacking  
- 📦 **X-Content-Type-Options** → Previne MIME Sniffing  
- ⚠️ **X-XSS-Protection** → Filtro básico contra XSS  

---

## ⚠️ Análise de segurança (Aviso Legal)

Este projeto foi desenvolvido exclusivamente para fins educacionais e auditorias de segurança autorizadas.

- ⚖️ Ética: O uso desta ferramenta contra alvos sem permissão prévia é ilegal.
- 🚫 Responsabilidade: O autor não se responsabiliza por qualquer uso indevido ou danos causados a terceiros.

---

