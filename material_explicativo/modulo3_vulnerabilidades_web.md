# Módulo 3: Análise de Vulnerabilidades Web

## Conceito Teórico

As aplicações web são alvos frequentes de ataques cibernéticos devido à sua ampla exposição e complexidade. A análise de vulnerabilidades web é o processo de identificar falhas de segurança em sites e aplicações web que poderiam ser exploradas por atacantes.

### Vulnerabilidades Web Comuns

1. **Injeção (SQL, NoSQL, OS, LDAP)**:
   - Ocorre quando dados não confiáveis são enviados como parte de um comando ou consulta
   - Exemplo: Injeção SQL permite manipular consultas ao banco de dados
   - Impacto: Acesso não autorizado a dados, modificação ou destruição de informações

2. **Quebra de Autenticação**:
   - Falhas nos mecanismos de autenticação e gerenciamento de sessão
   - Exemplo: Senhas fracas, tokens expostos, fixação de sessão
   - Impacto: Comprometimento de contas de usuários, incluindo administradores

3. **Exposição de Dados Sensíveis**:
   - Proteção inadequada de informações confidenciais
   - Exemplo: Transmissão sem criptografia, armazenamento inseguro de senhas
   - Impacto: Vazamento de dados pessoais, financeiros ou corporativos

4. **XML External Entities (XXE)**:
   - Processadores XML mal configurados interpretam entidades externas
   - Impacto: Divulgação de arquivos internos, execução remota de código

5. **Quebra de Controle de Acesso**:
   - Restrições inadequadas sobre ações de usuários autenticados
   - Exemplo: Elevação de privilégios, acesso a funcionalidades restritas
   - Impacto: Usuários podem acessar dados ou funções não autorizadas

6. **Configuração Incorreta de Segurança**:
   - Configurações padrão inseguras, diretórios abertos, mensagens de erro detalhadas
   - Impacto: Exposição de informações sensíveis sobre a infraestrutura

7. **Cross-Site Scripting (XSS)**:
   - Injeção de scripts maliciosos em páginas visualizadas por outros usuários
   - Tipos: Refletido, Armazenado e DOM-based
   - Impacto: Roubo de sessões, redirecionamentos maliciosos, modificação de conteúdo

8. **Deserialização Insegura**:
   - Deserialização de dados não confiáveis sem verificação adequada
   - Impacto: Execução remota de código, manipulação de objetos

9. **Uso de Componentes com Vulnerabilidades Conhecidas**:
   - Bibliotecas, frameworks e módulos desatualizados
   - Impacto: Exploração de vulnerabilidades já documentadas e corrigidas em versões mais recentes

10. **Registro e Monitoramento Insuficientes**:
    - Falha na detecção e resposta a incidentes
    - Impacto: Persistência de ataques, dificuldade em investigar incidentes

### Metodologia de Análise

A análise de vulnerabilidades web geralmente segue estas etapas:

1. **Reconhecimento**: Coleta de informações sobre a aplicação alvo
2. **Mapeamento**: Identificação de páginas, parâmetros e funcionalidades
3. **Descoberta**: Identificação de vulnerabilidades potenciais
4. **Exploração**: Verificação da existência real de vulnerabilidades
5. **Análise**: Avaliação do impacto e riscos associados
6. **Documentação**: Registro detalhado das descobertas
7. **Remediação**: Recomendações para correção das vulnerabilidades

## Demonstração Prática

O script `vulnerabilidades_web.py` implementa uma ferramenta básica de análise de vulnerabilidades web, focando em aspectos fundamentais de segurança como cabeçalhos HTTP, formulários, cookies e potenciais pontos de injeção SQL.

### Funcionalidades do Script

1. **Verificação de Cabeçalhos de Segurança**: Analisa a presença de cabeçalhos HTTP importantes para segurança.
2. **Análise de Formulários**: Identifica formulários e verifica problemas como método GET para dados sensíveis e ausência de proteção CSRF.
3. **Verificação de Cookies**: Analisa configurações de segurança em cookies (Secure, HttpOnly, SameSite).
4. **Detecção Básica de Injeção SQL**: Testa parâmetros URL para possíveis vulnerabilidades de injeção SQL.

### Como Utilizar o Script

