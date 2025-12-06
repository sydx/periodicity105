from fractions import Fraction
import matplotlib.pyplot as plt
import sympy

max_a = 6000

denominators = set()
index = 0
ratios = []
for a in range(2, max_a):
    print()
    sums = set()
    differences = set()
    candidate_count = 0
    goldbach_count = 0
    for b in range(1, a):
        imbalance = Fraction(a - b, a + b)
        seen = imbalance.denominator in denominators
        candidate = imbalance.numerator + imbalance.denominator == 2*a
        if candidate: candidate_count += 1
        goldbach = sympy.isprime(imbalance.numerator) and sympy.isprime(imbalance.denominator) and candidate
        if goldbach: goldbach_count += 1
        # print(index, a, b, imbalance, "" if seen else "novel", "candidate" if candidate else "", "goldbach" if goldbach else "")
        denominators.add(imbalance.denominator)
        sums.add(imbalance.numerator + imbalance.denominator)
        differences.add(imbalance.denominator - imbalance.numerator)
        index += 1
    ratios.append(goldbach_count / candidate_count)

plt.plot(ratios)
plt.show()
