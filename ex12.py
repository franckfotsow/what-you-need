def myfunction(x):
    return 2*x ** 3 + x-5
def tabulate(function, terminalInf, terminalUp, nbPas):
    if terminalInf > terminalUp:
        print("Error: borneInf must be less than borneSup.")
        return
    step = (terminalUp - terminalInf) / (nbPas - 1)
    for i in range(nbPas):
        x = terminalInf + i * step
        print(f"f({x}) = {function(x)}")
