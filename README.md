# wordle-bot

Automated [Wordle](https://www.powerlanguage.co.uk/wordle/) player that does not use Wordle source in any way. Uses a modified version of [The Stanford GraphBase's](https://www-cs-faculty.stanford.edu/~knuth/sgb.html) list of 5-letter words. Words are removed from `sgb.txt` on the fly as invalid words are discovered.

Must be using Python 3.8 or later. To get started, run
```
python bot.py
```

## Statistics of current hyperparameters

**Average number of guesses used: 3.8**

### Guess Frequencies
|Guesses Used|Frequency|
|---------|---------|
|1|0|
|2|0|
|3|17|
|4|16|
|5|5|
|6|2|

### Game History
|Day|Guesses Used|Solved?|
|----------------------|-----|---|
| Day 221 - 01/26/2022 | 4/6 | ✅ |
| Day 220 - 01/25/2022 | 3/6 | ✅ |
| Day 219 - 01/24/2022 | 4/6 | ✅ |
| Day 218 - 01/23/2022 | 5/6 | ✅ |
| Day 217 - 01/22/2022 | 3/6 | ✅ |
| Day 216 - 01/21/2022 | 6/6 | ✅ |
| Day 215 - 01/20/2022 | 4/6 | ✅ |
| Day 214 - 01/19/2022 | 4/6 | ✅ |
| Day 213 - 01/18/2022 | 4/6 | ✅ |
| Day 212 - 01/17/2022 | 3/6 | ✅ |
| Day 211 - 01/16/2022 | 3/6 | ✅ |
| Day 210 - 01/15/2022 | 4/6 | ✅ |
| Day 209 - 01/14/2022 | 3/6 | ✅ |
| Day 208 - 01/13/2022 | 3/6 | ✅ |
| Day 207 - 01/12/2022 | 4/6 | ✅ |
| Day 206 - 01/11/2022 | 4/6 | ✅ |
| Day 205 - 01/10/2022 | 4/6 | ✅ |
| Day 204 - 01/09/2022 | 3/6 | ✅ |
| Day 203 - 01/08/2022 | 4/6 | ✅ |
| Day 202 - 01/07/2022 | 4/6 | ✅ |
| Day 201 - 01/06/2022 | 3/6 | ✅ |
| Day 200 - 01/05/2022 | 3/6 | ✅ |
| Day 199 - 01/04/2022 | 3/6 | ✅ |
| Day 198 - 01/03/2022 | 3/6 | ✅ |
| Day 197 - 01/02/2022 | 4/6 | ✅ |
| Day 196 - 01/01/2022 | 5/6 | ✅ |
| Day 195 - 12/31/2021 | 3/6 | ✅ |
| Day 194 - 12/30/2021 | 4/6 | ✅ |
| Day 193 - 12/29/2021 | 3/6 | ✅ |
| Day 192 - 12/28/2021 | 3/6 | ✅ |
| Day 191 - 12/27/2021 | 5/6 | ✅ |
| Day 190 - 12/26/2021 | 4/6 | ✅ |
| Day 189 - 12/25/2021 | 5/6 | ✅ |
| Day 188 - 12/24/2021 | 5/6 | ✅ |
| Day 187 - 12/23/2021 | 3/6 | ✅ |
| Day 186 - 12/22/2021 | 6/6 | ✅ |
| Day 185 - 12/21/2021 | 4/6 | ✅ |
| Day 184 - 12/20/2021 | 3/6 | ✅ |
| Day 183 - 12/19/2021 | 3/6 | ✅ |
| Day 182 - 12/18/2021 | 4/6 | ✅ |