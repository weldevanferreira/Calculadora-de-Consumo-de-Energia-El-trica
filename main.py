while True:
    cv = 0.735499 # Não mexa neste valor, ele deve ser constante

    cvs = float(input("Informe a quantos de CVs? "))
    h = float(input("Informe o tempo em Horas? "))
    m = float(input("Informe a quantidade de dias por Mês? "))
    tr = float(input("Informe o valor da tarifa da sua região? "))

    kWh = cv * cvs
    kWhm = h * m
    total = kWh * kWhm
    tarifa = total * tr
    print(f"Um motor com {cvs} CV, ligado por {h} horas por dia, consome {total} kWh por mês. \nComsumo mensal e de R$:{round(tarifa, 2)} Por mês.")
    s = float(input("Deseja continuar? 0 para sim/ 1 para não! "))
    if s == 1:
        print("Fim!")
        exit()
    else:
        continue
