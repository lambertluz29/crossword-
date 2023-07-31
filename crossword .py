import sys

suffix = sys.argv[1] if len(sys.argv) > 1 else input("Enter suffix: ")

suffix = suffix.strip().lower()
suffixLength = len(suffix)

if suffixLength == 0:
    sys.exit()

with open("XwiJeffChenList.txt") as f:
    lines = f.readlines()

count = 0
fullWordList = []

for line in lines:
    line = line.lower().strip()
    parts = line.split(';')
    fullWord = parts[0]
    fullWordList.append(fullWord)  # All words get added to list

    # if the word ends with our suffix, see if the word without the suffix is already in the list.
    # Note, this assumes words in alphabetical order, eg, PASS would precede PASSION in the list.

    if fullWord.endswith(suffix):
        truncatedWord = fullWord[: -suffixLength]

        if truncatedWord in fullWordList:
            print(truncatedWord + ":" + fullWord)
            count += 1

print(f'{count} found')