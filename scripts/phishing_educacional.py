"""
Script de Demonstração: Gerador de Phishing Educacional
Autor: Wagner Loch
Data: Abril 2025

AVISO IMPORTANTE: Este script foi criado APENAS para fins educacionais.
Usar este tipo de técnica sem autorização explícita é ilegal e antiético.
Sempre pratique segurança cibernética de forma responsável e ética.
"""

import argparse
import os
import random
import string
import datetime
from colorama import Fore, Style, init

# Inicializa o colorama para formatação de texto colorido
init()

def banner():
    """Exibe um banner para o script"""
    print(Fore.CYAN + """
    ╔═══════════════════════════════════════════════╗
    ║                                               ║
    ║   GERADOR DE PHISHING EDUCACIONAL             ║
    ║   Apenas para fins educacionais               ║
    ║                                               ║
    ╚═══════════════════════════════════════════════╝
    """ + Style.RESET_ALL)

def gerar_id_aleatorio(tamanho=8):
    """
    Gera um ID aleatório para uso em URLs e nomes de arquivos.
    
    Args:
        tamanho: Tamanho do ID a ser gerado
        
    Returns:
        str: ID aleatório
    """
    caracteres = string.ascii_lowercase + string.digits
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def criar_email_phishing(template, empresa, nome_destinatario, email_destinatario, urgencia=False):
    """
    Cria um email de phishing educacional baseado em um template.
    
    Args:
        template: Nome do template a ser usado
        empresa: Nome da empresa a ser impersonada
        nome_destinatario: Nome do destinatário
        email_destinatario: Email do destinatário
        urgencia: Se deve adicionar elementos de urgência
        
    Returns:
        str: Conteúdo do email de phishing
    """
    data_atual = datetime.datetime.now().strftime("%d/%m/%Y")
    id_aleatorio = gerar_id_aleatorio()
    
    templates = {
        "reset_senha": {
            "assunto": f"[{empresa}] Ação necessária: Redefina sua senha imediatamente",
            "corpo": f"""
De: Suporte {empresa} <suporte@{empresa.lower().replace(' ', '')}.com>
Para: {nome_destinatario} <{email_destinatario}>
Assunto: [{empresa}] Ação necessária: Redefina sua senha imediatamente
Data: {data_atual}

Prezado(a) {nome_destinatario},

Detectamos uma atividade incomum em sua conta {empresa}. Por motivos de segurança, 
sua senha foi temporariamente bloqueada.

Para restaurar o acesso à sua conta, clique no link abaixo e siga as instruções:

https://conta-{empresa.lower().replace(' ', '')}.com/reset?id={id_aleatorio}&email={email_destinatario}

{"ATENÇÃO: Se você não redefinir sua senha nas próximas 24 horas, sua conta será suspensa permanentemente." if urgencia else ""}

Atenciosamente,
Equipe de Segurança {empresa}

NOTA: Esta é uma mensagem automática. Por favor, não responda a este email.
"""
        },
        "premio": {
            "assunto": f"Parabéns! Você foi selecionado para um prêmio especial da {empresa}",
            "corpo": f"""
De: Promoções {empresa} <promocoes@{empresa.lower().replace(' ', '')}.com>
Para: {nome_destinatario} <{email_destinatario}>
Assunto: Parabéns! Você foi selecionado para um prêmio especial da {empresa}
Data: {data_atual}

Prezado(a) {nome_destinatario},

Temos o prazer de informar que você foi selecionado para receber um prêmio especial 
da {empresa} no valor de R$ 1.000,00!

Para resgatar seu prêmio, clique no link abaixo e preencha suas informações:

https://promocao-{empresa.lower().replace(' ', '')}.com/premio?id={id_aleatorio}&email={email_destinatario}

{"ATENÇÃO: Esta oferta é válida apenas por 24 horas. Não perca esta oportunidade única!" if urgencia else "Esta oferta é válida por 7 dias."}

Atenciosamente,
Departamento de Marketing {empresa}

NOTA: Esta é uma mensagem automática. Por favor, não responda a este email.
"""
        },
        "fatura": {
            "assunto": f"Sua fatura {empresa} - Pagamento pendente",
            "corpo": f"""
De: Financeiro {empresa} <financeiro@{empresa.lower().replace(' ', '')}.com>
Para: {nome_destinatario} <{email_destinatario}>
Assunto: Sua fatura {empresa} - Pagamento pendente
Data: {data_atual}

Prezado(a) {nome_destinatario},

Informamos que sua fatura {empresa} do mês atual encontra-se pendente de pagamento.

Para visualizar e pagar sua fatura, clique no link abaixo:

https://fatura-{empresa.lower().replace(' ', '')}.com/pagar?id={id_aleatorio}&email={email_destinatario}

{"ATENÇÃO: O não pagamento até amanhã resultará em multa de 10% e suspensão imediata dos serviços." if urgencia else "O vencimento está próximo. Evite juros e multas pagando em dia."}

Atenciosamente,
Departamento Financeiro {empresa}

NOTA: Esta é uma mensagem automática. Por favor, não responda a este email.
"""
        },
        "documento": {
            "assunto": f"Documento importante da {empresa} para sua revisão",
            "corpo": f"""
De: Documentos {empresa} <docs@{empresa.lower().replace(' ', '')}.com>
Para: {nome_destinatario} <{email_destinatario}>
Assunto: Documento importante da {empresa} para sua revisão
Data: {data_atual}

Prezado(a) {nome_destinatario},

Anexamos um documento importante que requer sua revisão e assinatura.

Para acessar o documento, clique no link abaixo e faça login com suas credenciais:

https://docs-{empresa.lower().replace(' ', '')}.com/view?id={id_aleatorio}&email={email_destinatario}

{"ATENÇÃO: Este documento requer sua assinatura URGENTE até o final do dia de hoje." if urgencia else "Por favor, revise e assine este documento assim que possível."}

Atenciosamente,
Departamento Administrativo {empresa}

NOTA: Esta é uma mensagem automática. Por favor, não responda a este email.
"""
        }
    }
    
    if template not in templates:
        print(Fore.RED + f"[-] Erro: Template '{template}' não encontrado." + Style.RESET_ALL)
        return None
    
    return {
        "assunto": templates[template]["assunto"],
        "corpo": templates[template]["corpo"]
    }

