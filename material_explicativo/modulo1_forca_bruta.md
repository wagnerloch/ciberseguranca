# Módulo 1: Ataques de Força Bruta

## Conceito Teórico

Os ataques de força bruta são uma das técnicas mais antigas e diretas utilizadas para comprometer senhas e sistemas de autenticação. Neste tipo de ataque, o invasor tenta sistematicamente todas as combinações possíveis de caracteres ou utiliza uma lista de senhas comuns (wordlist) até encontrar a senha correta.

### Tipos de Ataques de Força Bruta

1. **Força Bruta Pura**: Testa todas as combinações possíveis de caracteres.
   - Exemplo: Para uma senha de 4 dígitos numéricos, testa de 0000 a 9999.
   - Vantagem: Garantia de encontrar a senha eventualmente.
   - Desvantagem: Pode levar muito tempo para senhas complexas.

2. **Ataque de Dicionário**: Utiliza uma lista predefinida de palavras comuns.
   - Exemplo: Testa palavras como "password", "123456", "admin", etc.
   - Vantagem: Muito mais rápido que força bruta pura.
   - Desvantagem: Limitado às palavras presentes no dicionário.

3. **Ataque Híbrido**: Combina palavras de dicionário com variações e números.
   - Exemplo: A partir de "password", testa "password123", "Password!", etc.
   - Vantagem: Mais eficaz contra senhas que usam palavras comuns com modificações.

4. **Ataque de Rainbow Tables**: Utiliza tabelas pré-computadas de hashes.
   - Vantagem: Extremamente rápido para encontrar senhas a partir de hashes.
   - Desvantagem: Requer grande espaço de armazenamento e é ineficaz contra senhas com salt.

### Fatores que Influenciam a Eficácia

- **Complexidade da senha**: Comprimento, variedade de caracteres, aleatoriedade.
- **Mecanismos de proteção**: Bloqueio após tentativas falhas, CAPTCHAs, atrasos.
- **Poder computacional**: Hardware disponível para o ataque.
- **Algoritmo de hash**: Alguns algoritmos são mais resistentes a ataques que outros.

## Demonstração Prática

O script `forca_bruta.py` demonstra um ataque de dicionário contra um hash de senha. Este é um exemplo educacional que ilustra como funciona um ataque básico de força bruta usando uma lista de senhas comuns.

### Funcionalidades do Script

1. **Geração de hash**: Cria hashes de senhas usando diferentes algoritmos (MD5, SHA1, SHA256).
2. **Criação de wordlist**: Gera uma lista de senhas comuns para demonstração.
3. **Ataque de força bruta**: Testa cada senha da lista contra um hash alvo.
4. **Estatísticas**: Mostra o número de tentativas, tempo decorrido e velocidade do ataque.

### Como Utilizar o Script

```bash
# Criar uma wordlist de demonstração
python3 forca_bruta.py --create-wordlist senhas.txt

# Gerar um hash para uma senha específica (para demonstração)
python3 forca_bruta.py --password "senha123" --algorithm md5

# Realizar um ataque de força bruta
python3 forca_bruta.py --wordlist senhas.txt --hash "5f4dcc3b5aa765d61d8327deb882cf99" --algorithm md5
```

### Análise do Código

O script foi desenvolvido de forma didática, com comentários detalhados para facilitar a compreensão. Alguns pontos importantes:

1. A função `simular_verificacao_senha()` demonstra como sistemas verificam senhas comparando hashes.
2. A função `ataque_forca_bruta()` implementa o processo de testar cada senha da lista.
3. O parâmetro `delay` foi adicionado para fins educacionais, permitindo visualizar o processo em sala de aula.

## Medidas de Proteção

Para proteger sistemas contra ataques de força bruta, recomenda-se:

1. **Políticas de senha robustas**:
   - Exigir senhas longas (mínimo 12 caracteres)
   - Combinar letras maiúsculas, minúsculas, números e símbolos
   - Evitar palavras de dicionário e informações pessoais

2. **Implementar mecanismos de proteção**:
   - Bloqueio temporário após múltiplas tentativas falhas
   - Atrasos progressivos entre tentativas
   - Uso de CAPTCHAs
   - Autenticação de dois fatores (2FA)

3. **Utilizar algoritmos de hash seguros**:
   - Algoritmos modernos como bcrypt, Argon2 ou PBKDF2
   - Implementar salt único para cada usuário
   - Utilizar funções de derivação de chave com custo computacional ajustável

4. **Monitoramento e alertas**:
   - Detectar e alertar sobre padrões suspeitos de login
   - Registrar tentativas de acesso falhas
   - Implementar sistemas de detecção de intrusão

## Exercícios Práticos

1. **Análise de Wordlists**:
   - Examine diferentes wordlists disponíveis (como RockYou)
   - Identifique padrões comuns em senhas vazadas
   - Discuta por que certas senhas são tão prevalentes

2. **Teste de Resistência**:
   - Modifique o script para medir o tempo necessário para quebrar senhas de diferentes complexidades
   - Compare a eficácia de diferentes algoritmos de hash

3. **Implementação de Proteções**:
   - Modifique o script para implementar um mecanismo de atraso progressivo
   - Adicione um sistema de bloqueio após X tentativas falhas

4. **Auditoria de Senhas**:
   - Utilize o script (em ambiente controlado) para verificar a segurança de senhas comuns
   - Discuta como empresas podem implementar verificações de senhas vazadas

## Discussão em Grupo

- Como equilibrar segurança e usabilidade em políticas de senha?
- Quais são as implicações éticas de desenvolver e compartilhar ferramentas de força bruta?
- Como a evolução do poder computacional afeta a segurança de senhas ao longo do tempo?
- Senhas vs. biometria vs. tokens: qual o futuro da autenticação?
