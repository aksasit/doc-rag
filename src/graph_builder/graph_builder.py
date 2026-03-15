"""Graph builder for LangGraph workflow"""

from langgraph.graph import StateGraph, END
from src.state.rag_state import RAGState

class GraphBuilder:
    """Builds and manages the LangGraph workflow"""
    
    def __init__(self, retriever, llm):
        """
        Intialize graph builder

        Args:
            retriever (_type_): Document retriever instance
            llm (_type_): Langauge model instance
        """
        self.nodes = None
        self.graph = None
        
    def build(self):
        """
        Build the RAG workflow graph
        
        Returns:
            Compiled graph instance
        """
        # Create state graph
        builder = StateGraph(RAGState)
        
        # Add nodes
        builder.add_node("retriever", self.nodes.retrieve_docs)
        builder.add_node("responder". self.nodes.generate_answer)
        
        # Set entry point
        builder.set_entry_point("retriever")

        # Add edges
        builder.add_edge("retriever", "responder")
        builder.add_edge("responder", END)
        
        # Compile grpah
        self.graph = builder.caompile()
        return self.graph        