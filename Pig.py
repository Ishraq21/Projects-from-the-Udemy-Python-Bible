# Get sentence from user

original = input("Put your sentence here: ").strip().lower()

# split sentence into words

words = original.split()


# loop through the words and convert to pig latin

new_words=[]

for word in words:
   if word[0] in "aeiou":
       new_word= word + "yay"
       new_words.append(new_word)
   else:
       vowel_pos = 0
       for letter in word:
           if letter not in "aeiou":
               vowel_pos = vowel_pos + 1
           else:
               break
       consonents = word[:vowel_pos]
       the_rest = word[vowel_pos:]
       new_word = the_rest +consonents + "ay"
       new_words.append(new_word)



#if it statrts with vowel, just add "yay"

#Otherwise, move the first consonant closer to end, and add "ay"

# stick words back together

output=" ".join(new_words)

# output the final string

print(output)
