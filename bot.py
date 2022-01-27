import string

WORD_LEN = 5
EXPLORATION_PUNISHMENT = 0.000001
ALPHABET = list(string.ascii_lowercase)
EXPLOIT_THRESHOLD = 0.006
DECAY = 0.1

def main():
    with open("sgb.txt", "r") as words:
        allowed_guesses = words.read().splitlines()

    possibles = []
    for i in range(WORD_LEN):
        possibles.append(set(ALPHABET))

    turn = 1
    guess = ""
    threshold = EXPLOIT_THRESHOLD


    exists = set()
    not_exists = set()
    explored = set()

    print("Inputs are CASE-INSENSITIVE")
    print()

    while True:
        guess_explore, guess_explore_score, guess_exploit, guess_exploit_prob = make_guesses(allowed_guesses, possibles, exists, not_exists, explored)

        if guess_exploit_prob >= EXPLOIT_THRESHOLD:
            guess = guess_exploit
            print(f"Exploiting on turn {turn} with p = {guess_exploit_prob}.", end=" ")
        else:
            guess = guess_explore
            print(f"Exploring on turn {turn}.", end=" ")
        print(f"Guess: {guess.upper()}")

        if guess_exploit_prob < 1:
            while ((colors := input("COLORS (G/Y/B): ").lower()) and not valid_colors(colors)):
                pass
        else:
            colors = "g" * WORD_LEN

        if colors == "g" * WORD_LEN:
            print()
            print(f"WON on turn {turn} with {guess.upper()}")
            print()
            break

        update_info(guess, colors, possibles, exists, not_exists, explored)

        turn += 1
        threshold = threshold * DECAY
        print()

def valid_colors(colors):
    if len(colors) != WORD_LEN:
        return False
    for letter in colors:
        if letter != "g" and letter != "y" and letter != "b":
            return False
    return True

def make_guesses(words, possibles, exists, not_exists, explored):
    letter_probs = {}
    position_probs = [{} for _ in range(WORD_LEN)]
    
    build_probs(words, possibles, exists, not_exists, letter_probs, position_probs)

    return best_words(words, possibles, exists, not_exists, explored, letter_probs, position_probs)

def can_explore(word, not_exists):
    for c in word:
        if c in not_exists:
            return False
    return True

def matches(word, possibles, exists):
    remaining = set(exists)
    for i, letter in enumerate(word):
        if letter not in possibles[i]:
            return False
        remaining.discard(letter)
    return len(remaining) == 0

def build_probs(words, possibles, exists, not_exists, letter_probs, position_probs):
    total_letters = 0
    position_totals = [0 for _ in range(WORD_LEN)]

    for word in words:
        if can_explore(word, not_exists):
            for i in range(WORD_LEN):
                letter_probs[word[i]] = letter_probs.get(word[i], 0) + 1
                total_letters += 1
        if matches(word, possibles, exists):
            for i in range(WORD_LEN):
                position_probs[i][word[i]] = position_probs[i].get(word[i], 0) + 1
                position_totals[i] += 1

    for letter in ALPHABET:
        letter_probs[letter] = letter_probs.get(letter, 0) / total_letters
        for i in range(WORD_LEN):
            position_probs[i][letter] = position_probs[i].get(letter, 0) / position_totals[i]

def word_score_explore(word, letter_probs, explored, possibles):
    res = 1
    seen = set()
    for i, c in enumerate(word):
        res = res * letter_probs[c]

        if c in explored:
            res = res * EXPLORATION_PUNISHMENT
        if c in seen:
            res = res * EXPLORATION_PUNISHMENT

        seen.add(c)
    return res

def word_prob(word, position_probs):
    res = 1
    for i in range(WORD_LEN):
        res = res * position_probs[i][word[i]]
    return res

def best_words(words, possibles, exists, not_exists, explored, letter_probs, position_probs):
    res_explore = ""
    res_prob = ""
    max_explore_score = -1
    max_prob = -1
    for word in words:
        if can_explore(word, not_exists):
            explore_score = word_score_explore(word, letter_probs, explored, possibles)
            if explore_score > max_explore_score or (explore_score == max_explore_score and word_prob(word, position_probs) > word_prob(res_explore, position_probs)):
                res_explore = word
                max_explore_score = explore_score

        if matches(word, possibles, exists):
            prob = word_prob(word, position_probs)
            if prob > max_prob:
                res_prob = word
                max_prob = prob
    return res_explore, max_explore_score, res_prob, max_prob

def update_info(guess, colors, possibles, exists, not_exists, explored):
    for i in range(WORD_LEN):
        letter, color = guess[i], colors[i]
        explored.add(letter)

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
                not_exists.add(letter)
                for j in range(WORD_LEN):
                    possibles[j].discard(letter)

if __name__ == "__main__":
    main()