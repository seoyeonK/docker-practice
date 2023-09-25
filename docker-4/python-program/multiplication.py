import os

dan = os.environ.get('DAN')

if dan is not None:
    dan = int(dan)
    for i in range(1, 10):
        print(dan," x ",i, " = ", dan * i )
    
else:
    for i in range(2, 10):
        for j in range(1,10):
            print(i," x ",j, " = ", i * j )

