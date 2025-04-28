from typing import Sequence, List
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, MessageGraph
from chains import generate_chain, reflect_chain

class TweetReflectorGraph:
    def __init__(self):
        self.REFLECT = "reflect"
        self.GENERATE = "generate"
        self.graph = self._build_graph()

    def _generation_node(self, state: Sequence[BaseMessage]):
        return generate_chain.invoke({"messages": state})

    def _reflection_node(self, messages: Sequence[BaseMessage]) -> List[BaseMessage]:
        res = reflect_chain.invoke({"messages": messages})
        return [HumanMessage(content=res.content)]

    def _should_continue(self, state: List[BaseMessage]) -> bool:
        return len(state) <= 6

    def _build_graph(self):
        builder = MessageGraph()
        builder.add_node(self.GENERATE, self._generation_node)
        builder.add_node(self.REFLECT, self._reflection_node)
        builder.set_entry_point(self.GENERATE)

        builder.add_conditional_edges(
            self.GENERATE,
            self._should_continue,
            {
                True: self.REFLECT,
                False: END
            }
        )
        builder.add_edge(self.REFLECT, self.GENERATE)

        return builder.compile()

    def get_graph(self):
        return self.graph

    def visualize(self):
        print(self.graph.get_graph().draw_mermaid())
        self.graph.get_graph().print_ascii()

    def process(self, messages):
        return self.graph.invoke(messages) 