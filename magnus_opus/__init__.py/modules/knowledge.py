import networkx as nx
import matplotlib.pyplot as plt
from pykeen.pipeline import pipeline
import pandas as pd

class KnowledgeEngine:
    def __init__(self):
        self.graph = nx.DiGraph() # Directed graph for better logic
        self.kb_results = None

    def add_relationship(self, head, relation, tail):
        self.graph.add_edge(head, tail, label=relation)

    def train_reasoning(self, training_data_path: str):
        """Uses PyKEEN to learn embeddings from a triples file."""
        self.kb_results = pipeline(
            dataset_kwargs=dict(training=training_data_path),
            model='TransE',
            epochs=10,
            device='gpu' if torch.cuda.is_available() else 'cpu'
        )
        return self.kb_results

    def visualize(self):
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues)
        edge_labels = nx.get_edge_attributes(self.graph, 'label')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.show()
