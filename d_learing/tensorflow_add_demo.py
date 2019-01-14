import tensorflow as tf

def structure_demo():
    """
    use tensorflow come true  add
    :return:
    """

    # user python
    a = 10
    b = 20
    sum_ab = a + b
    print('sum_ab is :', sum_ab)

    # use tensorflow
    # just define a graph, flow chart: define data and optism

    # 构建阶段：图：tensorflow将计算表示为指令之间的以来关系的一种表示法
    tf_a = tf.constant(10)
    tf_b = tf.constant(20)
    sum_tfab = tf_a + tf_b
    print('sum_tfab is:', sum_tfab)
    # sum_tfab is: Tensor("add:0", shape=(), dtype=int32)

    # 真正运行需要
    # 开启会话
    # 执行阶段：会话：tensorflow的跨一个或多个本地或远程设备运行数据（张量）流图的机制（调配资源工具）
    # 张量：tensorflow中的基本数据对象
    # 节点：提供途中执行的操作
    with tf.Session() as sess:
        sum_tfab_value = sess.run(sum_tfab)
        print('sum_tfab_value', sum_tfab_value)

    # return None
if __name__ == '__main__':
    structure_demo()
