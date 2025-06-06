def media():
    try:
        nota1 = float(input("Digite a primeira nota: ").strip())
        nota2 = float(input("Digite a segunda nota: ").strip())

        media_final = (nota1 + nota2) / 2
        print(f"Média: {media_final:.2f}")
    except ValueError:
        print("Erro: Digite apenas números válidos para as notas.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

media()
