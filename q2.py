def validate_postal_code(P):
    is_valid_range = len(P) == 6 and '1' <= P[0] <= '9' and all('0' <= ch <= '9' for ch in P)

    alternating_pairs = sum(1 for i in range(len(P) - 2) if P[i] == P[i + 2])

    return is_valid_range and alternating_pairs < 2

if __name__ == "__main__":
    P = input().strip()
    print(validate_postal_code(P))
