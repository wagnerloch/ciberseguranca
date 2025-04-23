"""
Script de Demonstração: Análise de Vulnerabilidades Web Básicas
Autor: Wagner Loch
Data: Abril 2025

AVISO IMPORTANTE: Este script foi criado APENAS para fins educacionais.
Usar este tipo de técnica sem autorização explícita é ilegal e antiético.
Sempre pratique segurança cibernética de forma responsável e ética.
"""

import argparse
import requests
import re
import urllib.parse
from bs4 import BeautifulSoup
from colorama import Fore, Style, init

# Inicializa o colorama para formatação de texto colorido
init()

# Desativa avisos de SSL para ambientes de teste
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def banner():
    """Exibe um banner para o script"""
    print(Fore.CYAN + """
    ╔═══════════════════════════════════════════════╗
    ║                                               ║
    ║   ANÁLISE DE VULNERABILIDADES WEB BÁSICAS     ║
    ║   Apenas para fins educacionais               ║
    ║                                               ║
    ╚═══════════════════════════════════════════════╝
    """ + Style.RESET_ALL)

def verificar_cabecalhos_seguranca(url):
    """
    Verifica se os cabeçalhos de segurança estão presentes na resposta HTTP.
    
    Args:
        url: A URL do site a ser verificado
        
    Returns:
        dict: Dicionário com os resultados da verificação
    """
    print(Fore.YELLOW + f"\n[*] Verificando cabeçalhos de segurança em: {url}" + Style.RESET_ALL)
    
    cabecalhos_seguranca = {
        'Strict-Transport-Security': 'Ausente - O site pode ser vulnerável a ataques de downgrade HTTPS',
        'Content-Security-Policy': 'Ausente - O site pode ser vulnerável a ataques XSS',
        'X-Content-Type-Options': 'Ausente - O site pode ser vulnerável a ataques de MIME sniffing',
        'X-Frame-Options': 'Ausente - O site pode ser vulnerável a ataques de clickjacking',
        'X-XSS-Protection': 'Ausente - O site pode ser vulnerável a ataques XSS em navegadores antigos',
        'Referrer-Policy': 'Ausente - O site pode vazar informações de referência',
        'Feature-Policy': 'Ausente - O site não restringe recursos do navegador',
        'Permissions-Policy': 'Ausente - O site não restringe permissões do navegador'
    }
    
    try:
        response = requests.get(url, verify=False, timeout=10)
        headers = response.headers
        
        resultados = {}
        
        for cabecalho, mensagem in cabecalhos_seguranca.items():
            if cabecalho in headers:
                resultados[cabecalho] = f"Presente: {headers[cabecalho]}"
            else:
                resultados[cabecalho] = mensagem
        
        return resultados
    
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[-] Erro ao acessar a URL: {str(e)}" + Style.RESET_ALL)
        return {}

