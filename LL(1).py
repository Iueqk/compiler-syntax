"""
主程序
"""
from lexical.lexical import Lexical
from syntax.rule import fileOutProductions
from syntax.syntax import Syntax, Tree
from tree import TreeVisualizer

# 新建词法分析器
lexical = Lexical()
# 载入源代码
lexical.load_source(open('test.c',encoding='utf-8').read())
# 执行词法分析
lexical_success = lexical.execute()
# 打印结果
print('词法分析是否成功:\t', lexical_success)
if lexical_success:
    lexical_result = lexical.get_result()
    print('词法分析结果:')
    for i in lexical_result:
        print("{:<7} {:<7} {:<3}".format(i.type, i.str, i.line))

    # # 开始执行语法分析
    fileOutProductions()
    syntax = Syntax()
    syntax.put_source(lexical_result)
    syntax_success = syntax.execute()
    print('语法分析是否成功\t', syntax_success)
    if syntax_success:
        print('语法分析结果:\n')
        tree = TreeVisualizer(syntax.grammar_tree)
        tree.visualize()
        Tree.print_tree(syntax.grammar_tree.root)
    else:
        print('错误原因:\t', syntax.get_error().info, syntax.get_error().line, '行')
else:
    print('错误原因:\t', lexical.get_error().info)
