#Given
X_0 = 0
X_1 = 1
P_X_0 = 0.3
P_X_1 = 0.7

#Finding E(X)
E_X = X_0*P_X_0+X_1*P_X_1 #formula
print("E(X) =",E_X)

#Finding Var(X)
Var_X = X_0**2*P_X_0 + X_1**2*P_X_1 - E_X**2 #formula
Value = "{:.2f}".format(Var_X)
print("Var(X) =",Value)
