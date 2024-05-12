import queue
from graphviz import Digraph


class TreeVisualizer:
    def __init__(self, tree):
        """
        构造函数
        :param tree: 语法树
        """
        self.tree = tree  # tree是Node类型  type:Node.data.type value:Node.data.str
        self.graph = Digraph('grammar_tree', format='png')

    def visualize(self):
        """
        可视化语法树
        """
        self.visualize_helper()
        self.graph.view()

    def visualize_helper(self):
        """
        层次遍历方式遍历树节点并添加到图中
        """
        # 首先添加根节点到图中
        root_type = str(self.tree.root.data.type)
        self.graph.node(root_type, label=root_type, fontname="FangSong")

        q = queue.Queue()
        q.put(self.tree.root)
        # 用于记录已经连接过的子节点
        connected_nodes = set()

        while not q.empty():
            current_node = q.get()
            for child in current_node.children:
                child_type = str(child.data.type)
                # 如果该子节点没有被连接过，则添加节点和边，并标记为已连接
                if child_type not in connected_nodes:
                    self.graph.node(child_type, label=child_type, fontname="FangSong")
                    self.graph.edge(str(current_node.data.type), child_type)
                    connected_nodes.add(child_type)
                q.put(child)
