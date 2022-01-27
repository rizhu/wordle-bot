# wordle-bot

Automated [Wordle](https://www.powerlanguage.co.uk/wordle/) player that does not use Wordle source in any way. Uses a modified version of [The Stanford GraphBase's](https://www-cs-faculty.stanford.edu/~knuth/sgb.html) list of 5-letter words. Words are removed from `sgb.txt` on the fly as invalid words are discovered.

Must be using Python 3.8 or later. To get started, run
```
python bot.py
```