# little complex brute force

wrod_to_find = "ram"

alphabet = "abcdefgnijklmnopqrstuvwxyt"

for i in alphabet:
    for j in alphabet:
        for k in alphabet:
            combined = i+j+k
            if combined == wrod_to_find:
                print(f"found word {combined}")
                break
                