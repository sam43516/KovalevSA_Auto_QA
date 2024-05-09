def bank(X,Y):
    for i in range(Y):
        X+= X*0.1
    return X

print(bank(1000,10))