"""
Script de Demonstração: Scanner de Portas
Autor: Wagner Loch
Data: Abril 2025

AVISO IMPORTANTE: Este script foi criado APENAS para fins educacionais.
Usar este tipo de técnica sem autorização explícita é ilegal e antiético.
Sempre pratique segurança cibernética de forma responsável e ética.
"""

import socket
import argparse
import threading
import time
import subprocess
import re
import ipaddress
from queue import Queue
from colorama import Fore, Style, init

# Inicializa o colorama para formatação de texto colorido
init()

# Variáveis globais
portas_abertas = {}
lock = threading.Lock()

def banner():
    """Exibe um banner para o script"""
    print(Fore.CYAN + """
    ╔═══════════════════════════════════════════════╗
    ║                                               ║
    ║   DEMONSTRAÇÃO DE SCANNER DE PORTAS           ║
    ║   Apenas para fins educacionais               ║
    ║                                               ║
    ╚═══════════════════════════════════════════════╝
    """ + Style.RESET_ALL)

def verificar_porta(ip, porta, timeout=1):
    """
    Verifica se uma porta específica está aberta em um determinado IP.
    
    Args:
        ip: O endereço IP alvo
        porta: A porta a ser verificada
        timeout: Tempo limite para a conexão em segundos
        
    Returns:
        bool: True se a porta estiver aberta, False caso contrário
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    
    try:
        resultado = sock.connect_ex((ip, porta))
        if resultado == 0:
            try:
                # Tenta identificar o serviço
                servico = socket.getservbyport(porta)
            except:
                servico = "desconhecido"
            
            with lock:
                if ip not in portas_abertas:
                    portas_abertas[ip] = []
                portas_abertas[ip].append((porta, servico))
            return True
    except socket.error:
        pass
    finally:
        sock.close()
    
    return False

def worker(ip, fila_portas, timeout):
    """
    Função worker para processamento de portas em threads.
    
    Args:
        ip: O endereço IP alvo
        fila_portas: Fila contendo as portas a serem verificadas
        timeout: Tempo limite para a conexão em segundos
    """
    while not fila_portas.empty():
        porta = fila_portas.get()
        
        # Exibe a porta sendo verificada
        print(f"Verificando {ip}:{porta}...", end='\r')
        
        if verificar_porta(ip, porta, timeout):
            with lock:
                print(Fore.GREEN + f"[+] {ip}: Porta {porta} aberta ({portas_abertas[ip][-1][1]})" + Style.RESET_ALL + " "*20)
        
        fila_portas.task_done()

def verificar_host_ativo(ip, timeout=1):
    """
    Verifica se um host está ativo usando uma conexão na porta 80.
    
    Args:
        ip: O endereço IP a ser verificado
        timeout: Tempo limite para a conexão em segundos
        
    Returns:
        bool: True se o host estiver ativo, False caso contrário
    """
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 80))
        s.close()
        return True
    except:
        try:
            # Tenta ping usando socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, 443))
            s.close()
            return True
        except:
            try:
                # Tenta ICMP ping
                if subprocess.call(['ping', '-c', '1', '-W', '1', ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
                    return True
                return False
            except:
                return False

def obter_dispositivos_rede():
    """
    Obtém os dispositivos na rede local usando o comando arp -a.
    
    Returns:
        list: Lista de endereços IP dos dispositivos encontrados
    """
    dispositivos = []
    
    try:
        # Executa o comando arp -a
        resultado = subprocess.check_output(['arp', '-a'], universal_newlines=True)
        
        # Extrai os endereços IP usando expressão regular
        padrao = r'\((\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\)'
        ips = re.findall(padrao, resultado)
        
        # Filtra IPs válidos
        for ip in ips:
            if ip not in dispositivos and ip != '0.0.0.0' and not ip.startswith('127.'):
                dispositivos.append(ip)
        
        return dispositivos
    
    except Exception as e:
        print(Fore.RED + f"[-] Erro ao obter dispositivos da rede: {str(e)}" + Style.RESET_ALL)
        return []

def obter_rede_local():
    """
    Obtém informações sobre a rede local.
    
    Returns:
        tuple: (IP local, máscara de rede)
    """
    try:
        # Obtém o IP local
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_local = s.getsockname()[0]
        s.close()
        
        # Obtém a máscara de rede
        resultado = subprocess.check_output(['ip', 'addr', 'show'], universal_newlines=True)
        padrao = rf'{ip_local}/(\d+)'
        match = re.search(padrao, resultado)
        
        if match:
            mascara = int(match.group(1))
            return ip_local, mascara
        
        # Fallback para máscara padrão
        return ip_local, 24
    
    except Exception as e:
        print(Fore.RED + f"[-] Erro ao obter informações da rede local: {str(e)}" + Style.RESET_ALL)
        return None, None

def gerar_ips_rede(ip_base, mascara):
    """
    Gera todos os IPs possíveis em uma rede.
    
    Args:
        ip_base: IP base da rede
        mascara: Máscara de rede em formato CIDR
        
    Returns:
        list: Lista de todos os IPs possíveis na rede
    """
    try:
        rede = ipaddress.IPv4Network(f'{ip_base}/{mascara}', strict=False)
        return [str(ip) for ip in rede.hosts()]
    except Exception as e:
        print(Fore.RED + f"[-] Erro ao gerar IPs da rede: {str(e)}" + Style.RESET_ALL)
        return []

def scanner_portas(ip, porta_inicial=1, porta_final=1024, threads=50, timeout=1):
    """
    Realiza o escaneamento de portas em um intervalo especificado.
    
    Args:
        ip: O endereço IP alvo
        porta_inicial: A porta inicial do intervalo
        porta_final: A porta final do intervalo
        threads: Número de threads a serem usadas
        timeout: Tempo limite para a conexão em segundos
        
    Returns:
        bool: True se o escaneamento foi concluído, False caso contrário
    """
    print(Fore.YELLOW + f"\n[*] Iniciando escaneamento de portas em: {ip}" + Style.RESET_ALL)
    print(Fore.YELLOW + f"[*] Intervalo de portas: {porta_inicial}-{porta_final}" + Style.RESET_ALL)
    
    # Verifica se o host está ativo
    print(Fore.YELLOW + f"[*] Verificando se o host está ativo..." + Style.RESET_ALL)
    if not verificar_host_ativo(ip, timeout):
        print(Fore.RED + f"[-] O host {ip} parece estar inativo ou inacessível." + Style.RESET_ALL)
        return False
    else:
        print(Fore.GREEN + f"[+] Host {ip} está ativo!" + Style.RESET_ALL)
    
    # Inicializa a fila de portas
    fila_portas = Queue()
    for porta in range(porta_inicial, porta_final + 1):
        fila_portas.put(porta)
    
    print(Fore.YELLOW + f"[*] Escaneando {fila_portas.qsize()} portas com {threads} threads..." + Style.RESET_ALL)
    
    inicio = time.time()
    
    # Cria e inicia as threads
    thread_list = []
    for _ in range(min(threads, fila_portas.qsize())):
        t = threading.Thread(target=worker, args=(ip, fila_portas, timeout))
        t.daemon = True
        t.start()
        thread_list.append(t)
    
    # Aguarda a conclusão de todas as threads
    for t in thread_list:
        t.join(timeout=None)
    
    # Aguarda a conclusão de todas as tarefas na fila
    fila_portas.join()
    
    tempo_decorrido = time.time() - inicio
    
    # Exibe os resultados
    print(Fore.BLUE + f"\n[i] Escaneamento de {ip} concluído em {tempo_decorrido:.2f} segundos" + Style.RESET_ALL)
    print(Fore.BLUE + f"[i] Total de portas verificadas: {porta_final - porta_inicial + 1}" + Style.RESET_ALL)
    print(Fore.BLUE + f"[i] Velocidade média: {(porta_final - porta_inicial + 1) / tempo_decorrido:.2f} portas/segundo" + Style.RESET_ALL)
    
    if ip in portas_abertas and portas_abertas[ip]:
        print(Fore.GREEN + f"\n[+] Portas abertas encontradas em {ip}: {len(portas_abertas[ip])}" + Style.RESET_ALL)
        print(Fore.GREEN + "=" * 50 + Style.RESET_ALL)
        print(Fore.GREEN + "    PORTA    |    SERVIÇO" + Style.RESET_ALL)
        print(Fore.GREEN + "=" * 50 + Style.RESET_ALL)
        
        for porta, servico in sorted(portas_abertas[ip]):
            print(Fore.GREEN + f"    {porta:<9}|    {servico}" + Style.RESET_ALL)
        
        print(Fore.GREEN + "=" * 50 + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + f"\n[!] Nenhuma porta aberta encontrada em {ip} no intervalo especificado." + Style.RESET_ALL)
    
    return True

def scanner_rede(porta_inicial=1, porta_final=1024, threads=50, timeout=1, max_hosts=None):
    """
    Realiza o escaneamento de portas em todos os dispositivos da rede local.
    
    Args:
        porta_inicial: A porta inicial do intervalo
        porta_final: A porta final do intervalo
        threads: Número de threads a serem usadas
        timeout: Tempo limite para a conexão em segundos
        max_hosts: Número máximo de hosts a serem escaneados (None = todos)
    """
    print(Fore.YELLOW + "\n[*] Obtendo dispositivos na rede local..." + Style.RESET_ALL)
    
    # Método 1: Usar arp -a
    dispositivos = obter_dispositivos_rede()
    
    # Método 2: Gerar IPs da rede local
    if not dispositivos:
        print(Fore.YELLOW + "[*] Tentando método alternativo para descobrir dispositivos..." + Style.RESET_ALL)
        ip_local, mascara = obter_rede_local()
        if ip_local:
            dispositivos = gerar_ips_rede(ip_local, mascara)
    
    if not dispositivos:
        print(Fore.RED + "[-] Não foi possível encontrar dispositivos na rede local." + Style.RESET_ALL)
        return
    
    # Limita o número de hosts se necessário
    if max_hosts and len(dispositivos) > max_hosts:
        print(Fore.YELLOW + f"[*] Limitando escaneamento aos primeiros {max_hosts} dispositivos de {len(dispositivos)} encontrados." + Style.RESET_ALL)
        dispositivos = dispositivos[:max_hosts]
    
    print(Fore.GREEN + f"[+] Encontrados {len(dispositivos)} dispositivos na rede local." + Style.RESET_ALL)
    
    # Escaneia cada dispositivo
    dispositivos_ativos = 0
    for i, ip in enumerate(dispositivos, 1):
        print(Fore.YELLOW + f"\n[*] Escaneando dispositivo {i}/{len(dispositivos)}: {ip}" + Style.RESET_ALL)
        if scanner_portas(ip, porta_inicial, porta_final, threads, timeout):
            dispositivos_ativos += 1
    
    # Exibe resumo final
    print(Fore.BLUE + "\n" + "=" * 70 + Style.RESET_ALL)
    print(Fore.BLUE + f"[i] RESUMO DO ESCANEAMENTO DE REDE" + Style.RESET_ALL)
    print(Fore.BLUE + "=" * 70 + Style.RESET_ALL)
    print(Fore.BLUE + f"[i] Total de dispositivos encontrados: {len(dispositivos)}" + Style.RESET_ALL)
    print(Fore.BLUE + f"[i] Dispositivos ativos: {dispositivos_ativos}" + Style.RESET_ALL)
    print(Fore.BLUE + f"[i] Dispositivos com portas abertas: {len(portas_abertas)}" + Style.RESET_ALL)
    
    # Exibe relatório detalhado
    if portas_abertas:
        print(Fore.GREEN + "\n[+] RELATÓRIO DETALHADO:" + Style.RESET_ALL)
        
        for ip, portas in portas_abertas.items():
            print(Fore.GREEN + f"\n[+] Dispositivo: {ip}" + Style.RESET_ALL)
            print(Fore.GREEN + f"[+] Portas abertas: {len(portas)}" + Style.RESET_ALL)
            print(Fore.GREEN + "    " + "-" * 40 + Style.RESET_ALL)
            print(Fore.GREEN + "    PORTA    |    SERVIÇO" + Style.RESET_ALL)
            print(Fore.GREEN + "    " + "-" * 40 + Style.RESET_ALL)
            
            for porta, servico in sorted(portas):
                print(Fore.GREEN + f"    {porta:<9}|    {servico}" + Style.RESET_ALL)
    
    print(Fore.BLUE + "\n" + "=" * 70 + Style.RESET_ALL)

def salvar_relatorio(arquivo_saida):
    """
    Salva o relatório de escaneamento em um arquivo.
    
    Args:
        arquivo_saida: Caminho para o arquivo de saída
    """
    try:
        with open(arquivo_saida, 'w') as f:
            f.write("RELATÓRIO DE ESCANEAMENTO DE PORTAS\n")
            f.write("==================================\n\n")
            
            if not portas_abertas:
                f.write("Nenhuma porta aberta encontrada.\n")
                return
            
            for ip, portas in portas_abertas.items():
                f.write(f"Dispositivo: {ip}\n")
                f.write(f"Portas abertas: {len(portas)}\n")
                f.write("-" * 40 + "\n")
                f.write("PORTA    |    SERVIÇO\n")
                f.write("-" * 40 + "\n")
                
                for porta, servico in sorted(portas):
                    f.write(f"{porta:<9}|    {servico}\n")
                
                f.write("\n")
            
        print(Fore.GREEN + f"[+] Relatório salvo em: {arquivo_saida}" + Style.RESET_ALL)
    
    except Exception as e:
        print(Fore.RED + f"[-] Erro ao salvar relatório: {str(e)}" + Style.RESET_ALL)

def main():
    """Função principal do script"""
    parser = argparse.ArgumentParser(description='Demonstração de Scanner de Portas')
    parser.add_argument('-t', '--target', help='Endereço IP ou hostname alvo (omita para escanear toda a rede)')
    parser.add_argument('-p', '--port-range', default='1-1024', help='Intervalo de portas a serem escaneadas (ex: 1-1024)')
    parser.add_argument('-T', '--threads', type=int, default=50, help='Número de threads (padrão: 50)')
    parser.add_argument('--timeout', type=float, default=1.0, help='Timeout em segundos (padrão: 1.0)')
    parser.add_argument('--network-scan', action='store_true', help='Escanear todos os dispositivos na rede local')
    parser.add_argument('--max-hosts', type=int, help='Número máximo de hosts a serem escaneados na rede')
    parser.add_argument('--output', help='Salvar relatório em arquivo')
    
    args = parser.parse_args()
    
    banner()
    
    # Processa o intervalo de portas
    try:
        if '-' in args.port_range:
            porta_inicial, porta_final = map(int, args.port_range.split('-'))
        else:
            porta_inicial = porta_final = int(args.port_range)
        
        if porta_inicial < 1 or porta_final > 65535 or porta_inicial > porta_final:
            raise ValueError()
    except:
        print(Fore.RED + "[-] ERRO: Intervalo de portas inválido. Use o formato 'inicio-fim' (ex: 1-1024)" + Style.RESET_ALL)
        return
    
    # Determina o modo de escaneamento
    if args.network_scan or not args.target:
        # Modo de escaneamento de rede
        scanner_rede(porta_inicial, porta_final, args.threads, args.timeout, args.max_hosts)
    else:
        # Modo de escaneamento de host único
        scanner_portas(args.target, porta_inicial, porta_final, args.threads, args.timeout)
    
    # Salva o relatório se solicitado
    if args.output and portas_abertas:
        salvar_relatorio(args.output)

if __name__ == "__main__":
    main()
