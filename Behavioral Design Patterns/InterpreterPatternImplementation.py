### Interpreter Design Pattern

### Scenario: Language Translator (Tamil to English)
# Base Expression Class
class Expression:
    def interpret(self):
        pass

# Subject Expression: Mapping Tamil subject to English subject
class SubjectExpression(Expression):
    subject_dict = {
        'நான்': 'I',
        'நீ': 'You',
        'அவன்': 'He',
        'அவள்': 'She',
        'நாம்': 'We'
    }
    
    def __init__(self, subject):
        self.subject = subject
    
    def interpret(self):
        return self.subject_dict.get(self.subject, self.subject)

# Verb Expression: Mapping Tamil verbs to English verbs
class VerbExpression(Expression):
    verb_dict = {
        'போக': 'go',
        'செய்': 'do',
        'சாப்பிடு': 'eat',
        'பிடி': 'catch',
        'காண்': 'see'
    }
    
    def __init__(self, verb):
        self.verb = verb
    
    def interpret(self):
        return self.verb_dict.get(self.verb, self.verb)

# Object Expression: Mapping Tamil objects to English objects
class ObjectExpression(Expression):
    object_dict = {
        'பழம்': 'fruit',
        'நூல்': 'book',
        'பாய்': 'dog',
        'பட்டம்': 'cat'
    }
    
    def __init__(self, obj):
        self.obj = obj
    
    def interpret(self):
        return self.object_dict.get(self.obj, self.obj)

# Sentence Expression: Constructing the complete sentence
class SentenceExpression(Expression):
    def __init__(self, subject, verb, obj):
        self.subject = subject
        self.verb = verb
        self.obj = obj
    
    def interpret(self):
        subject = self.subject.interpret()
        verb = self.verb.interpret()
        obj = self.obj.interpret()
        return f"{subject} {verb} {obj}"

# Function to parse the Tamil sentence and return an interpreted expression
def parse_tamil_sentence(sentence):
    words = sentence.split()
    
    # Assume the structure is: Subject Verb Object
    subject = SubjectExpression(words[0])
    verb = VerbExpression(words[1])
    obj = ObjectExpression(words[2])
    
    # Construct a full sentence expression
    return SentenceExpression(subject, verb, obj)

# Example usage
tamil_sentence = "நான் சாப்பிடு பழம்"  # "I eat fruit"
parsed_sentence = parse_tamil_sentence(tamil_sentence)

# Translate the sentence to English
translated_sentence = parsed_sentence.interpret()
print(f"Tamil Sentence: {tamil_sentence}")
print(f"English Translation: {translated_sentence}")

### Expected Output
# Tamil Sentence: நான் சாப்பிடு பழம்
# English Translation: I eat fruit