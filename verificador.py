import string

def verificar_forca_senha(senha):
  comprimento_minimo = 8
  tem_letra_maiuscula = any(c in string.ascii_uppercase for c in senha)
  tem_letra_minuscula = any(c in string.ascii_lowercase for c in senha)
  tem_numero = any(c.isdigit() for c in senha)
  tem_caractere_especial = any(c in string.punctuation for c in senha)

  # Verificando o comprimento da senha
  if len(senha) < comprimento_minimo:
    return f"Sua senha e muito curta. Recomenda-se no minimo {comprimento_minimo} caracteres."

  # Verificando se a senha contém letras maiúsculas e minúsculas
  if not tem_letra_maiuscula:
    return "Sua senha deve conter pelo menos uma letra maiuscula."
  if not tem_letra_minuscula:
    return "Sua senha deve conter pelo menos uma letra minuscula."

  # Verificando se a senha contém números
  if not tem_numero:
    return "Sua senha deve conter pelo menos um numero."

  # Verificando se a senha contém caracteres especiais
  if not tem_caractere_especial:
    return "Sua senha nao atende aos requisitos de seguranca."

  # Verificando se a senha contém sequências comuns
  sequencias_comuns = ["123456", "abcdef"]
  for sequencia in sequencias_comuns:
    if sequencia in senha:
      return "Sua senha contem uma sequencia comum. Tente uma senha mais complexa."

  # Verificando se a senha contém palavras comuns
  palavras_comuns = ["password", "123456", "qwerty"]
  if senha in palavras_comuns:
    return "Sua senha e muito comum. Tente uma senha mais complexa."

  return "Sua senha atende aos requisitos de seguranca. Parabens!"

# Obtendo a senha do usuário
senha = input().strip()

# Verificando a força da senha
resultado = verificar_forca_senha(senha)

# Imprimindo o resultado
print(resultado)
