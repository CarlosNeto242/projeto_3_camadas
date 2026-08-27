

def build_header(h0=0, h1=0, h2=0, h3=0, h4=0, h5=0, h6=0, h7=0, h8=0, h9=0):
    lista = [h0, h1, h2, h3, h4, h5, h6, h7, h8, h9]
    for i in range(10):
        lista[i] = int.to_bytes(lista[i])
    return ''.join(lista)