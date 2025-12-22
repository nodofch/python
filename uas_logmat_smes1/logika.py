def soal_1(A, B):
    X = 10
    if A and B:
        X = X + 5
    elif A and not B:
        X = X - 2
    else:
        X = 0

    if (not A) or B:
        X = X * 2
    return X


def soal_2(N):
    result = False
    for i in range(1, N + 1):
        if i % 2 == 0:
            result = not result
        else:
            result = result
        return result


def soal_3(P, Q):
    R = P ^ Q
    if R == True:
        P = not P
        Q = P or Q
    else:
        Q = not Q
    return P, Q


def soal_4(X, Y):
    status = "None"
    try:
        if X > 0 and (Y / X > 2):
            status = "Alpha"
        elif X == 0 or Y < 0:
            status = "Beta"
        else:
            status = "Gamma"
    except ZeroDivisionError:
        status = "Error: Devision by Zero"
    return status


def soal_5(Sinyal):
    state = 0
    for bit in Sinyal:
        if state == 0 and bit == True:
            state = 1
        elif state == 1 and bit == False:
            state = 2
        elif state == 2 and bit == True:
            state = 0
        else:
            state = state
    return state


print("A\tB\tOutput X")
for A in [True, False]:
    for B in [True, False]:
        hasil = soal_1(A, B)
        print(f"{A}\t{B}\t{hasil}")

print(" ")

for n in range(1, 5):
    print(f"N = {n}, Result = {soal_2(n)}")

print(" ")

print("P_in\tQ_in\tP_out\tQ_out")
for P in [True, False]:
    for Q in [True, False]:
        res_P, res_Q = soal_3(P, Q)
        print(f"{P}\t{Q}\t{res_P}\t{res_Q}")

print(" ")

pasangan = [(2, 5), (0, 10), (2, 2), (-1, -5)]
for x, y in pasangan:
    print(f"Input: ({x}, {y}) -> Output: {soal_4(x, y)}")

print(" ")

print(f"a) [T, F, T] -> State: {soal_5([True, False, True])}")
print(f"b) [T, T, F] -> State: {soal_5([True, True, False])}")
print(f"c) [F, F, T] -> State: {soal_5([False, False, True])}")
