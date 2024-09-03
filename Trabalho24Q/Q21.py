def somaImposto( custo, taxaImposto):

    taxaImposto = taxaImposto / 100

    precofinal = custo * taxaImposto + custo
    print(precofinal)
    return precofinal

somaImposto(100,10)