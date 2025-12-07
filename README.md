
# 📜 Vowel/Consonant Markov Chain Analyzer

This project performs a **First-Order Markov Chain analysis** on a text corpus to study the statistical patterns of **Vowel** (V) and **Consonant** (C) sequences. The goal is to gain insights into the phonetic and syllabic structure of the language in the analyzed text.

## ⚙️ How It Works: Code Breakdown

The script operates in three main phases: **Data Loading**, **Initial Probability Calculation**, and **Transition Probability Calculation**.

### 1. Data Loading and Setup

The script first defines the character sets and loads the text.

| Code Block | Description |
| :--- | :--- |
| `consonant = [c for c in string.ascii_lowercase if c not in vowels]` | Creates the definitive list of 21 English consonants by removing the five vowels from all 26 lowercase letters. |
| `corpus = [word.lower() for sen in data for word in sen.split()]` | Reads the entire book file, splits it into a list of words, and converts every word to **lowercase**. |


### 2. `vowels_and_consonent_count(corpus)`

This function calculates the **unconditional frequency** of Vowels and Consonants across the entire text.

| Line | Function Body Explanation |
| :--- | :--- |
| `for word in corpus:` | Iterates through every word in the loaded list. |
| `for i in range(len(char)):` | Iterates through every character within the current word. |
| `if char[i] in vowels:` | Checks if the character is one of the five defined vowels. If so, increments `vowels_count`. |
| `elif char[i] in consonant:` | **Crucially**, if the character is a consonant, it increments `consonant_count`. **Punctuation is ignored** as it fails both the `if` and `elif` checks, preventing it from skewing the total count (`total`). |

**Output:** The final lines calculate $\text{P}(\text{V}) = \frac{\text{Vowel Count}}{\text{Total Letters}}$ and $\text{P}(\text{C}) = \frac{\text{Consonant Count}}{\text{Total Letters}}$.


### 3. `markov1chainby(corpus)`

This function is the core of the Markov chain analysis. It calculates the raw **counts** of the four possible state transitions (or bigrams).

| Line | Function Body Explanation |
| :--- | :--- |
| `for i in range(len(word) - 1):` | Iterates through a word, stopping one character early to ensure `word[i+1]` is always valid. This allows checking adjacent pairs. |
| `if word[i] in vowels and word[i+1] in vowels:` | **Vowel $\rightarrow$ Vowel (VV):** Checks for two consecutive vowels (e.g., the 'eo' in 'leopard'). |
| `elif word[i] in vowels and word[i+1] in consonant:` | **Vowel $\rightarrow$ Consonant (VC):** Checks for a vowel followed by a consonant (the most common sequence, e.g., 'ca' in 'cat'). |
| `elif word[i] in consonant and word[i+1] in consonant:` | **Consonant $\rightarrow$ Consonant (CC):** Checks for two consecutive consonants (e.g., 'st' in 'stop'). |
| `elif word[i] in consonant and word[i+1] in vowels:` | **Consonant $\rightarrow$ Vowel (CV):** Checks for a consonant followed by a vowel (e.g., 'te' in 'test'). |

**Output:** The script then converts these raw counts into **conditional probabilities**:

$$\text{P}(\text{V} \rightarrow \text{C}) = \frac{\text{Count}(\text{VC})}{\text{Count}(\text{VV}) + \text{Count}(\text{VC})}$$


## ⚠️ Known Limitation: Punctuation Handling

The current methodology relies on processing word-by-word, but does not explicitly remove punctuation from the words.

* **Punctuation breaks the chain:** For a word like `"prince."`, the transition from the vowel `'e'` to the period `.` is **missed**, as the `if/elif` statements ignore the period.
* **Missing Inter-Word Transitions:** The model does not account for the transition between the last letter of one word and the first letter of the next word.

This limitation means the count of valid transitions ($\text{VV}$, $\text{VC}$, $\text{CC}$, $\text{CV}$) is slightly **understated**, but the calculated **probabilities** (the ratios) remain very accurate for the sequences that *do* occur within words.