def verificar_formularios(url):
    """
    Verifica formulários no site para possíveis vulnerabilidades.
    
    Args:
        url: A URL do site a ser verificado
        
    Returns:
        list: Lista de formulários encontrados com informações sobre possíveis vulnerabilidades
    """
    print(Fore.YELLOW + f"\n[*] Verificando formulários em: {url}" + Style.RESET_ALL)
    
    formularios = []
    
    try:
        response = requests.get(url, verify=False, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for form in soup.find_all('form'):
            form_info = {
                'action': form.get('action', ''),
                'method': form.get('method', 'get').upper(),
                'inputs': [],
                'vulnerabilidades': []
            }
            
            # Verifica se o formulário usa HTTPS
            if form_info['action'] and form_info['action'].startswith('http:'):
                form_info['vulnerabilidades'].append('Formulário submete dados via HTTP não criptografado')
            
            # Verifica se o método é POST para formulários de login/senha
            tem_senha = False
            for input_field in form.find_all('input'):
                input_type = input_field.get('type', '')
                input_name = input_field.get('name', '')
                
                form_info['inputs'].append({
                    'type': input_type,
                    'name': input_name
                })
                
                if input_type == 'password':
                    tem_senha = True
            
            if tem_senha and form_info['method'] != 'POST':
                form_info['vulnerabilidades'].append('Formulário com campo de senha usa método GET')
            
            # Verifica se há proteção CSRF
            tem_csrf = False
            for input_field in form.find_all('input'):
                input_name = input_field.get('name', '').lower()
                if 'csrf' in input_name or 'token' in input_name:
                    tem_csrf = True
                    break
            
            if not tem_csrf and form_info['method'] == 'POST':
                form_info['vulnerabilidades'].append('Formulário POST sem proteção CSRF aparente')
            
            formularios.append(form_info)
        
        return formularios
    
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[-] Erro ao acessar a URL: {str(e)}" + Style.RESET_ALL)
        return []
    except Exception as e:
        print(Fore.RED + f"[-] Erro ao analisar a página: {str(e)}" + Style.RESET_ALL)
        return []

def verificar_cookies(url):
    """
    Verifica cookies do site para possíveis vulnerabilidades.
    
    Args:
        url: A URL do site a ser verificado
        
    Returns:
        list: Lista de cookies encontrados com informações sobre possíveis vulnerabilidades
    """
    print(Fore.YELLOW + f"\n[*] Verificando cookies em: {url}" + Style.RESET_ALL)
    
    cookies_info = []
    
    try:
        response = requests.get(url, verify=False, timeout=10)
        
        for cookie in response.cookies:
            cookie_info = {
                'nome': cookie.name,
                'valor': cookie.value[:10] + '...' if len(cookie.value) > 10 else cookie.value,
                'secure': cookie.secure,
                'httponly': cookie.has_nonstandard_attr('HttpOnly'),
                'samesite': cookie.get_nonstandard_attr('SameSite'),
                'vulnerabilidades': []
            }
            
            # Verifica flags de segurança
            if not cookie.secure:
                cookie_info['vulnerabilidades'].append('Cookie sem flag Secure')
            
            if not cookie.has_nonstandard_attr('HttpOnly'):
                cookie_info['vulnerabilidades'].append('Cookie sem flag HttpOnly')
            
            if not cookie.get_nonstandard_attr('SameSite'):
                cookie_info['vulnerabilidades'].append('Cookie sem atributo SameSite')
            
            cookies_info.append(cookie_info)
        
        return cookies_info
    
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[-] Erro ao acessar a URL: {str(e)}" + Style.RESET_ALL)
        return []

def verificar_injecao_sql_simples(url):
    """
    Verifica possíveis pontos de injeção SQL simples.
    
    Args:
        url: A URL base do site a ser verificado
        
    Returns:
        list: Lista de URLs potencialmente vulneráveis
    """
    print(Fore.YELLOW + f"\n[*] Verificando possíveis pontos de injeção SQL em: {url}" + Style.RESET_ALL)
    print(Fore.YELLOW + f"[*] NOTA: Esta é uma verificação muito básica e pode gerar falsos positivos" + Style.RESET_ALL)
    
    payloads_teste = ["'", "\"", "1=1", "1=1--", "' OR '1'='1", "\" OR \"1\"=\"1"]
    urls_vulneraveis = []
    
    try:
        # Obtém a página inicial para extrair links
        response = requests.get(url, verify=False, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Coleta links com parâmetros
        links = []
        for a in soup.find_all('a', href=True):
            href = a['href']
            if '?' in href and '=' in href:
                if href.startswith('http'):
                    links.append(href)
                elif href.startswith('/'):
                    links.append(urllib.parse.urljoin(url, href))
        
        # Testa cada link com parâmetros
        for link in links:
            print(f"Testando link: {link}", end='\r')
            
            # Separa a URL base dos parâmetros
            base_url, params = link.split('?', 1)
            param_pairs = params.split('&')
            
            for i, param_pair in enumerate(param_pairs):
                if '=' in param_pair:
                    param_name, param_value = param_pair.split('=', 1)
                    
                    for payload in payloads_teste:
                        # Cria uma nova lista de parâmetros com o payload
                        new_params = param_pairs.copy()
                        new_params[i] = f"{param_name}={param_value}{payload}"
                        
                        # Constrói a URL de teste
                        test_url = f"{base_url}?{'&'.join(new_params)}"
                        
                        try:
                            test_response = requests.get(test_url, verify=False, timeout=5)
                            
                            # Verifica por erros SQL comuns na resposta
                            error_patterns = [
                                "SQL syntax", "mysql_fetch", "ORA-", "Oracle error",
                                "Microsoft SQL Server", "PostgreSQL", "SQLite", "syntax error"
                            ]
                            
                            for pattern in error_patterns:
                                if pattern.lower() in test_response.text.lower():
                                    urls_vulneraveis.append({
                                        'url': test_url,
                                        'payload': payload,
                                        'erro': pattern
                                    })
                                    break
                        
                        except requests.exceptions.RequestException:
                            # Ignora erros de timeout ou conexão
                            pass
        
        return urls_vulneraveis
    
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[-] Erro ao acessar a URL: {str(e)}" + Style.RESET_ALL)
        return []
    except Exception as e:
        print(Fore.RED + f"[-] Erro ao analisar a página: {str(e)}" + Style.RESET_ALL)
        return []

def exibir_resultados(url, cabecalhos, formularios, cookies, urls_sql):
    """
    Exibe os resultados da análise de vulnerabilidades.
    
    Args:
        url: A URL analisada
        cabecalhos: Resultados da análise de cabeçalhos
        formularios: Resultados da análise de formulários
        cookies: Resultados da análise de cookies
        urls_sql: Resultados da análise de injeção SQL
    """
    print(Fore.BLUE + f"\n\n[i] RESULTADOS DA ANÁLISE PARA: {url}" + Style.RESET_ALL)
    print(Fore.BLUE + "=" * 70 + Style.RESET_ALL)
    
    # Exibe resultados dos cabeçalhos
    print(Fore.BLUE + "\n[i] CABEÇALHOS DE SEGURANÇA:" + Style.RESET_ALL)
    if cabecalhos:
        for cabecalho, status in cabecalhos.items():
            if "Ausente" in status:
                print(Fore.RED + f"[-] {cabecalho}: {status}" + Style.RESET_ALL)
            else:
                print(Fore.GREEN + f"[+] {cabecalho}: {status}" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "[!] Não foi possível analisar os cabeçalhos." + Style.RESET_ALL)
    
    # Exibe resultados dos formulários
    print(Fore.BLUE + "\n[i] FORMULÁRIOS:" + Style.RESET_ALL)
    if formularios:
        for i, form in enumerate(formularios, 1):
            print(Fore.BLUE + f"\n[i] Formulário #{i}:" + Style.RESET_ALL)
            print(f"    Action: {form['action']}")
            print(f"    Method: {form['method']}")
            print(f"    Campos: {len(form['inputs'])}")
            
            if form['vulnerabilidades']:
                print(Fore.RED + f"    Vulnerabilidades encontradas:" + Style.RESET_ALL)
                for vuln in form['vulnerabilidades']:
                    print(Fore.RED + f"    - {vuln}" + Style.RESET_ALL)
            else:
                print(Fore.GREEN + f"    Nenhuma vulnerabilidade óbvia encontrada" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "[!] Nenhum formulário encontrado ou não foi possível analisar." + Style.RESET_ALL)
    
    # Exibe resultados dos cookies
    print(Fore.BLUE + "\n[i] COOKIES:" + Style.RESET_ALL)
    if cookies:
        for i, cookie in enumerate(cookies, 1):
            print(Fore.BLUE + f"\n[i] Cookie #{i}: {cookie['nome']}" + Style.RESET_ALL)
            print(f"    Valor: {cookie['valor']}")
            print(f"    Secure: {'Sim' if cookie['secure'] else 'Não'}")
            print(f"    HttpOnly: {'Sim' if cookie['httponly'] else 'Não'}")
            print(f"    SameSite: {cookie['samesite'] if cookie['samesite'] else 'Não definido'}")
            
            if cookie['vulnerabilidades']:
                print(Fore.RED + f"    Vulnerabilidades encontradas:" + Style.RESET_ALL)
                for vuln in cookie['vulnerabilidades']:
                    print(Fore.RED + f"    - {vuln}" + Style.RESET_ALL)
            else:
                print(Fore.GREEN + f"    Nenhuma vulnerabilidade óbvia encontrada" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "[!] Nenhum cookie encontrado ou não foi possível analisar." + Style.RESET_ALL)
    
    # Exibe resultados da injeção SQL
    print(Fore.BLUE + "\n[i] POSSÍVEIS PONTOS DE INJEÇÃO SQL:" + Style.RESET_ALL)
    if urls_sql:
        for i, vuln in enumerate(urls_sql, 1):
            print(Fore.RED + f"\n[-] Ponto potencial #{i}:" + Style.RESET_ALL)
            print(Fore.RED + f"    URL: {vuln['url']}" + Style.RESET_ALL)
            print(Fore.RED + f"    Payload: {vuln['payload']}" + Style.RESET_ALL)
            print(Fore.RED + f"    Erro detectado: {vuln['erro']}" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "[+] Nenhum ponto óbvio de injeção SQL encontrado nos links testados." + Style.RESET_ALL)
    
    print(Fore.BLUE + "\n" + "=" * 70 + Style.RESET_ALL)
    print(Fore.YELLOW + "\n[!] LEMBRETE: Esta é uma análise básica para fins educacionais." + Style.RESET_ALL)
    print(Fore.YELLOW + "[!] Falsos positivos e falsos negativos são possíveis." + Style.RESET_ALL)
    print(Fore.YELLOW + "[!] Para uma análise completa, utilize ferramentas profissionais e metodologias adequadas." + Style.RESET_ALL)

def main():
    """Função principal do script"""
    parser = argparse.ArgumentParser(description='Demonstração de Análise de Vulnerabilidades Web Básicas')
    parser.add_argument('-u', '--url', required=True, help='URL do site a ser analisado')
    parser.add_argument('--no-sql', action='store_true', help='Desativa a verificação de injeção SQL')
    
    args = parser.parse_args()
    
    banner()
    
    # Verifica se a URL começa com http:// ou https://
    url = args.url
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
        print(Fore.YELLOW + f"[!] URL ajustada para: {url}" + Style.RESET_ALL)
    
    # Realiza as verificações
    cabecalhos = verificar_cabecalhos_seguranca(url)
    formularios = verificar_formularios(url)
    cookies = verificar_cookies(url)
    
    urls_sql = []
    if not args.no_sql:
        urls_sql = verificar_injecao_sql_simples(url)
    
    # Exibe os resultados
    exibir_resultados(url, cabecalhos, formularios, cookies, urls_sql)

if __name__ == "__main__":
    main()
