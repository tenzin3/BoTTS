from botok import WordTokenizer
from bophono import UnicodeToApi

class Phenomer:
    def __init__(self):
        self.tokenizer = WordTokenizer()
        self.converter = UnicodeToApi(schema="MST", options={'aspirateLowTones': True})

    def tokenize(self, text)->list[str]:
        tokens = self.tokenizer.tokenize(text)
        texts = [token.text.strip() for token in tokens if token.text.strip()]
        return texts

    def text_to_phonemes(self, text):
        return self.converter.get_api(text)

    def run(self, text):
        tokens = self.tokenize(text)
        phonemes = [self.text_to_phonemes(token) for token in tokens]
        return " ".join(phonemes)


if __name__ == "__main__":
    # Example Usage
    input_text = "བཀྲ་ཤིས་བདེ་ལེགས།"
    phenomer = Phenomer()
    result = phenomer.run(input_text)

    print(f"Original: {input_text}")
    print(f"Phonemes: {result}")