dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

segundosDias = dias * 86400
segundosHoras = horas * 3600
segundosMinutos = minutos * 60

print(f"O total de segundos é {segundosDias + segundosHoras + segundosMinutos + segundos}")
