# 给定 index 寻找父节点
parent = (index - 1) // 2 = (index - 1) >> 2

# 给定 index 寻找子节点
left = 2 * index + 1 = (index << 1) + 1
right = 2 * index + 2 = left + 1

# 初始化
class MaxHeap:
    def __init__(self, maxSize=None):
        self.maxSize = maxSize
        self.list = [None] * maxSize
        self.count = 0
 
    # 当前堆中的元素
    def length(self):
        # 求数组的长度
        return self.count
 
    # 展示当前堆中所有元素，乱序
    def show(self):
        if self.count <= 0:
            print('null')
        else:
            print(self.list[: self.count])
 
    # 判断堆是否为空
    def isEmpty(self):
        if self.count <= 0:
            return True
        else:
            return False

    # 向堆中添加元素
    def add(self, value):
        if self.count >= self.maxSize:
            raise Exception('full')
        self.list[self.count] = value  # 将新节点增加到最后
        self._shift_up(self.count)  # 递归构建大堆
        self.count += 1
 
    def _shift_up(self, index):
        if index > 0:
            parent = (index - 1) // 2  # 找到根节点
            if self.list[index] > self.list[parent]:  # 交换结点
                self.list[index], self.list[parent] = self.list[parent], self.list[index]
                self._shift_up(parent)  # 继续递归从底往上判断

    def extract(self):
        # 弹出最大堆的根节点，即最大值
        if not self.count:
            raise Exception('null')
        value = self.list[0]
        self.count -= 1
        # 最后的值放在顶端
        self.list[0] = self.list[self.count]
        # 最后一位置为 None
        self.list[self.count] = None
        self._shift_down(0)
        return value
 
    def _shift_down(self, index):
        # 获取左右节点索引
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
 
        # 分别与左右节点比较大小
        if left < self.length() and self.list[left] > self.list[largest]:
            largest = left
        if right < self.length() and self.list[right] > self.list[largest]:
            largest = right
 
        # 向下递归寻找
        if largest != index:
            self.list[index], self.list[largest] = self.list[largest], self.list[index]
            self._shift_down(largest)
