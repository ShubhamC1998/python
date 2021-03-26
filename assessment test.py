#use for split(), and if to create a statement that will print out words that start with "s"
st = "Sam print only the words that start with s in this sentence"
for word in st.split():
    if word[0].lower()=="s"or word[0].upper()=="S":
        print(word)



# usr range () to print all the even numbers from 0 to 10
for x in range(0,10):
    if x%2==0:
        print(x)


