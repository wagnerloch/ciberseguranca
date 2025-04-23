"""
Script de Demonstração: Ataque de Força Bruta
Autor: Wagner Loch
Data: Abril 2025

AVISO IMPORTANTE: Este script foi criado APENAS para fins educacionais.
Usar este tipo de técnica sem autorização explícita é ilegal e antiético.
Sempre pratique segurança cibernética de forma responsável e ética.
"""

import time
import hashlib
import argparse
from colorama import Fore, Style, init

# Inicializa o colorama para formatação de texto colorido
init()

def banner():
    """Exibe um banner para o script"""
    print(Fore.CYAN + """
    ╔═══════════════════════════════════════════════╗
    ║                                               ║
    ║   DEMONSTRAÇÃO DE ATAQUE DE FORÇA BRUTA       ║
    ║   Apenas para fins educacionais               ║
    ║                                               ║
    ╚═══════════════════════════════════════════════╝
    """ + Style.RESET_ALL)

def simular_verificacao_senha(senha_tentativa, senha_hash, algoritmo='md5'):
    """
    Simula a verificação de uma senha contra um hash armazenado.
    
    Args:
        senha_tentativa: A senha que está sendo testada
        senha_hash: O hash da senha correta
        algoritmo: O algoritmo de hash usado (padrão: md5)
        
    Returns:
        bool: True se a senha estiver correta, False caso contrário
    """
    if algoritmo == 'md5':
        hash_tentativa = hashlib.md5(senha_tentativa.encode()).hexdigest()
    elif algoritmo == 'sha1':
        hash_tentativa = hashlib.sha1(senha_tentativa.encode()).hexdigest()
    elif algoritmo == 'sha256':
        hash_tentativa = hashlib.sha256(senha_tentativa.encode()).hexdigest()
    else:
        raise ValueError(f"Algoritmo de hash não suportado: {algoritmo}")
    
    return hash_tentativa == senha_hash

def ataque_forca_bruta(arquivo_senhas, senha_hash, algoritmo='md5', delay=0.1):
    """
    Realiza um ataque de força bruta usando uma lista de senhas.
    
    Args:
        arquivo_senhas: Caminho para o arquivo contendo a lista de senhas
        senha_hash: O hash da senha que estamos tentando quebrar
        algoritmo: O algoritmo de hash usado (padrão: md5)
        delay: Tempo de espera entre tentativas para visualização (padrão: 0.1s)
        
    Returns:
        tuple: (senha encontrada ou None, número de tentativas, tempo decorrido)
    """
    print(Fore.YELLOW + f"\n[*] Iniciando ataque de força bruta usando arquivo: {arquivo_senhas}" + Style.RESET_ALL)
    print(Fore.YELLOW + f"[*] Hash alvo: {senha_hash}" + Style.RESET_ALL)
    print(Fore.YELLOW + f"[*] Algoritmo: {algoritmo.upper()}" + Style.RESET_ALL)
    
    inicio = time.time()
    tentativas = 0
    
    try:
        with open(arquivo_senhas, 'r', encoding='utf-8', errors='ignore') as f:
            for linha in f:
                senha = linha.strip()
                tentativas += 1
                
                # Exibe a tentativa atual
                print(f"[{tentativas}] Testando: {senha}", end='\r')
                
                # Verifica se a senha está correta
                if simular_verificacao_senha(senha, senha_hash, algoritmo):
                    tempo_decorrido = time.time() - inicio
                    print("\n" + Fore.GREEN + f"[+] SENHA ENCONTRADA: {senha}" + Style.RESET_ALL)
                    return senha, tentativas, tempo_decorrido
                
                # Adiciona um pequeno delay para visualização em sala de aula
                time.sleep(delay)
    
    except FileNotFoundError:
        print(Fore.RED + f"\n[-] ERRO: Arquivo de senhas '{arquivo_senhas}' não encontrado!" + Style.RESET_ALL)
        return None, tentativas, time.time() - inicio
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n[-] Ataque interrompido pelo usuário!" + Style.RESET_ALL)
        return None, tentativas, time.time() - inicio
    
    tempo_decorrido = time.time() - inicio
    print(Fore.RED + "\n[-] Senha não encontrada no arquivo fornecido." + Style.RESET_ALL)
    return None, tentativas, tempo_decorrido

def gerar_hash_senha(senha, algoritmo='md5'):
    """
    Gera o hash de uma senha usando o algoritmo especificado.
    
    Args:
        senha: A senha para gerar o hash
        algoritmo: O algoritmo de hash a ser usado
        
    Returns:
        str: O hash da senha
    """
    if algoritmo == 'md5':
        return hashlib.md5(senha.encode()).hexdigest()
    elif algoritmo == 'sha1':
        return hashlib.sha1(senha.encode()).hexdigest()
    elif algoritmo == 'sha256':
        return hashlib.sha256(senha.encode()).hexdigest()
    else:
        raise ValueError(f"Algoritmo de hash não suportado: {algoritmo}")

