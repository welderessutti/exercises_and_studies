def has_stop_codon(dna, frame=0):
    """
    This function checks if given sequence has in frame stop codons.

    :param dna: Dna sequence.
    :param frame: Step.
    :return: True or False.
    """
    stop_codon_found = False
    stop_codons = ["tga", "tag", "taa"]
    for i in range(frame, len(dna), 3):
        codon = dna[i:i+3].lower()
        if codon in stop_codons:
            stop_codon_found = True
            break
    return stop_codon_found


def reverse_string(seq):
    """
    :param seq: Dna sequence.
    :return: Invert dna sequence.
    """
    return seq[::-1]


def complement(dna):
    """
    :param dna: Dna sequence.
    :return: Return the complementary sequence string.
    """
    base_complement = {"A": "T", "C": "G", "G": "C", "T": "A",
                       "N": "N", "a": "t", "c": "g", "g": "c", "t": "a", "n": "n"}
    letters = list(dna)
    for i, b in enumerate(letters):
        letters[i] = base_complement[b]
    return "".join(letters)


dna_sequence = "atgagcgggccggct"

print(has_stop_codon(dna_sequence, 1))

inverted_seq = reverse_string(dna_sequence)
print(inverted_seq)

seq_inverted_complement = complement(inverted_seq)
print(seq_inverted_complement)
