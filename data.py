import string
import pathlib

import pandas as pd

WORD_LEN = 5
ALPHABET = list(string.ascii_lowercase)
CWD = pathlib.Path(__file__).parent.resolve()
DATA_PATH = CWD.joinpath("data")

if not DATA_PATH.is_dir():
    DATA_PATH.mkdir()

letter_counts_total = {}
letter_counts_position = {}
times_present = {}

words = []

print("Reading words...")
with open("sgb.txt", "r") as sgb:
    words.extend(sgb.read().splitlines())
    for word in words:
        for i, letter in enumerate(word):
            if letter not in letter_counts_total:
                letter_counts_total[letter] = [0]
            letter_counts_total[letter][0] += 1
            if letter not in letter_counts_position:
                letter_counts_position[letter] = [0] * WORD_LEN
            letter_counts_position[letter][i] += 1
        for c in ALPHABET:
            if c in word:
                if c not in times_present:
                    times_present[c] = [0]
                times_present[c][0] += 1

def save_csv(data_dict, name):
    pd.DataFrame(data_dict).to_csv(DATA_PATH.joinpath(name), index=False)

def has_unique_letters(word):
    return len(word) == len(set(word))

def query_uniques(letters, save=True):
    res = []
    letters = letters.lower();
    for word in words:
        if has_unique_letters(word) and all([l in letters for l in word]):
            res.append(word)
    if save:
        print("Saving data...")
        save_csv(res, f"uniques_of_{letters}.csv")
        print(f"Saved data to {DATA_PATH}")
    else:
        for word in res:
            print(word)

def query_uniques_pos(letters, save=True):
    assert len(letters) == WORD_LEN

    res = []
    letters = letters.lower();
    for word in words:
        if has_unique_letters(word) and all([word[i] in letters[i] for i in range(WORD_LEN)]):
            res.append(word)
    if save:
        print("Saving data...")
        save_csv(res, f"uniques_of_{letters}.csv")
        print(f"Saved data to {DATA_PATH}")
    else:
        for word in res:
            print(word)

if __name__ == '__main__':
    print("Saving data...")
    save_csv(letter_counts_total, "letter_counts_total.csv")
    save_csv(letter_counts_position, "letter_counts_position.csv")
    save_csv(times_present, "times_present.csv")
    print(f"Saved data to {DATA_PATH}")