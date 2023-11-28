# Gerador de Senhas

Este script em Python gera senhas aleatórias que atendem a certos critérios de complexidade, incluindo pelo menos uma letra maiúscula, uma letra minúscula, um caractere especial, um número e um comprimento entre 12 e 30 caracteres.

## Uso

1. Execute o script `gerador_de_senhas.py` em um ambiente Python.
   
   ```bash
   python gerador_de_senhas.py
   ```

2. A senha gerada será exibida no console junto com o tamanho da senha.

## Detalhes de Implementação

- **Consistência na Geração:**
  - O script garante que cada senha gerada tenha pelo menos um caractere de cada tipo (maiúscula, minúscula, número, especial).

- **Uso de String para Senha:**
  - O código utiliza listas para construir a senha, proporcionando uma maneira eficiente de manipular caracteres antes de convertê-los em uma string final.

- **Embaralhamento:**
  - A senha é embaralhada para garantir que não haja padrões previsíveis.

- **Randomização Controlada:**
  - O script utiliza funções do módulo `random` de maneira controlada, evitando o uso excessivo de randomizações para melhor consistência nas senhas geradas.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorar este gerador de senhas.
