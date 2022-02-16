from math import floor, log2, pow


def print_tree(tree, value_space=5):
    depth = floor(log2(len(tree))) + 1
    bottom_width = pow(2, depth - 1) * value_space
    for level in range(depth):
        left_idx = int(pow(2, level)) - 1
        right_idx = int(pow(2, level + 1)) - 1
        num_nodes = right_idx - left_idx
        node_space = int(bottom_width // num_nodes)
        for i in range(left_idx, min(right_idx, len(tree))):
            value = tree[i]
            value_width = len(str(value))
            value_pos = floor(node_space / 2 - value_width / 2)
            left_padding = ' ' * value_pos
            right_padding = ' ' * (node_space - (value_pos + value_width))
            print(f'{left_padding}{tree[i]}{right_padding}', end='')
        print()


def test1():
    tree = [i for i in range(16)]
    print_tree(tree)


if __name__ == '__main__':
    test1()
