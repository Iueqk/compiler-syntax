import graphviz

class TreeVisualizer:
    def __init__(self, tree):
        """
        构造函数
        :param tree: 语法树
        """
        self.tree = tree  # tree是Node类型  type:Node.data.type value:Node.data.str

    def draw_tree(self):
        # 创建Graph对象
        dot = graphviz.Digraph('grammar_tree', format='jpg')

        # 绘制根节点
        root_node = self.tree.root
        dot.node(name=self.get_node_id(root_node), label=root_node.data.type, fontname='FangSong')

        # 递归绘制直接子节点
        for child in root_node.children:
            self.plot_tree(child, dot)

        dot.view()

    def plot_tree(self, node, dot):
        # 添加当前节点
        dot.node(name=self.get_node_id(node), label=node.data.type, fontname='FangSong')

        # 添加父子关系
        if node.parent is not None:
            dot.edge(self.get_node_id(node.parent), self.get_node_id(node))

        # 递归绘制直接子节点
        for child in node.children:
            self.plot_tree(child, dot)

    def get_node_id(self, node):
        return str(id(node))