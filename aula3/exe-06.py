materia1 = float(input("Nota Materia 1: "))
materia2 = float(input("Nota Materia 2: "))
materia3 = float(input("Nota Materia 3: "))

notaMedia = 7

media = materia1 > notaMedia and materia2 > notaMedia and materia3 > notaMedia

print(f"As notas são {materia1}, {materia2} e {materia3}. Com isso a afirmação é {media}")
