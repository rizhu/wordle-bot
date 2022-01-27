import string

WORD_LEN = 5
ALPHABET = list(string.ascii_lowercase)

def main():
    with open("words.txt", "r") as words:
        sgb = words.read().splitlines()

    possibles = []
    for i in range(WORD_LEN):
        possibles.append(set(ALPHABET))

    turn = 1
    guess = ""
    exists = set()

    while turn < 7:
        global_probs = {}
        local_probs = [{} for _ in range(WORD_LEN)]
        
        build_probs(sgb, possibles, global_probs, local_probs)
        guess_global, guess_global_prob, guess_local, guess_local_prob = best_words(sgb, possibles, global_probs, local_probs)

        print(f"Guesses for turn {turn}")
        print(f"Best global guess: {guess_global.upper()} with p = {guess_global_prob}")
        print(f"Best local guess: {guess_local.upper()} with p = {guess_local_prob}")

        if guess_local_prob < 1:
            guess = input("GUESS: ").lower()
            colors = input("COLORS (G/Y/B): ").lower()
        else:
            guess = guess_local
            colors = "g" * WORD_LEN

        if colors == "g" * WORD_LEN:
            print(f"Won on turn {turn} with {guess_local.upper()}")
            break

        adjust_possibles(guess, colors, possibles, exists)

        turn += 1


def matches(word, possibles):
    for i in range(WORD_LEN):
        if word[i] not in possibles[i]:
            return False
    return True

def build_probs(words, possibles, global_probs, local_probs):
    global_total = 0
    local_totals = [0 for _ in range(WORD_LEN)]

    for word in words:
        if matches(word, possibles):
            for i in range(WORD_LEN):
                global_probs[word[i]] = global_probs.get(word[i], 0) + 1
                global_total += 1

                local_probs[i][word[i]] = local_probs[i].get(word[i], 0) + 1
                local_totals[i] += 1

    for letter in ALPHABET:
        global_probs[letter] = global_probs.get(letter, 0) / global_total
        for i in range(WORD_LEN):
            local_probs[i][letter] = local_probs[i].get(letter, 0) / local_totals[i]

def word_prob_global(word, global_probs):
    res = 1
    seen = set()
    for c in word:
        if c in seen:
            return 0
        else:
            seen.add(c)
        res = res * global_probs[c]
    return res

def word_prob_local(word, local_probs):
    res = 1
    for i in range(WORD_LEN):
        res = res * local_probs[i][word[i]]
    return res

def best_words(words, possibles, global_probs, local_probs):
    res_global = ""
    res_local = ""
    max_prob_global = 0
    max_prob_local = 0
    for word in words:
        if matches(word, possibles):
            prob = word_prob_global(word, global_probs)
            if prob > max_prob_global:
                res_global = word
                max_prob_global = prob

            prob = word_prob_local(word, local_probs)
            if prob > max_prob_local:
                res_local = word
                max_prob_local = prob
    return res_global, max_prob_global, res_local, max_prob_local

def adjust_possibles(guess, colors, possibles, exists):
    for i in range(WORD_LEN):
        letter, color = guess[i], colors[i]

        if color == "g":
            possibles[i] = set([letter])
            exists.add(letter)
        elif color == "y":
            possibles[i].discard(letter)
            exists.add(letter)
        elif color == "b":
            if letter in exists:
                possibles[i].discard(letter)
            else:
                for j in range(WORD_LEN):
                    possibles[j].discard(letter)

if __name__ == "__main__":
    main()