def criar_pagina_phishing(template, empresa, logo_url=None):
    """
    Cria uma página HTML de phishing educacional baseada em um template.
    
    Args:
        template: Nome do template a ser usado
        empresa: Nome da empresa a ser impersonada
        logo_url: URL opcional do logotipo da empresa
        
    Returns:
        str: Conteúdo HTML da página de phishing
    """
    logo_html = f'<img src="{logo_url}" alt="{empresa} Logo" class="logo">' if logo_url else ''
    
    templates = {
        "reset_senha": f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Redefinir Senha - {empresa}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }}
        .container {{
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 30px;
            width: 100%;
            max-width: 400px;
            text-align: center;
        }}
        .logo {{
            max-width: 150px;
            margin-bottom: 20px;
        }}
        h1 {{
            color: #333;
            font-size: 24px;
            margin-bottom: 20px;
        }}
        .form-group {{
            margin-bottom: 15px;
            text-align: left;
        }}
        label {{
            display: block;
            margin-bottom: 5px;
            color: #555;
            font-size: 14px;
        }}
        input {{
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 14px;
            box-sizing: border-box;
        }}
        button {{
            background-color: #0066cc;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 12px 20px;
            font-size: 16px;
            cursor: pointer;
            width: 100%;
            margin-top: 10px;
        }}
        button:hover {{
            background-color: #0052a3;
        }}
        .footer {{
            margin-top: 20px;
            font-size: 12px;
            color: #777;
        }}
    </style>
