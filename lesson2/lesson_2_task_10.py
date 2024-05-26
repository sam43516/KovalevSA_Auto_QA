def bank(X,Y):
    start = X
    for i in range(Y):
        X+= X*0.17
    return X

print(bank(500000,2))
