nota_NP1 = float(input("Nota NP1: "))
nota_NP2 = float(input("Nota NP2: "))

media_NPs = ( nota_NP1 + nota_NP2 ) / 2

if media_NPs >= 7:
    print(f"Você foi aprovado! Média: {media_NPs}")

else:
    print(f"Você ficou de exame! Média: {media_NPs}")
    inpt_exame = str(input("Você realizou o exame? [S/N]"))

    if inpt_exame == 'S':
        nota_Exame = float(input("Nota Exame: "))
        media_Exame = ( nota_Exame + media_NPs ) / 2

        if media_Exame >= 5:
            print(f"Você passou no exame! Média: {media_Exame}")
        else:
            print("Você ficou de DP! Média: {media_Exame}")

    else:
        print("Agende seu exame!!!")
