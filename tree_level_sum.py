
class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(lst):
    root = Node(1)
    node = root
    for i in lst:
        while node:
            if i > node.value:
                if not node.right: 
                    node.right = Node(i)
                    break
                else:
                    node = node.right
            else:
                if not node.left:
                    node.left = Node(i)
                    break
                else:
                    node = node.left
             
    return root

def level_sum(root):
    from collections import defaultdict, deque
    result = []
    level_element = defaultdict(list)
    nodes = deque()
    if not root:
        return result
    else:
        nodes.append([root,1])

    while nodes:
        node, level = nodes.popleft()
        if node:
            level_element[level].append(node.value)
        if node.left:
            nodes.append([node.left, level+1])
        if node.right:
            nodes.append([node.right, level+1])
    print(f'{level}')
    print(level_element)
    for k,v in level_element.items():
        #print(f'{sum(v)}')
        result.append(float(sum(v)/len(v)))
    return result

def main():
    import random
    lst = [random.randint(1,20) for i in range(10)]
    root = build_tree(lst)
    print(level_sum(root))

if __name__ == '__main__':
    main()
         
