class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, s: str) -> None:
        curr = self.root
        for c in s:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr["**"] = {}


    def check_prefix(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]
        return True    


    def search(self, s: str) -> bool:
        curr = self.root
        for c in s:
            if c not in curr:
                return False
            curr = curr[c]
        return "**" in curr


    def delete(self, s: str) -> bool:
        stack = []
        curr = self.root
        for c in s:
            if c not in curr:
                return False
            stack.append((curr, c))
            curr = curr[c]
        
        # Check if s is inside trie
        if "**" not in curr:
            return False
        
        del curr["**"]
        
        # Delete as much as possible
        while stack:
            parent, c = stack.pop()
            child = parent[c]
            if child:  # Check if child has any children
                break
            del parent[c]  # Cut off child
        return True