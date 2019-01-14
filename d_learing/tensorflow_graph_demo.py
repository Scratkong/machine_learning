import tensorflow as tf

def graph_demo():
    """图栗"""
    # 构建阶段：图：tensorflow将计算表示为指令之间的以来关系的一种表示法
    tf_a = tf.constant(10)
    tf_b = tf.constant(20)
    sum_tfab = tf_a + tf_b
    print('sum_tfab is:', sum_tfab)

    # 查看默认图
    # 方法１
    print('方法１查看默认图', tf.get_default_graph())

    # 方法２
    print('方法２查看默认图tf_a.graph:', tf_a.graph)
    print('方法２查看默认图tf_b.graph:', tf_b.graph)
    print('放法２查看默认图sum_tfab.graph', sum_tfab.graph)

    # 手动创建图
    new_g = tf.Graph()
    print('new_g', new_g)
    # 在自己定义的图中定义数据和操作
    with new_g.as_default():
        new_a = tf.constant(30)
        new_b = tf.constant(40)
        sum_newab = tf.add(new_a, new_b)
        print('='*10,new_a,new_b,sum_newab)

    # 开启会话，指定自定义的图
    with tf.Session(graph = new_g) as sess_new:
        sum_newab_value = sess_new.run(sum_newab)
        print('sum_newab_value', sum_newab_value)

    return None

if __name__ == '__main__':
    graph_demo()