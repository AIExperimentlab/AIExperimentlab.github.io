import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class NLPModule:
    def __init__(self, model_name="bert-base-uncased"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name).to(self.device)

    def preprocess(self, text: str):
        tokens = word_tokenize(text.lower())
        return [self.lemmatizer.lemmatize(t) for t in tokens if t.isalnum() and t not in self.stop_words]

    def classify(self, text: str):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True).to(self.device)
        with torch.no_grad():
            outputs = self.model(**inputs)
        return torch.nn.functional.softmax(outputs.logits, dim=-1).cpu().numpy()
