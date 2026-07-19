"""Finite audit for the weighted high-distortion RD amalgam."""

from heapq import heappop, heappush


Word = tuple[tuple[int, int], ...]


def ell0(a: int) -> int:
    """The binary weighted length sum 2^n."""
    return a


def ell1(a: int) -> int:
    """The heavy weighted length sum 2^(2^n)."""
    total = 0
    n = 0
    while a:
        if a & 1:
            total += 1 << (1 << n)
        a >>= 1
        n += 1
    return total


def multiply_syllable(word: Word, factor: int, value: int) -> Word:
    """Right multiply a reduced C_2*C_3 word by one cyclic syllable."""
    value %= factor
    if value == 0:
        return word
    if word and word[-1][0] == factor:
        combined = (word[-1][1] + value) % factor
        if combined == 0:
            return word[:-1]
        return word[:-1] + ((factor, combined),)
    return word + ((factor, value),)


def all_reduced_words(max_length: int) -> set[Word]:
    words: set[Word] = {()}
    tokens = ((2, 1), (3, 1), (3, 2))
    changed = True
    while changed:
        changed = False
        for word in tuple(words):
            for factor, value in tokens:
                new_word = multiply_syllable(word, factor, value)
                if len(new_word) <= max_length and new_word not in words:
                    words.add(new_word)
                    changed = True
    return words


def check_weighted_lengths() -> None:
    limit = 1 << 8
    for a in range(limit):
        for b in range(limit):
            assert ell0(a ^ b) <= ell0(a) + ell0(b)
            assert ell1(a ^ b) <= ell1(a) + ell1(b)

    for radius in range(limit):
        ball_size = sum(ell0(a) <= radius for a in range(limit))
        assert ball_size == radius + 1
        witness = radius
        if radius >= 1:
            assert ell1(witness) ** 2 > 2**radius
        assert ell1(witness) <= 2 ** (radius + 1)


def check_universal_length(bits: int = 3, bound: int = 7) -> None:
    """Dijkstra audit of L^U(a,q)=ell0(a)+|q| on a finite truncation."""
    a_values = range(1 << bits)
    moves: list[tuple[int, int, int, int]] = []

    # G=A x C_2 has the heavy A length.
    for a in a_values:
        for u in (0, 1):
            if a or u:
                moves.append((a, 2, u, ell1(a) + (u != 0)))

    # H=A x C_3 has the light A length.
    for a in a_values:
        for v in (0, 1, 2):
            if a or v:
                moves.append((a, 3, v, ell0(a) + (v != 0)))

    start = (0, ())
    distance: dict[tuple[int, Word], int] = {start: 0}
    queue: list[tuple[int, int, Word]] = [(0, 0, ())]
    while queue:
        current, a, word = heappop(queue)
        if distance[(a, word)] != current:
            continue
        for move_a, factor, value, cost in moves:
            new_a = a ^ move_a
            new_word = multiply_syllable(word, factor, value)
            new_distance = current + cost
            state = (new_a, new_word)
            if new_distance <= bound and new_distance < distance.get(state, bound + 1):
                distance[state] = new_distance
                heappush(queue, (new_distance, new_a, new_word))

    words = all_reduced_words(bound)
    for a in a_values:
        for word in words:
            formula = ell0(a) + len(word)
            if formula <= bound:
                assert distance[(a, word)] == formula
    for (a, word), value in distance.items():
        assert value == ell0(a) + len(word)


def main() -> None:
    check_weighted_lengths()
    check_universal_length()
    print("weighted high-distortion RD amalgam audit: PASS")


if __name__ == "__main__":
    main()
