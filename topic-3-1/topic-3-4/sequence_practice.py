scores = [72, 85, 91, 68, 88]

title = "weekly score report"

print(scores[0])

print(scores[2])

print(scores[-1])

scores[1] = 86

print(scores)

scores.append(93)

print(scores)

first_word = title[0:6]

last_word = title[13:18]

print(first_word)

print(last_word)

label = last_word + ": " + str(len(scores))

print(label)

print("Scores:", scores)

