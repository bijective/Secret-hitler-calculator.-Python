import math
print("How much L Sir?")
L = int(input())
print("How much F Sir?")
F = int(input())
Fl = F + L

nCk = math.comb(Fl, 3)
nCfff = math.comb(F, 3)
nClll = math.comb(L, 3)
nCl = math.comb(L, 1)
nCff = math.comb((Fl - L), 2)

lll = float((nClll/nCk)*100)
fff = float((nCfff/nCk)*100)
ffl = float((nCl*nCff/nCk)*100)
fll = float(100 - (ffl + fff + lll))
l = float(ffl+fll+lll)

print("FFF - %s"%round(fff, 2), "%", sep="")
print("FFL - %s"%round(ffl, 2), "%", sep="")
print("FLL - %s"%round(fll, 2), "%", sep="")
print("LLL - %s"%round(lll, 2), "%", sep="")
print("1+L - %s"%round(l, 2), "%", sep="")
