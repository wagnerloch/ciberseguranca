# Módulo 4: Engenharia Social e Phishing

## Conceito Teórico

A engenharia social é uma técnica que explora o elemento humano da segurança, manipulando pessoas para que revelem informações confidenciais ou realizem ações que comprometam a segurança. Diferentemente de ataques puramente técnicos, a engenharia social foca nas vulnerabilidades humanas como confiança, medo, urgência e desejo de ajudar.

### Tipos de Ataques de Engenharia Social

1. **Phishing**: Envio de comunicações fraudulentas que parecem vir de fontes confiáveis.
   - **Spear Phishing**: Ataques direcionados a indivíduos ou organizações específicas.
   - **Whaling**: Direcionado a executivos de alto nível.
   - **Smishing**: Phishing via SMS.
   - **Vishing**: Phishing via chamadas telefônicas.

2. **Pretexting**: Criação de um cenário fabricado para obter informações específicas.
   - Exemplo: Fingir ser do suporte técnico para obter credenciais.

3. **Baiting**: Oferecimento de algo atraente para induzir a vítima a uma ação.
   - Exemplo: Pen drives infectados deixados em locais públicos.

4. **Quid Pro Quo**: Oferta de um serviço ou benefício em troca de informações.
   - Exemplo: Oferecer ajuda técnica gratuita que na verdade é maliciosa.

5. **Tailgating/Piggybacking**: Ganhar acesso físico não autorizado seguindo alguém.
   - Exemplo: Entrar em áreas restritas seguindo funcionários autorizados.

6. **Scareware**: Indução de medo para que a vítima tome ações precipitadas.
   - Exemplo: Falsos alertas de vírus que levam a downloads maliciosos.

### Elementos Psicológicos Explorados

- **Autoridade**: Tendência a obedecer figuras de autoridade.
- **Escassez**: Percepção de que algo é raro ou tem tempo limitado.
- **Urgência**: Pressão para agir rapidamente sem tempo para reflexão.
- **Familiaridade**: Confiança em pessoas ou marcas conhecidas.
- **Reciprocidade**: Tendência a retribuir favores.
- **Prova social**: Tendência a seguir o comportamento de outros.
- **Medo**: Reações impulsivas diante de ameaças percebidas.

## Demonstração Prática

O script `phishing_educacional.py` demonstra como atacantes podem criar materiais de phishing convincentes, incluindo emails e páginas web falsas que imitam organizações legítimas.

### Funcionalidades do Script

1. **Geração de Emails de Phishing**: Cria emails fraudulentos baseados em templates comuns (redefinição de senha, prêmios, faturas).
2. **Criação de Páginas de Phishing**: Gera páginas HTML que imitam sites legítimos para captura de credenciais.
3. **Geração de QR Codes**: Cria QR codes que direcionam para páginas de phishing.
4. **Elementos de Urgência**: Opção para adicionar linguagem que cria senso de urgência.

### Como Utilizar o Script

```bash
# Gerar um email de phishing de redefinição de senha
python3 phishing_educacional.py --email --empresa "Banco Nacional" --nome "João Silva" --email-dest "joao.silva@exemplo.com" --template-email reset_senha

# Criar uma página de phishing de login
python3 phishing_educacional.py --pagina --empresa "Rede Social" --template-pagina login --output ./demo_phishing

# Gerar uma página de pagamento com QR code
python3 phishing_educacional.py --pagina --qrcode --empresa "Loja Online" --template-pagina pagamento --output ./demo_phishing

# Adicionar elementos de urgência aos materiais
python3 phishing_educacional.py --email --empresa "Serviço Cloud" --urgencia --template-email fatura --output ./demo_phishing
```

### Análise do Código

O script foi desenvolvido para fins educacionais, demonstrando técnicas comuns usadas em ataques de phishing:

