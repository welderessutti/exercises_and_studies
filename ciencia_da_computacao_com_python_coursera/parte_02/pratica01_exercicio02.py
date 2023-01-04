def sao_multiplicaveis(m1, m2):
    dim_m1 = len(m1), len(m1[0])
    dim_m2 = len(m2), len(m2[0])
    if dim_m1[1] == dim_m2[0]:
        return True
    else:
        return False
