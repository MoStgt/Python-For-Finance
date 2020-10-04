import math


def OptionPrice(asset, volatility, IntRate, Strike, Expiry, NoSteps):

    """Binomial Method for a European option"""
    timeStep = Expiry/NoSteps
    DiscountFactor = math.exp(-IntRate * timeStep)
    temp1 = math.exp((IntRate + volatility * volatility)* timeStep)
    temp2 = 0.5 * (DiscountFactor + temp1)
    u = temp2 + math.sqrt(temp2 * temp2 - 1)
    d = 1/u
    p = ((math.exp(IntRate * timeStep) - d) / (u - d))

    S = [0] * (NoSteps+1)
    V = [0] * (NoSteps+1)
    S[0] = asset

    for n in range(1, NoSteps+1, 1):
        for j in range(n, 0, -1):
            S[j] = u * S[j-1]

        S[0] = d * S[0]
    print(S)

    for j in range(0, NoSteps+1, 1):
        V[j] = Payoff(S[j], Strike)
    print(V)

    for n in range(NoSteps, 0, -1):
        for j in range(0, n, 1):
            V[j] = (p * V[j + 1] + (1 - p)*V[j])*DiscountFactor


    Price = V[0]
    return Price

def Payoff(S, K):
    Payoff = 0
    if S > K:
        Payoff = S - K
    return Payoff

print(OptionPrice(100, 0.2, 0.1, 100, 0.3332, 4))






