# wordle-bot

Automated [Wordle](https://www.powerlanguage.co.uk/wordle/) bot that does not use Wordle page source (e.g. the future solutions list and allowed guesses list found on the Wordle site) in any way. Uses a modified version of [The Stanford GraphBase's](https://www-cs-faculty.stanford.edu/~knuth/sgb.html) list of 5-letter words. Words are removed from `sgb.txt` on the fly as invalid words are discovered.

## Description

`wordle-bot` essentially plays using Bayesian inference, generating 2 guesses for each row: one that it deems optimal for gathering information about the search space (exploration) and one that it deems optimal for getting the right answer given the all the information it knows (exploitation). `wordle-bot` does not perform any kind of tree searching.

The exploration guess is generated by assigning a score to each valid word in the search space and higher scores are given to words that contain more frequently-occurring letters. Additionally, words that contain repetitive, nonnovel information are punished according to a hyperparameter. The exploitation guess is generated by maximizing the probability over all valid guesses of each letter being in its position given all previously seen information.

If the exploitation guess's probability is larger than a theshold, then `wordle-bot` uses it as its guess for the current row and otherwise, it uses the exploration guess. The threshold decays on every subsequent row in an exponential fashion and the initial threshold and the rate of decay are hyperparameters.

## Usage

Must be using Python 3.8 or later. To get started, run
```
python bot.py
```

## Statistics of current hyperparameters

**Average number of guesses used: 3.918699187**

### Guess Frequencies
|Guesses Used|Frequency|
|---------|---------|
|1|0|
|2|3|
|3|36|
|4|51|
|5|21|
|6|7|

### Game History
**Day**|**Guesses Used**|**Solved?**
:-----:|:-----:|:-----:
Day 221 - 01/26/2022|5|✅
Day 220 - 01/25/2022|3|✅
Day 219 - 01/24/2022|4|✅
Day 218 - 01/23/2022|5|✅
Day 217 - 01/22/2022|3|✅
Day 216 - 01/21/2022|6|✅
Day 215 - 01/20/2022|4|✅
Day 214 - 01/19/2022|4|✅
Day 213 - 01/18/2022|4|✅
Day 212 - 01/17/2022|2|✅
Day 211 - 01/16/2022|2|✅
Day 210 - 01/15/2022|4|✅
Day 209 - 01/14/2022|3|✅
Day 208 - 01/13/2022|4|✅
Day 207 - 01/12/2022|5|✅
Day 206 - 01/11/2022|4|✅
Day 205 - 01/10/2022|5|✅
Day 204 - 01/09/2022|3|✅
Day 203 - 01/08/2022|4|✅
Day 202 - 01/07/2022|4|✅
Day 201 - 01/06/2022|3|✅
Day 200 - 01/05/2022|3|✅
Day 199 - 01/04/2022|3|✅
Day 198 - 01/03/2022|4|✅
Day 197 - 01/02/2022|3|✅
Day 196 - 01/01/2022|4|✅
Day 195 - 12/31/2021|3|✅
Day 194 - 12/30/2021|4|✅
Day 193 - 12/29/2021|3|✅
Day 192 - 12/28/2021|3|✅
Day 191 - 12/27/2021|3|✅
Day 190 - 12/26/2021|4|✅
Day 189 - 12/25/2021|5|✅
Day 188 - 12/24/2021|5|✅
Day 187 - 12/23/2021|4|✅
Day 186 - 12/22/2021|6|✅
Day 185 - 12/21/2021|4|✅
Day 184 - 12/20/2021|3|✅
Day 183 - 12/19/2021|3|✅
Day 182 - 12/18/2021|4|✅
Day 181 - 12/17/2021|4|✅
Day 180 - 12/16/2021|3|✅
Day 179 - 12/15/2021|3|✅
Day 178 - 12/14/2021|4|✅
Day 177 - 12/13/2021|4|✅
Day 176 - 12/12/2021|3|✅
Day 175 - 12/11/2021|3|✅
Day 174 - 12/10/2021|5|✅
Day 173 - 12/09/2021|3|✅
Day 172 - 12/08/2021|3|✅
Day 171 - 12/07/2021|4|✅
Day 170 - 12/06/2021|4|✅
Day 169 - 12/05/2021|4|✅
Day 168 - 12/04/2021|3|✅
Day 167 - 12/03/2021|5|✅
Day 166 - 12/02/2021|5|✅
Day 165 - 12/01/2021|3|✅
Day 164 - 11/30/2021|4|✅
Day 163 - 11/29/2021|4|✅
Day 162 - 11/28/2021|5|✅
Day 161 - 11/27/2021|4|✅
Day 160 - 11/26/2021|5|✅
Day 159 - 11/25/2021|6|✅
Day 158 - 11/24/2021|4|✅
Day 157 - 11/23/2021|5|✅
Day 156 - 11/22/2021|3|✅
Day 155 - 11/21/2021|3|✅
Day 154 - 11/20/2021|2|✅
Day 153 - 11/19/2021|4|✅
Day 152 - 11/18/2021|4|✅
Day 151 - 11/17/2021|3|✅
Day 150 - 11/16/2021|6|✅
Day 149 - 11/15/2021|4|✅
Day 148 - 11/14/2021|3|✅
Day 147 - 11/13/2021|6|✕
Day 146 - 11/12/2021|4|✅
Day 145 - 11/11/2021|3|✅
Day 144 - 11/10/2021|4|✅
Day 143 - 11/09/2021|6|✅
Day 142 - 11/08/2021|3|✅
Day 141 - 11/07/2021|5|✅
Day 140 - 11/06/2021|3|✅
Day 139 - 11/05/2021|3|✅
Day 138 - 11/04/2021|5|✅
Day 137 - 11/03/2021|3|✅
Day 136 - 11/02/2021|5|✅
Day 135 - 11/01/2021|5|✅
Day 134 - 10/31/2021|4|✅
Day 133 - 10/30/2021|4|✅
Day 132 - 10/29/2021|4|✅
Day 131 - 10/28/2021|4|✅
Day 130 - 10/27/2021|4|✅
Day 129 - 10/26/2021|5|✅
Day 128 - 10/25/2021|5|✅
Day 127 - 10/24/2021|5|✅
Day 126 - 10/23/2021|4|✅
Day 125 - 10/22/2021|3|✅
Day 124 - 10/21/2021|4|✅
Day 123 - 10/20/2021|6|✅
Day 122 - 10/19/2021|4|✅
Day 121 - 10/18/2021|4|✅
Day 120 - 10/17/2021|4|✅
Day 119 - 10/16/2021|4|✅
Day 118 - 10/15/2021|4|✅
Day 117 - 10/14/2021|4|✅
Day 116 - 10/13/2021|3|✅
Day 115 - 10/12/2021|4|✅
Day 114 - 10/11/2021|5|✅
Day 113 - 10/10/2021|5|✅
Day 112 - 10/09/2021|4|✅
Day 111 - 10/08/2021|4|✅
Day 110 - 10/07/2021|3|✅
Day 109 - 10/06/2021|5|✅
Day 108 - 10/05/2021|4|✅
Day 107 - 10/04/2021|3|✅
Day 106 - 10/03/2021|4|✅
Day 105 - 10/02/2021|3|✅
Day 104 - 10/01/2021|3|✅
Day 103 - 09/30/2021|5|✅
Day 102 - 09/29/2021|4|✅
Day 101 - 09/28/2021|4|✅
Day 100 - 09/27/2021|4|✅
