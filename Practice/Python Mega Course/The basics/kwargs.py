def find_winner(**kwargs):
    return max(kwargs, key=kwargs.get)

print(find_winner(ANdy = 17, Marry = 19, Sim = 45, Kae = 34))