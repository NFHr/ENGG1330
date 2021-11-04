import Q4R
import sys

class Logger(object):
    def __init__(self, filename='default.log', stream=sys.stdout):
	    self.terminal = stream
	    self.log = open(filename, 'a')

    def write(self, message):
	    self.terminal.write(message)
	    self.log.write(message)

    def flush(self):
	    pass

sys.stdout = Logger('default.log', sys.stdout)

P, var = 0, 1000
for i in range(var):
    if Q4R.main() == 1:
        P += 1
    else:
        print('ERROR')

print(f'Player1 wins: {P, round(P/var, 3)}, Player2 wins: {var - P, round((var - P)/var,3)}')