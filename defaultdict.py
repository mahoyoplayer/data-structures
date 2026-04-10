class DefaultDict:
    def __init__(self, f: callable):
        self.key_val = {}
        self.default_factory = f

    def __getitem__(self, key):
        if key not in self.key_val:
            self.key_val[key] = self.default_factory()
        return self.key_val[key]
    
    def __setitem__(self, key, val):
        self.key_val[key] = val

    def __iter__(self):
        return iter(self.key_val)
    
    def items(self):
        return self.key_val.items()

freq = DefaultDict(int)
s = "abbccc122333"
for c in s:
    freq[c] += 1

for c, f in freq.items():
    print(f"Char: {c}, Freq: {f}")

