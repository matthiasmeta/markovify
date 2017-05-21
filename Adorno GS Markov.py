import markovify

# Get raw text as string.
with open("C:\\Users\\Gamer\\Desktop\\Adorno GS.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)



# ein satz mit 140 zeichen maximum 
for i in range(3):
    print(text_model.make_short_sentence(140))