</head>
<body>
    <div class="container">
        {logo_html}
        <h1>Redefinir sua senha {empresa}</h1>
        <p>Por motivos de segurança, precisamos que você redefina sua senha.</p>
        
        <form id="resetForm">
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" placeholder="Seu email" required>
            </div>
            <div class="form-group">
                <label for="password">Senha atual</label>
                <input type="password" id="password" name="password" placeholder="Sua senha atual" required>
            </div>
            <div class="form-group">
                <label for="newPassword">Nova senha</label>
                <input type="password" id="newPassword" name="newPassword" placeholder="Nova senha" required>
            </div>
            <div class="form-group">
                <label for="confirmPassword">Confirmar nova senha</label>
                <input type="password" id="confirmPassword" name="confirmPassword" placeholder="Confirmar nova senha" required>
            </div>
            
            <button type="submit">Redefinir Senha</button>
        </form>
        
        <div class="footer">
            &copy; {datetime.datetime.now().year} {empresa}. Todos os direitos reservados.
        </div>
    </div>
    
    <script>
        // Este script demonstra como os dados poderiam ser capturados
        document.getElementById('resetForm').addEventListener('submit', function(e) {{
            e.preventDefault();
            
            // Em um ataque real, estes dados seriam enviados para o servidor do atacante
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            // Simulação educacional - apenas mostra um alerta
            alert('DEMONSTRAÇÃO EDUCACIONAL DE PHISHING\\n\\nEm um ataque real, suas credenciais teriam sido roubadas:\\n\\nEmail: ' + email + '\\nSenha: ' + password + '\\n\\nNUNCA insira suas credenciais em sites suspeitos!');
            
            // Redireciona para o site real após a demonstração
            window.location.href = 'https://www.google.com/search?q=como+se+proteger+de+phishing';
        }});
    </script>
