dic_cor_f = {0: "Preta", 1: "Marrom", 2: "Vermelha", 3: "Laranja", 4: "Amarela", 5: "Verde",
         6: "Azul", 7: "Violeta", 8: "Cinza", 9: "Branca"}

dic_cor_mu = {-3: "Rosa", -2: "Prata", -1: "Dourada", 0: "Preta", 1: "Marrom", 2: "Vermelha", 3: "Laranja", 4: "Amarela", 5: "Verde",
         6: "Azul", 7: "Violeta", 8: "Cinza", 9: "Branca"}

dic_cor_t = {20: "Nenhuma", 10: "Prata", 5 : "Dourada", 1: "Marrom",  2: "Vermelha", 0.05: "Laranja", 0.02: "Amarela", 0.5: "Verde",
          0.25: "Azul", 0.1: "Violeta", 0.01: "Cinza"}

dic_mu = {"m": -3, "-": 0, "K": 3, "M": 6, "G": 9}

def IEC60062(resistencia):
    FM, T = resistencia.split()
    M = FM[-1]
    F = FM.replace(M, '')
    indice = 0

    if '.' not in T:
        T = int(T)
    else:
        T = float(T)

    if '.' in F:
        F_cor = str(F.replace('.', '')) # valor fatores da resistencia para atribuir cor
        bef_point, aft_point = F.split('.')
        if len(aft_point) == 1:
            F = F + '0'
            indice -= 1
        elif len(aft_point) == 2:
            F = F + '00'
            indice -= 2
        F_int = int(F.replace('.', '')) # valor final da resistencia para multiplicar

    # Se o fator só tiver 1 dígito, será adicionado um 0, e multiplicado por 10**-1 para equilibrar
    else:
        if len(F) < 2:
            F = F + '0'
            indice -= 1
        # Entrada "normal":
        F_int = int(F) # transformando em inteiro
        F_cor = str(F)  # valor fatores da resistencia para atribuir cor


    # calculando resistencia:
    indice += dic_mu[M]

    # atribuindo cor do F
    # cada cor individualmente atribuida, pra depois entrar na lista de cores
    cor_F1 = dic_cor_f.get(int(F_cor[0]))
    cor_F2 = dic_cor_f.get(int(F_cor[1]))
    if len(F_cor) == 3:
        cor_F3 = dic_cor_f.get(int(F_cor[2]))

    # atribuindo cor do M
    cor_M = dic_cor_mu.get(indice)
    # atribuindo cor do T
    cor_T = dic_cor_t.get(T)

    #cores relacionadas a cada caso
    cores = [cor_F1, cor_F2, cor_M, cor_T]
    if len(F_cor) == 3:
        cores = [cor_F1, cor_F2, cor_F3, cor_M, cor_T]

    return cores
