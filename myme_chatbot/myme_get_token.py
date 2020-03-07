from janome.tokenizer import Tokenizer

class Token:
    def __init__(self):
        self.token = Tokenizer()

    def get_token(self, txt='何かテキストを入力してください'):
        return self.token.tokenize(txt)

if '__main__' == __name__:
    t = Token()
    for _ in t.get_token():
        print(_)