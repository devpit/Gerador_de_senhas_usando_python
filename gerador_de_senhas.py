import random
import string

def gerador_de_senhas():
    tamanho = random.randint(12, 30)

    # Garante pelo menos um caractere de cada tipo
    senha = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Preenche o restante da senha
    senha += random.choices(string.ascii_letters + string.digits + string.punctuation, k=tamanho - 4)

    # Embaralha a senha
    random.shuffle(senha)

    # Retorna a senha como string
    return ''.join(senha)

senha = gerador_de_senhas()
print(f'A senha gerada foi: {senha}')
print(f'O tamanho da senha é {len(senha)}')