1. A função `criar_email_phishing()` gera emails com diferentes narrativas persuasivas.
2. A função `criar_pagina_phishing()` cria páginas HTML que imitam sites legítimos.
3. O script inclui alertas educacionais nas páginas geradas, mostrando como credenciais poderiam ser roubadas.
4. Todos os materiais incluem avisos claros sobre seu propósito exclusivamente educacional.

## Medidas de Proteção

Para proteger indivíduos e organizações contra ataques de engenharia social:

1. **Educação e Conscientização**:
   - Treinamento regular sobre ameaças de engenharia social
   - Simulações de phishing para testar e educar funcionários
   - Cultura de segurança que valoriza o questionamento saudável

2. **Verificação Multicanal**:
   - Confirmar solicitações sensíveis por um canal diferente
   - Implementar processos de verificação para solicitações incomuns
   - Nunca usar informações de contato fornecidas na comunicação suspeita

3. **Políticas e Procedimentos**:
   - Estabelecer protocolos claros para solicitações sensíveis
   - Implementar processos de aprovação para transferências financeiras
   - Definir canais oficiais de comunicação

4. **Tecnologias de Proteção**:
   - Filtros anti-spam e anti-phishing
   - Autenticação multifator (MFA)
   - Verificação de URLs e anexos
   - Soluções de segurança de email com análise de comportamento

5. **Verificação de Identidade**:
   - Implementar métodos robustos de verificação de identidade
   - Utilizar perguntas de segurança não baseadas em informações públicas
   - Evitar uso de informações pessoais facilmente obtidas em redes sociais

6. **Gerenciamento de Informações Públicas**:
   - Limitar informações organizacionais disponíveis publicamente
   - Treinar funcionários sobre o que compartilhar em redes sociais
   - Implementar políticas de classificação de informações

## Exercícios Práticos

1. **Análise de Emails de Phishing**:
   - Examine emails de phishing reais (com identificadores removidos)
   - Identifique indicadores de phishing (erros gramaticais, domínios suspeitos, etc.)
   - Discuta como cada email tenta manipular o destinatário

2. **Criação e Análise de Campanhas Educativas**:
   - Utilize o script para criar materiais de phishing educativos
   - Implemente uma campanha simulada em ambiente controlado
   - Analise os resultados e discuta estratégias de conscientização

3. **Desenvolvimento de Políticas**:
   - Crie políticas organizacionais para mitigar riscos de engenharia social
   - Desenvolva um fluxograma de resposta a incidentes de phishing
   - Elabore materiais de treinamento para diferentes níveis organizacionais

4. **Análise Técnica de Phishing**:
   - Examine o código-fonte de páginas de phishing
   - Identifique técnicas usadas para ocultar a verdadeira natureza da página
   - Implemente verificações técnicas para detectar sites de phishing

## Discussão em Grupo

- Como equilibrar segurança e eficiência operacional em organizações?
- Qual o papel da cultura organizacional na prevenção de ataques de engenharia social?
- Como as tecnologias emergentes (IA, deepfakes) estão mudando o panorama da engenharia social?
- Quais são as responsabilidades éticas de profissionais de segurança ao realizar testes de engenharia social?

## Sinais de Alerta em Comunicações

### Em Emails:
- Erros gramaticais e ortográficos
- Domínios ligeiramente diferentes dos oficiais
- Solicitações urgentes ou ameaçadoras
- Pedidos incomuns de informações sensíveis
- Links suspeitos ou encurtados
- Saudações genéricas ("Caro cliente")
- Ofertas boas demais para ser verdade

### Em Páginas Web:
- URLs não correspondentes ao site legítimo
- Ausência de HTTPS ou certificado inválido
- Erros de design ou formatação
- Formulários solicitando informações excessivas
- Páginas que não carregam completamente
- Redirecionamentos suspeitos

### Em Interações Pessoais/Telefônicas:
- Pressão para ação imediata
- Relutância em fornecer informações de contato para verificação
- Solicitação de informações que a organização já deveria ter
- Ofertas não solicitadas que requerem informações pessoais
- Tentativas de evitar processos formais de verificação
