sequence = "dbbaCEDbdAacCEAadcB"

unique_values = set(sequence)

# Create a dictionary with all unique characters.
# Assign a default value of 0 for each char.
scores = {value.lower(): 0 for key, value in enumerate(unique_values)}

for char in sequence:
    index = char.lower()
    if char.isupper():
        scores[index] -= 1
    else:
        scores[index] += 1

result = []
for i in sorted(scores, key=scores.get, reverse=True):
    result.append("{0}:{1}".format(i, scores[i]))

print(', '.join(result))