</body>
</html>""",
        "login": f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - {empresa}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }}
        .container {{
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 30px;
            width: 100%;
            max-width: 350px;
            text-align: center;
        }}
        .logo {{
            max-width: 150px;
            margin-bottom: 20px;
        }}
        h1 {{
            color: #333;
            font-size: 24px;
            margin-bottom: 20px;
        }}
        .form-group {{
            margin-bottom: 15px;
            text-align: left;
        }}
        label {{
            display: block;
            margin-bottom: 5px;
            color: #555;
            font-size: 14px;
        }}
        input {{
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 14px;
            box-sizing: border-box;
        }}
        button {{
            background-color: #0066cc;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 12px 20px;
            font-size: 16px;
            cursor: pointer;
            width: 100%;
            margin-top: 10px;
        }}
        button:hover {{
            background-color: #0052a3;
        }}
        .footer {{
            margin-top: 20px;
            font-size: 12px;
            color: #777;
        }}
        .forgot-password {{
            display: block;
            margin-top: 15px;
            font-size: 13px;
            color: #0066cc;
            text-decoration: none;
        }}
    </style>
</head>
<body>
    <div class="container">
        {logo_html}
        <h1>Login {empresa}</h1>
        
        <form id="loginForm">
            <div class="form-group">
                <label for="email">Email ou nome de usuário</label>
                <input type="text" id="email" name="email" placeholder="Seu email ou usuário" required>
            </div>
            <div class="form-group">
                <label for="password">Senha</label>
                <input type="password" id="password" name="password" placeholder="Sua senha" required>
            </div>
            
            <button type="submit">Entrar</button>
            <a href="#" class="forgot-password">Esqueceu sua senha?</a>
        </form>
        
        <div class="footer">
            &copy; {datetime.datetime.now().year} {empresa}. Todos os direitos reservados.
        </div>
    </div>
    
    <script>
        // Este script demonstra como os dados poderiam ser capturados
        document.getElementById('loginForm').addEventListener('submit', function(e) {{
            e.preventDefault();
            
            // Em um ataque real, estes dados seriam enviados para o servidor do atacante
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            // Simulação educacional - apenas mostra um alerta
            alert('DEMONSTRAÇÃO EDUCACIONAL DE PHISHING\\n\\nEm um ataque real, suas credenciais teriam sido roubadas:\\n\\nEmail/Usuário: ' + email + '\\nSenha: ' + password + '\\n\\nNUNCA insira suas credenciais em sites suspeitos!');
            
            // Redireciona para o site real após a demonstração
            window.location.href = 'https://www.google.com/search?q=como+se+proteger+de+phishing';
        }});
    </script>
</body>
</html>""",
        "pagamento": f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pagamento de Fatura - {empresa}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
            box-sizing: border-box;
        }}
        .container {{
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 30px;
            width: 100%;
            max-width: 500px;
        }}
        .logo {{
            max-width: 150px;
            display: block;
            margin: 0 auto 20px;
        }}
        h1 {{
            color: #333;
            font-size: 24px;
            margin-bottom: 20px;
            text-align: center;
        }}
        .form-group {{
            margin-bottom: 15px;
        }}
        label {{
            display: block;
            margin-bottom: 5px;
            color: #555;
            font-size: 14px;
        }}
        input, select {{
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 14px;
            box-sizing: border-box;
        }}
        .card-details {{
            display: flex;
            gap: 15px;
        }}
        .card-details .form-group {{
            flex: 1;
        }}
        .expiry-cvv {{
            display: flex;
            gap: 15px;
        }}
        .expiry-cvv .form-group {{
            flex: 1;
        }}
        button {{
            background-color: #0066cc;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 12px 20px;
            font-size: 16px;
            cursor: pointer;
            width: 100%;
            margin-top: 10px;
        }}
        button:hover {{
            background-color: #0052a3;
        }}
        .footer {{
            margin-top: 20px;
            font-size: 12px;
            color: #777;
            text-align: center;
        }}
        .invoice-details {{
            background-color: #f9f9f9;
            border-radius: 4px;
            padding: 15px;
            margin-bottom: 20px;
        }}
        .invoice-details p {{
            margin: 5px 0;
            font-size: 14px;
        }}
        .invoice-details .amount {{
            font-size: 18px;
            font-weight: bold;
            color: #d9534f;
        }}
    </style>
