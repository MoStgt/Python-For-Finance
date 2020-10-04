import math

def USOptionPrice(asset, volatility, IntRate, Strike, Expiry, NoSteps):
    """Binomial Method for a US option"""

    timeStep = Expiry / NoSteps
    DiscountFactor = math.exp(-IntRate * timeStep)
    temp1 = math.exp((IntRate + volatility * volatility) * timeStep)
    temp2 = 0.5 * (DiscountFactor + temp1)
    u = temp2 + math.sqrt(temp2 * temp2 - 1)
    d = 1 / u
    p = ((math.exp(IntRate * timeStep) - d) / (u - d))

    w, h = NoSteps + 1, NoSteps + 1
    S = [[0 for x in range(w)] for y in range(h)]
    V = [[0 for x in range(w)] for y in range(h)]
    S[0][0] = asset

    for n in range(1, NoSteps + 1, 1):
        for j in range(n, 0, -1):
            S[j][n] = u * S[j - 1][n - 1]

        S[0][n] = d * S[0][n - 1]
    print(S)

    for j in range(0, NoSteps + 1, 1):
        V[j][NoSteps] = Payoff(S[j][NoSteps], Strike)
    print(V)

    for n in range(NoSteps, 0, -1):
        for j in range(0, n, 1):
            V[j][n - 1] = max((p * V[j + 1][n] + (1 - p) * V[j][n]) * DiscountFactor, Payoff(S[j][n - 1], Strike))

    Price = V[0][0]
    return Price


def Payoff(S, K):
    Payoff = 0
    if S > K:
        Payoff = S - K
    return Payoff


print(USOptionPrice(100, 0.2, 0.1, 100, 0.3332, 4))