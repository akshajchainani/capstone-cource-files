def word_occurrence_counter():
    n = int(input().strip())
    word_counts = {}
    word_order = []
    for _ in range(n):
        word = input().strip()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            word_order.append(word)
    print(len(word_order))
    print(" ".join(str(word_counts[word]) for word in word_order))
if __name__ == "__main__":
    word_occurrence_counter()
