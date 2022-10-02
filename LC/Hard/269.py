class Solution:
    def alienOrder(self, words: List[str]) -> str:
        sorted_language = ""
        
        adjacency_list = defaultdict(list)
        in_degrees = {c : 0 for word in words for c in word}
        
        for w1, w2 in zip(words, words[1:]):
            for parent, child in zip(w1, w2):
                if parent != child:
                    adjacency_list[parent].append(child)
                    in_degrees[child] += 1
                    break
            else:
                if len(w2) < len(w1): return ""
                
        sources = [k for k in in_degrees if in_degrees[k] == 0]
        
        while sources:
            letter = sources.pop(0)
            sorted_language += letter
            
            for child in adjacency_list[letter]:
                in_degrees[child] -= 1
                
                if in_degrees[child] == 0:
                    sources.append(child)
                    
        return sorted_language if len(in_degrees) == len(sorted_language) else ""