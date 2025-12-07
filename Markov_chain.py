import string

consonant = list(string.ascii_lowercase)
vowels = ["a", "e", "i", "o", "u"]
consonant = [c for c in consonant if c not in vowels]


book_name = "Books/candide.txt"
with open(book_name, "r") as data:
    corpus = [word.lower() for sen in data for word in sen.split()] 


def vowels_and_consonent_count(corpus):
    vowels_count = 0
    consonant_count = 0

    for word in corpus:
        char = list(word)
        for i in range(len(char)):
            if char[i] in vowels:
                vowels_count += 1
            elif char[i] in consonant:
                consonant_count += 1

    return vowels_count, consonant_count

vowels_count, consonant_count = vowels_and_consonent_count(corpus=corpus)
print(f"Vowels Count: {vowels_count}")
print(f"Consonant Count: {consonant_count}")

total = vowels_count + consonant_count
vowels_prob = vowels_count / total
consonant_prob = consonant_count / total

print(f"Vowels Count Probability: {vowels_prob}")
print(f"Consonant Count Probability: {consonant_prob}")

print('-----------------------------------State---------------------------------------------')


def markov1chainby(corpus):
    vv = 0
    vc = 0
    cc = 0
    cv = 0
    for word in corpus:
        for i in range(len(word) - 1):
            if word[i] in vowels and word[i+1] in vowels:
                vv += 1
            elif word[i] in vowels and word[i+1] in consonant:
                vc += 1
            elif word[i] in consonant and word[i+1] in consonant:
                cc += 1
            elif word[i] in consonant and word[i+1] in vowels:
                cv += 1
            
    return vv, vc, cc, cv
                        
vv, vc, cc, cv = markov1chainby(corpus)
print(f"vv: {vv} | vc: {vc} | cc: {cc} | cv: {cv}")

vv_prob = vv / (vv + vc)
vc_prob = vc / (vv + vc)
cc_prob = cc / (cc + cv)
cv_prob = cv / (cc + cv)
print(f"vv_prob: {vv_prob} | vc_prob: {vc_prob} | cc_prob: {cc_prob} | cv_prob: {cv_prob}")
