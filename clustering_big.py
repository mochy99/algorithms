def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Input strings must have the same length")

    return sum(bit1 != bit2 for bit1, bit2 in zip(str1, str2))

def find_pairs_with_hamming_distance_less_than_2(strings):
    pairs = []
    n = len(strings)

    for i in range(n):
        for j in range(i + 1, n):
            distance = hamming_distance(strings[i], strings[j])
            if distance < 2:
                pairs.append((strings[i], strings[j]))

    return pairs

# Example usage
binary_strings = ["1101101", "1011001", "1111101", "1001001"]

result = find_pairs_with_hamming_distance_less_than_2(binary_strings)
print("Pairs with Hamming distance less than 2:", result)