def criar_arquivo_senhas_demo(arquivo_saida, senhas_adicionais=None):
    """
    Cria um arquivo de demonstração com senhas comuns para teste.
    
    Args:
        arquivo_saida: Caminho para o arquivo de saída
        senhas_adicionais: Lista opcional de senhas adicionais para incluir
    """
    senhas_comuns = [
        "123456", "password", "12345678", "qwerty", "123456789",
        "12345", "1234", "111111", "1234567", "dragon",
        "123123", "baseball", "abc123", "football", "monkey",
        "letmein", "shadow", "master", "666666", "qwertyuiop",
        "123321", "mustang", "1234567890", "michael", "654321",
        "superman", "1qaz2wsx", "7777777", "121212", "000000",
        "qazwsx", "123qwe", "killer", "trustno1", "jordan",
        "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster",
        "soccer", "harley", "batman", "andrew", "tigger",
        "sunshine", "iloveyou", "2000", "charlie", "robert",
        "thomas", "hockey", "ranger", "daniel", "starwars",
        "klaster", "112233", "george", "computer", "michelle",
        "jessica", "pepper", "1111", "zxcvbn", "555555",
        "11111111", "131313", "freedom", "777777", "pass",
        "maggie", "159753", "aaaaaa", "ginger", "princess",
        "joshua", "cheese", "amanda", "summer", "love",
        "ashley", "nicole", "chelsea", "biteme", "matthew",
        "access", "yankees", "987654321", "dallas", "austin",
        "thunder", "taylor", "matrix", "mobilemail", "mom",
        "monitor", "monitoring", "montana", "moon", "senha123"
    ]
    
    # Adiciona senhas personalizadas se fornecidas
    if senhas_adicionais:
        senhas_comuns.extend(senhas_adicionais)
    
    try:
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            for senha in senhas_comuns:
                f.write(f"{senha}\n")
        print(Fore.GREEN + f"[+] Arquivo de senhas de demonstração criado: {arquivo_saida}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"[-] Erro ao criar arquivo de senhas: {str(e)}" + Style.RESET_ALL)

def main():
    """Função principal do script"""
    parser = argparse.ArgumentParser(description='Demonstração de Ataque de Força Bruta')
    parser.add_argument('-w', '--wordlist', help='Arquivo de lista de senhas')
    parser.add_argument('-p', '--password', help='Senha para gerar hash (para demonstração)')
    parser.add_argument('-a', '--algorithm', choices=['md5', 'sha1', 'sha256'], default='md5',
                        help='Algoritmo de hash a ser usado (padrão: md5)')
    parser.add_argument('-d', '--delay', type=float, default=0.1,
                        help='Atraso entre tentativas em segundos (padrão: 0.1)')
    parser.add_argument('--create-wordlist', help='Criar uma wordlist de demonstração')
    parser.add_argument('--hash', help='Hash da senha a ser quebrada')
    parser.add_argument('--only-hash', action='store_true', help='Apenas gerar o hash da senha e sair')
    
    args = parser.parse_args()
    
    banner()
    
    # Criar wordlist de demonstração se solicitado
    if args.create_wordlist:
        criar_arquivo_senhas_demo(args.create_wordlist)
        return
    
    # Verificar se temos um hash para quebrar ou uma senha para gerar hash
    senha_hash = args.hash
    if not senha_hash and args.password:
        senha_hash = gerar_hash_senha(args.password, args.algorithm)
        print(Fore.BLUE + f"[i] Hash gerado para '{args.password}': {senha_hash}" + Style.RESET_ALL)
        
        # Se o usuário só quer gerar o hash, encerrar aqui
        if args.only_hash:
            return
    
    if not senha_hash:
        print(Fore.RED + "[-] ERRO: Você deve fornecer um hash (--hash) ou uma senha (--password) para gerar o hash!" + Style.RESET_ALL)
        return
    
    # Verificar se temos uma wordlist para o ataque de força bruta
    if not args.wordlist:
        print(Fore.RED + "[-] ERRO: Você deve fornecer um arquivo de lista de senhas (--wordlist) para realizar o ataque!" + Style.RESET_ALL)
        print(Fore.YELLOW + "[!] DICA: Se você só quer gerar o hash de uma senha, use a opção --only-hash junto com --password" + Style.RESET_ALL)
        return
    
    # Iniciar o ataque de força bruta
    senha, tentativas, tempo = ataque_forca_bruta(args.wordlist, senha_hash, args.algorithm, args.delay)
    
    # Exibir estatísticas
    print(Fore.BLUE + f"\n[i] Estatísticas do ataque:" + Style.RESET_ALL)
    print(Fore.BLUE + f"[i] Tentativas realizadas: {tentativas}" + Style.RESET_ALL)
    print(Fore.BLUE + f"[i] Tempo decorrido: {tempo:.2f} segundos" + Style.RESET_ALL)
    print(Fore.BLUE + f"[i] Velocidade média: {tentativas/tempo if tempo > 0 else 0:.2f} senhas/segundo" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
