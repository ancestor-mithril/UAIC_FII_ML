import functions as f

with open("input.txt", "r") as fd:
    M, H = map(float, fd.read().split())


print("M = ", int(M))
print("H = ", H)


# 2 * gini(p) = 4 * p * (1 - p) =~ H <=> - 4 * (p ** 2) + 4 * p - H =~ 0
a = -4
b = 4
c = -H
p_1, p_2 = f.solve_quadratic_equation(a, b, c)
print("p_1 = ", p_1)
print("p_2 = ", p_2)
p = min(p_1, p_2)

print("Number of incorrectly classified examples: ~", int(p * 100 * M), " from ", int(M))


