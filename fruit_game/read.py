import pickle
f=open('highscore.txt','rb')
s=pickle.load(f)
print(s)