```bash
# Análise básica de um site
python3 vulnerabilidades_web.py -u exemplo.com

# Desativar a verificação de injeção SQL (para sites sensíveis)
python3 vulnerabilidades_web.py -u exemplo.com --no-sql
```

### Análise do Código

O script utiliza a biblioteca `requests` para interações HTTP e `BeautifulSoup` para análise HTML:

1. A função `verificar_cabecalhos_seguranca()` verifica a presença de cabeçalhos HTTP de segurança.
2. A função `verificar_formularios()` analisa formulários HTML em busca de configurações inseguras.
3. A função `verificar_cookies()` examina as propriedades de segurança dos cookies.
4. A função `verificar_injecao_sql_simples()` testa parâmetros URL com payloads básicos de SQL injection.

## Medidas de Proteção

Para proteger aplicações web contra vulnerabilidades comuns:

1. **Validação e Sanitização de Entrada**:
   - Validar todos os dados de entrada no servidor
   - Implementar listas de permissão (whitelist) em vez de listas de bloqueio
   - Utilizar bibliotecas de sanitização para diferentes contextos (HTML, SQL, etc.)

2. **Implementar Cabeçalhos de Segurança**:
   - Content-Security-Policy (CSP): Mitigar XSS e outros ataques de injeção
   - X-Content-Type-Options: Prevenir MIME sniffing
   - X-Frame-Options: Proteger contra clickjacking
   - Strict-Transport-Security (HSTS): Forçar conexões HTTPS

3. **Segurança em Cookies**:
   - Flags Secure: Transmitir apenas via HTTPS
   - HttpOnly: Prevenir acesso via JavaScript
   - SameSite: Proteger contra CSRF
   - Definir prazos de expiração adequados

4. **Proteção Contra CSRF**:
   - Implementar tokens anti-CSRF em formulários
   - Verificar o cabeçalho Referer/Origin
   - Utilizar SameSite cookies

5. **Prevenção de Injeção SQL**:
   - Utilizar consultas parametrizadas ou prepared statements
   - Implementar ORM (Object-Relational Mapping)
   - Aplicar princípio do menor privilégio nas contas de banco de dados

6. **Autenticação Segura**:
   - Implementar autenticação multifator (MFA)
   - Utilizar algoritmos seguros para armazenamento de senhas (bcrypt, Argon2)
   - Implementar políticas de bloqueio após tentativas falhas

7. **Gerenciamento de Dependências**:
   - Manter bibliotecas e frameworks atualizados
   - Utilizar ferramentas de análise de dependências (OWASP Dependency Check)
   - Implementar processo de revisão de segurança para novas dependências

8. **Configuração Segura**:
   - Remover funcionalidades, páginas e APIs desnecessárias
   - Desativar recursos não utilizados
   - Implementar HTTPS em toda a aplicação
   - Configurar adequadamente servidores web e frameworks

## Exercícios Práticos

1. **Análise de Cabeçalhos**:
   - Utilize o script para analisar cabeçalhos de segurança em sites populares
   - Compare os resultados entre diferentes tipos de sites (bancos, redes sociais, blogs)
   - Implemente os cabeçalhos ausentes em uma aplicação web de exemplo

2. **Identificação de Vulnerabilidades XSS**:
   - Modifique o script para detectar potenciais vulnerabilidades XSS em formulários
   - Teste em um ambiente controlado com aplicações web vulneráveis (como DVWA)
   - Implemente correções para as vulnerabilidades encontradas

3. **Análise de Formulários**:
   - Examine formulários de login em diferentes sites
   - Identifique boas e más práticas de implementação
   - Desenvolva um formulário seguro com todas as proteções necessárias

4. **Teste de Injeção SQL**:
   - Configure um ambiente de teste com uma aplicação web vulnerável
   - Utilize o script para identificar pontos de injeção SQL
   - Modifique o script para testar payloads mais avançados

## Discussão em Grupo

- Como equilibrar segurança e usabilidade em aplicações web modernas?
- Qual o papel das ferramentas automatizadas vs. testes manuais na identificação de vulnerabilidades?
- Como as organizações devem priorizar a correção de vulnerabilidades web?
- De que forma o desenvolvimento seguro (DevSecOps) pode reduzir vulnerabilidades web?
