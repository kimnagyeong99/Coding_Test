def solution(M, N):
    if M > N:
        a = (M-1) + (N-1)*M
    elif M < N:
        a = (N-1) + (M-1)*N
    else:
        a = (M-1) + (M-1)*M
    return a