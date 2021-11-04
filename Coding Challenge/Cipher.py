mode = input('Mode: ')
text = input('Text: ')
to_cipher = {'a':'c', 'b':'g', 'c':'i', 'd':'n', 'e':'e', 'f':'l', 'g':'o', 'h':'s', 'i':'u', 'j:':'r', 'k':'y', 'l':'h', 'm':'p',
            'n':'v', 'o':'a', 'p':'b', 'q':'z', 'r':'j', 's':'k', 't':'x', 'u':'d', 'v':'t', 'w':'f', 'x':'w', 'y':'m', 'z':'q'}

to_plain = {'c':'a', 'g':'b', 'i':'c', 'n':'d', 'e':'e', 'l':'f', 'o':'g', 's':'h', 'u':'i', 'r':'j:', 'y':'k','h':'l', 'p':'m', 
            'v':'n', 'a':'o', 'b':'p', 'z':'q', 'j':'r', 'k':'s', 'x':'t', 'd':'u', 't':'v', 'f':'w', 'w':'x', 'm':'y', 'q':'z'}