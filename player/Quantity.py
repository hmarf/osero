import pickle

class Quantity:
    def __init__(self, alpha, gamma, filename, initial_q = 1):
        self._initial_q = initial_q
        self._values = {}
        if filename == 'no':
            self._values = {}
        else:
            with open(filename,mode='rb') as f:
                self._values = pickle.load(f)
        #print(self._values)
        self._alpha = alpha
        self._gamma = gamma
        self.count = 0

    def get(self, state, act):
        if self._values.get((state, act)) is None:
            # self._values[(state, act)] = self._initial_q
            return self._initial_q
        return self._values.get((state, act))

    def set(self, s, a, q_value):
        self._values[s, a] = q_value

    def update(self, s, a, r, max_q):
        pQ = self.get(s, a)
        new_q = pQ + self._alpha * ((r + self._gamma * max_q) - pQ)
        self.set(s, a, new_q)

    def save(self,filename):
        with open(filename,mode='wb') as f:
            pickle.dump(self._values,f)

    # def load(self,filename):
    #     with open(filename,mode='rb') as f:
    #         self._values = pickle.load(f)
    #         print(self._values)

    def return_value(self):
        return self._values