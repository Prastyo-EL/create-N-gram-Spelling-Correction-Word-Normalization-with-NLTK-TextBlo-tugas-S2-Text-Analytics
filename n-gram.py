# import library
from nltk import ngrams
from textblob import TextBlob

# import file txt
g=open("original.txt",'r+')
# baca file
fi=g.read()
# jumlah generate n-gram pada corpus digunakan 3
n = 3
threegrams = ngrams(fi.split(), n)

for grams in threegrams:
  print (grams)


# text original
print("original text : ",(fi))
b=TextBlob(fi)
# hasil koreksi ejaan dan normalisasi dengan textblob
print("corrected text : ",str(b.correct()))
# output hasil koreksi
d=open("corrected.txt","w")
d.write(str(b.correct()))
d.close()