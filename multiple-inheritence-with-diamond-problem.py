class Tokenizer:
    """Tokenize text"""
    def __init__(self, text):
        print('Start Tokenizer.__init__()')
        self.tokens = text.split()
        print('End Tokenizer.__init__()')


class WordCounter(Tokenizer):
    """Count words in text"""
    def __init__(self, text):
        print('Start init WordCounter.__init__()')
        super().__init__(text)
        self.word_count = len(self.tokens)
        print('End WordCounter.__init__()')
    
    def util(self):
        print("superb i am in WordCounter util function")


class Vocabulary(Tokenizer):
    """Find unique words in text"""
    def __init__(self, text):
        print('Start init Vocabulary.__init__()')
        super().__init__(text)
        self.vocab = set(self.tokens)
        print('End init Vocabulary.__init__()')
    
    def util(self):
        print("superb i am in vocabulary util function")


class TextDescriber(Vocabulary, WordCounter):
    """Describe text with multiple metrics"""
    def __init__(self, text):
        print('Start init TextDescriber.__init__()')
        super().__init__(text)
        print('End init TextDescriber.__init__()')


td = TextDescriber('row row row your boat')
td.util()


