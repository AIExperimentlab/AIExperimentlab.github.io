from modules.nlp import NLPModule
from modules.knowledge import KnowledgeEngine
import pandas as pd

class MagnusOpusV2:
    def __init__(self):
        print("[*] Initializing Magnus Opus 2.0 Advanced...")
        self.nlp = NLPModule()
        self.kb = KnowledgeEngine()
        
    def ingest_document(self, text: str):
        """Example: Extract entities and classify sentiment."""
        tokens = self.nlp.preprocess(text)
        sentiment = self.nlp.classify(text)
        print(f"Processed: {len(tokens)} tokens. Sentiment Distribution: {sentiment}")
        return tokens

    def run_demo(self):
        # 1. NLP Task
        self.ingest_document("Magnus Opus is a highly scalable AI architecture.")
        
        # 2. Knowledge Graph Task
        self.kb.add_relationship("MagnusOpus", "contains", "NLPModule")
        self.kb.add_relationship("NLPModule", "uses", "Transformers")
        print("[*] Knowledge Graph updated. Visualizing...")
        self.kb.visualize()

if __name__ == "__main__":
    system = MagnusOpusV2()
    system.run_demo()
