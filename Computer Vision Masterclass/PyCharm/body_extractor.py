pontos = []

def verificar_bracos_ACIMA(pontos):
    # BRAÇO ESQUERDO
    # posição horizontal
    cabeca_V = 0
    punhoEsquerdo_H = 0
    # posição veritical
    ombroEsquerdo_H = 0
    punhoEsquerdo_V = 0

    # BRAÇO DIREITO
    # posição horizontal
    punhoDireito_H = 0
    # posição veritical
    punhoDireito_V = 0
    ombroDireito_H = 0

    for indx, p in enumerate(pontos):
        # BRAÇOS
        # 0 ao 8 - ESQUERDO
        # 0 ao 5 - DIREITO
        # print(indx, p)
        # p[0] é na horizontal
        # p[1] é na vertical

        # CABEÇA
        if indx == 0:
            cabeca_V = p[1]

        # OMBRO DIREITO
        elif indx == 2:
            ombroDireito_H = p[0]

        # PUNHO DIREITO
        elif indx == 4:
            punhoDireito_H = p[0]
            punhoDireito_V = p[1]

        # OMBRO ESQUERDO
        elif indx == 5:
            ombroEsquerdo_H = p[0]

        # PUNHO ESQUERDO
        elif indx == 7:
            punhoEsquerdo_H = p[0]
            punhoEsquerdo_V = p[1]

    # quanto menor a posição da altura, mais alto o ponto está
    # quanto maior a posição da altura, mais baixo o ponto está
    # COMPARANDO NA VERITICAL
    if punhoEsquerdo_V and punhoDireito_V < cabeca_V:
        # print('Punho acima da cabeça')
        # COMPARANDO NA HORIZONTAL
        if (punhoEsquerdo_H <= ombroEsquerdo_H) and (punhoDireito_H >= ombroDireito_H):
            #     # print('Punhos passaram da linha do ombro')
            return True
    else:
        return False


def verificar_bracos_ABAIXO(pontos):
    # BRAÇO ESQUERDO
    # posição horizontal
    punhoEsquerdo_H = 0
    # posição veritical
    ombroEsquerdo_H = 0
    ombroEsquerdo_V = 0
    punhoEsquerdo_V = 0

    # BRAÇO DIREITO
    # posição horizontal
    # posição veritical
    punhoDireito_V = 0
    ombroDireito_H = 0

    for indx, p in enumerate(pontos):
        # OMBRO DIREITO
        if indx == 2:
            ombroDireito_H = p[0]
            ombroDireito_V = p[1]

        # PUNHO DIREITO
        if indx == 4:
            punhoDireito_V = p[1]

        # OMBRO ESQUERDO
        if indx == 5:
            ombroEsquerdo_H = p[0]
            ombroEsquerdo_V = p[1]

        # PUNHO ESQUERDO
        if indx == 7:
            punhoEsquerdo_V = p[1]
            punhoEsquerdo_H = p[0]

    if (punhoEsquerdo_V >= ombroEsquerdo_V) and (punhoDireito_V >= ombroDireito_V):
        if (punhoEsquerdo_H <= ombroEsquerdo_H) and (punhoEsquerdo_H >= ombroDireito_H):
            print('posicao inicial')
            return True
    else:
        return False


def verificar_pernas_AFASTADAS(pontos):
    # PERNAS
    # 11 ao 14 a esquerda
    # 8 ao 11 a direita
    tornozeloEsquerdo_H = 0
    tornozeloDireito_H = 0
    quadrilEsquerdo_H = 0
    quadrilDireito_H = 0

    for indx, p in enumerate(pontos):
        # print(indx, p)
        # p[0] é na horizontal
        # p[1] é na vertical
        if indx == 0:
            quadrilDireito_H = p[0]
        if indx == 2:
            tornozeloDireito_H = p[0]
        if indx == 3:
            quadrilEsquerdo_H = p[0]
        if indx == 5:
            tornozeloEsquerdo_H = p[0]
    if (tornozeloDireito_H < quadrilDireito_H) and (tornozeloEsquerdo_H > quadrilEsquerdo_H):
        return True
    else:
        return False


def verificar_pernas_JUNTAS(pontos):
    # PERNAS
    # 11 ao 14 a esquerda
    # 8 ao 11 a direita
    tornozeloEsquerdo_H = 0
    tornozeloDireito_H = 0
    quadrilEsquerdo_H = 0
    quadrilDireito_H = 0

    for indx, p in enumerate(pontos):
        # print(indx, p)
        # p[0] é na horizontal
        # p[1] é na vertical
        if indx == 0:
            quadrilDireito_H = p[0]
        if indx == 2:
            tornozeloDireito_H = p[0]
        if indx == 3:
            quadrilEsquerdo_H = p[0]
        if indx == 5:
            tornozeloEsquerdo_H = p[0]
    if (tornozeloDireito_H >= quadrilDireito_H) and (tornozeloEsquerdo_H <= quadrilEsquerdo_H):
        return True
    else:
        return False