</head>
<body>
    <div class="container">
        {logo_html}
        <h1>Pagamento de Fatura</h1>
        
        <div class="invoice-details">
            <p><strong>Cliente:</strong> <span id="clientName">Nome do Cliente</span></p>
            <p><strong>Fatura:</strong> #INV-{random.randint(10000, 99999)}</p>
            <p><strong>Data de vencimento:</strong> {(datetime.datetime.now() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')}</p>
            <p class="amount"><strong>Valor:</strong> R$ {random.randint(50, 500)},{random.randint(0, 99):02d}</p>
        </div>
        
        <form id="paymentForm">
            <div class="form-group">
                <label for="cardName">Nome no cartão</label>
                <input type="text" id="cardName" name="cardName" placeholder="Nome como aparece no cartão" required>
            </div>
            
            <div class="form-group">
                <label for="cardNumber">Número do cartão</label>
                <input type="text" id="cardNumber" name="cardNumber" placeholder="0000 0000 0000 0000" required>
            </div>
            
            <div class="expiry-cvv">
                <div class="form-group">
                    <label for="expiryDate">Data de validade</label>
                    <input type="text" id="expiryDate" name="expiryDate" placeholder="MM/AA" required>
                </div>
                <div class="form-group">
                    <label for="cvv">CVV</label>
                    <input type="text" id="cvv" name="cvv" placeholder="123" required>
                </div>
            </div>
            
            <div class="form-group">
                <label for="cpf">CPF do titular</label>
                <input type="text" id="cpf" name="cpf" placeholder="000.000.000-00" required>
            </div>
            
            <button type="submit">Pagar agora</button>
        </form>
        
        <div class="footer">
            &copy; {datetime.datetime.now().year} {empresa}. Todos os direitos reservados.<br>
            Pagamento processado com segurança.
        </div>
    </div>
    
    <script>
        // Este script demonstra como os dados poderiam ser capturados
        document.getElementById('paymentForm').addEventListener('submit', function(e) {{
            e.preventDefault();
            
            // Em um ataque real, estes dados seriam enviados para o servidor do atacante
            const cardName = document.getElementById('cardName').value;
            const cardNumber = document.getElementById('cardNumber').value;
            const expiryDate = document.getElementById('expiryDate').value;
            const cvv = document.getElementById('cvv').value;
            const cpf = document.getElementById('cpf').value;
            
            // Simulação educacional - apenas mostra um alerta
            alert('DEMONSTRAÇÃO EDUCACIONAL DE PHISHING\\n\\nEm um ataque real, seus dados de pagamento teriam sido roubados:\\n\\nNome: ' + cardName + '\\nNúmero do cartão: ' + cardNumber + '\\nValidade: ' + expiryDate + '\\nCVV: ' + cvv + '\\nCPF: ' + cpf + '\\n\\nNUNCA insira dados de pagamento em sites suspeitos!');
            
            // Redireciona para o site real após a demonstração
            window.location.href = 'https://www.google.com/search?q=como+se+proteger+de+phishing';
        }});
        
        // Preenche um nome aleatório para o cliente
        const nomes = ['Maria Silva', 'João Santos', 'Ana Oliveira', 'Carlos Souza', 'Juliana Lima'];
        document.getElementById('clientName').textContent = nomes[Math.floor(Math.random() * nomes.length)];
    </script>
</body>
</html>"""
    }
    
    if template not in templates:
        print(Fore.RED + f"[-] Erro: Template '{template}' não encontrado." + Style.RESET_ALL)
        return None
    
    return templates[template]

def salvar_arquivo(conteudo, nome_arquivo, diretorio):
    """
    Salva o conteúdo em um arquivo.
    
    Args:
        conteudo: Conteúdo a ser salvo
        nome_arquivo: Nome do arquivo
        diretorio: Diretório onde o arquivo será salvo
        
    Returns:
        str: Caminho completo do arquivo salvo
    """
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    
    caminho_completo = os.path.join(diretorio, nome_arquivo)
    
    try:
        with open(caminho_completo, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        return caminho_completo
    except Exception as e:
        print(Fore.RED + f"[-] Erro ao salvar arquivo: {str(e)}" + Style.RESET_ALL)
        return None

def gerar_qrcode_phishing(url, nome_arquivo, diretorio):
    """
    Gera um QR code para a URL de phishing.
    
    Args:
        url: URL para o QR code
        nome_arquivo: Nome do arquivo
        diretorio: Diretório onde o arquivo será salvo
        
    Returns:
        str: Caminho completo do arquivo salvo
    """
    try:
        import qrcode
        
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
        
        caminho_completo = os.path.join(diretorio, nome_arquivo)
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(caminho_completo)
        
        return caminho_completo
    except ImportError:
        print(Fore.YELLOW + "[!] Módulo 'qrcode' não encontrado. Instale-o com 'pip install qrcode[pil]'." + Style.RESET_ALL)
        return None
    except Exception as e:
        print(Fore.RED + f"[-] Erro ao gerar QR code: {str(e)}" + Style.RESET_ALL)
        return None

def main():
    """Função principal do script"""
    parser = argparse.ArgumentParser(description='Gerador de Phishing Educacional')
    parser.add_argument('--email', action='store_true', help='Gerar email de phishing')
    parser.add_argument('--pagina', action='store_true', help='Gerar página de phishing')
    parser.add_argument('--qrcode', action='store_true', help='Gerar QR code para a URL de phishing')
    parser.add_argument('--empresa', default='Empresa', help='Nome da empresa a ser impersonada')
    parser.add_argument('--nome', default='Usuário', help='Nome do destinatário (para emails)')
    parser.add_argument('--email-dest', default='usuario@exemplo.com', help='Email do destinatário (para emails)')
    parser.add_argument('--template-email', choices=['reset_senha', 'premio', 'fatura', 'documento'], 
                        default='reset_senha', help='Template de email a ser usado')
    parser.add_argument('--template-pagina', choices=['reset_senha', 'login', 'pagamento'], 
                        default='login', help='Template de página a ser usado')
    parser.add_argument('--urgencia', action='store_true', help='Adicionar elementos de urgência')
    parser.add_argument('--logo', help='URL do logotipo da empresa (para páginas)')
    parser.add_argument('--output', default='./phishing_demo', help='Diretório de saída')
    
    args = parser.parse_args()
    
    banner()
    
    print(Fore.YELLOW + "\n[*] Iniciando geração de materiais de phishing educacional..." + Style.RESET_ALL)
    print(Fore.YELLOW + f"[*] Empresa alvo (simulada): {args.empresa}" + Style.RESET_ALL)
    
    # Cria o diretório de saída se não existir
    if not os.path.exists(args.output):
        os.makedirs(args.output)
    
    # Gera o email de phishing
    if args.email:
        print(Fore.YELLOW + f"\n[*] Gerando email de phishing com template '{args.template_email}'..." + Style.RESET_ALL)
        email = criar_email_phishing(args.template_email, args.empresa, args.nome, args.email_dest, args.urgencia)
        
        if email:
            arquivo_email = f"email_{args.template_email}_{gerar_id_aleatorio()}.txt"
            caminho_email = salvar_arquivo(email["corpo"], arquivo_email, args.output)
            
            if caminho_email:
                print(Fore.GREEN + f"[+] Email de phishing salvo em: {caminho_email}" + Style.RESET_ALL)
                print(Fore.GREEN + f"[+] Assunto do email: {email['assunto']}" + Style.RESET_ALL)
    
    # Gera a página de phishing
    if args.pagina:
        print(Fore.YELLOW + f"\n[*] Gerando página de phishing com template '{args.template_pagina}'..." + Style.RESET_ALL)
        pagina = criar_pagina_phishing(args.template_pagina, args.empresa, args.logo)
        
        if pagina:
            arquivo_pagina = f"pagina_{args.template_pagina}_{gerar_id_aleatorio()}.html"
            caminho_pagina = salvar_arquivo(pagina, arquivo_pagina, args.output)
            
            if caminho_pagina:
                print(Fore.GREEN + f"[+] Página de phishing salva em: {caminho_pagina}" + Style.RESET_ALL)
                
                # Gera QR code para a página
                if args.qrcode:
                    print(Fore.YELLOW + f"[*] Gerando QR code para a página de phishing..." + Style.RESET_ALL)
                    
                    # URL fictícia para o QR code
                    url_ficticia = f"https://{args.empresa.lower().replace(' ', '')}-secure.com/{args.template_pagina}.php"
                    
                    arquivo_qrcode = f"qrcode_{args.template_pagina}_{gerar_id_aleatorio()}.png"
                    caminho_qrcode = gerar_qrcode_phishing(url_ficticia, arquivo_qrcode, args.output)
                    
                    if caminho_qrcode:
                        print(Fore.GREEN + f"[+] QR code salvo em: {caminho_qrcode}" + Style.RESET_ALL)
                        print(Fore.GREEN + f"[+] URL no QR code: {url_ficticia}" + Style.RESET_ALL)
    
    print(Fore.BLUE + "\n[i] LEMBRETE IMPORTANTE:" + Style.RESET_ALL)
    print(Fore.BLUE + "[i] Este material foi gerado APENAS para fins educacionais." + Style.RESET_ALL)
    print(Fore.BLUE + "[i] O uso destas técnicas sem autorização explícita é ilegal e antiético." + Style.RESET_ALL)
    print(Fore.BLUE + "[i] Sempre pratique segurança cibernética de forma responsável e ética." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
