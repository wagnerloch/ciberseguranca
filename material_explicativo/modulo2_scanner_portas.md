# Módulo 2: Escaneamento de Portas

## Conceito Teórico

O escaneamento de portas é uma técnica fundamental tanto para administradores de sistemas quanto para profissionais de segurança. Consiste em verificar quais portas de comunicação estão abertas em um sistema, identificando serviços em execução e potenciais pontos de entrada para atacantes.

### Fundamentos de Portas e Serviços

Uma porta é um endpoint de comunicação em um sistema operacional. Cada serviço em execução (como servidores web, email, FTP) geralmente escuta em uma porta específica:

- **Portas bem conhecidas (1-1023)**: Atribuídas a serviços comuns
  - 80/443: HTTP/HTTPS (Web)
  - 22: SSH
  - 21: FTP
  - 25: SMTP (Email)
  - 53: DNS

- **Portas registradas (1024-49151)**: Usadas por aplicações de usuário
  - 3306: MySQL
  - 8080: Proxy/Web alternativo
  - 1433: Microsoft SQL Server

- **Portas dinâmicas/privadas (49152-65535)**: Usadas para conexões temporárias

### Tipos de Escaneamento de Portas

1. **TCP Connect Scan**: Estabelece uma conexão completa com a porta.
   - Vantagem: Altamente confiável, sem falsos positivos.
   - Desvantagem: Facilmente detectável em logs.

2. **SYN Scan (Half-open)**: Envia apenas pacote SYN, não completa a conexão.
   - Vantagem: Menos detectável, mais rápido.
   - Desvantagem: Requer privilégios de administrador.

3. **UDP Scan**: Verifica portas UDP abertas.
   - Vantagem: Identifica serviços UDP frequentemente negligenciados.
   - Desvantagem: Lento e menos confiável.

4. **FIN/NULL/XMAS Scans**: Utiliza pacotes TCP com flags específicas.
   - Vantagem: Pode passar por alguns firewalls.
   - Desvantagem: Não funciona em todos os sistemas operacionais.

5. **Escaneamento de versão**: Identifica versões de serviços em execução.
   - Vantagem: Fornece informações detalhadas para avaliação de vulnerabilidades.
   - Desvantagem: Mais intrusivo e detectável.

### Implicações de Segurança

O escaneamento de portas é frequentemente o primeiro passo em um ataque cibernético, permitindo ao atacante:

- Mapear a infraestrutura da rede
- Identificar sistemas ativos
- Descobrir serviços potencialmente vulneráveis
- Encontrar portas não padrão ou inesperadas
- Determinar o sistema operacional (OS fingerprinting)

## Demonstração Prática

O script `scanner_portas.py` implementa um scanner de portas TCP básico em Python, permitindo identificar portas abertas em um host alvo e os serviços associados a essas portas.

### Funcionalidades do Script

1. **Verificação de host ativo**: Testa se o host alvo está respondendo antes de iniciar o escaneamento.
2. **Escaneamento multithreaded**: Utiliza múltiplas threads para acelerar o processo.
3. **Identificação de serviços**: Tenta associar portas abertas a serviços conhecidos.
4. **Estatísticas de escaneamento**: Mostra o tempo decorrido e a velocidade do escaneamento.

### Como Utilizar o Script

```bash
# Escanear as portas padrão (1-1024) em um host
python3 scanner_portas.py -t 192.168.1.1

# Escanear um intervalo específico de portas
python3 scanner_portas.py -t 192.168.1.1 -p 20-25

# Escanear com mais threads para maior velocidade
python3 scanner_portas.py -t 192.168.1.1 -T 100

# Aumentar o timeout para redes mais lentas
python3 scanner_portas.py -t 192.168.1.1 --timeout 2.0
```

### Análise do Código

O script utiliza a biblioteca `socket` do Python para realizar as conexões TCP:

1. A função `verificar_porta()` tenta estabelecer uma conexão TCP com uma porta específica.
2. A função `worker()` processa múltiplas portas em paralelo usando threads.
3. A função `verificar_host_ativo()` verifica se o host está respondendo antes de iniciar o escaneamento completo.

## Medidas de Proteção

Para proteger sistemas contra escaneamento de portas e ataques subsequentes:

1. **Implementar firewalls adequados**:
   - Configurar regras para bloquear tráfego não autorizado
   - Implementar filtragem de pacotes stateful
   - Utilizar sistemas de detecção/prevenção de intrusão (IDS/IPS)

2. **Princípio do menor privilégio**:
   - Manter apenas as portas necessárias abertas
   - Fechar serviços não utilizados
   - Usar portas não padrão para serviços críticos (obscuridade adicional)

3. **Segmentação de rede**:
   - Separar redes em zonas de segurança
   - Implementar VLANs e ACLs
   - Utilizar DMZs para serviços públicos

4. **Monitoramento e alertas**:
   - Configurar alertas para escaneamentos de portas
   - Monitorar tentativas de conexão incomuns
   - Implementar honeypots para detectar atividades maliciosas

5. **Atualizações e patches**:
   - Manter todos os serviços atualizados
   - Aplicar patches de segurança regularmente
   - Remover ou desativar serviços desnecessários

## Exercícios Práticos

1. **Mapeamento de rede local**:
   - Utilize o script para mapear dispositivos na rede local do laboratório
   - Identifique serviços inesperados ou potencialmente inseguros
   - Discuta as implicações de segurança das descobertas

2. **Comparação de ferramentas**:
   - Compare os resultados do script com ferramentas profissionais como Nmap
   - Identifique diferenças e limitações da implementação em Python

3. **Detecção de escaneamento**:
   - Configure um sistema para registrar tentativas de escaneamento
   - Utilize diferentes técnicas de escaneamento e compare sua detectabilidade
   - Implemente medidas para dificultar o escaneamento preciso

4. **Análise de serviços**:
   - Para cada porta aberta encontrada, pesquise vulnerabilidades conhecidas
   - Discuta como um atacante poderia explorar esses serviços
   - Proponha medidas de mitigação específicas

## Discussão em Grupo

- Como equilibrar funcionalidade e segurança ao decidir quais portas manter abertas?
- Quais são as implicações legais e éticas do escaneamento de portas em diferentes contextos?
- Como as organizações podem detectar e responder a escaneamentos de portas maliciosos?
- De que forma o escaneamento de portas se encaixa em uma metodologia completa de teste de penetração?
