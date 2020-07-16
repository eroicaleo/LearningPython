#!/usr/bin/env python

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def linkListBuilder(nodeString):
    nodeList = [None if n == 'null' else int(n) for n in nodeString[1:-1].split(',')]
    print(nodeList)
    st, level_list, last_cut = 0, [], 0
    for i, n in enumerate(nodeList):
        if isinstance(n, int):
            st = 1
        elif n == None:
            if st == 1:
                level_list.append(nodeList[last_cut:i])
                last_cut = i+1
                st = 0
    level_list.append(nodeList[last_cut:])
    print(level_list)
    print('front aligned:')
    prev_alig = 0
    level_list_front_aligned = [level_list[0]]
    for i, l in enumerate(level_list[1:]):
        for j, v in enumerate(l):
            if v != None:
                break
        level_list_front_aligned.append([None]*prev_alig+l)
        prev_alig = j
    print(level_list_front_aligned)

    # Stitch within the same level
    level_node_list = []
    for l in level_list_front_aligned:
        level_nodes = [Node(n,None,None,None) for n in l]
        for i, n in enumerate(level_nodes):
            if i < len(level_nodes)-1:
                level_nodes[i].next = level_nodes[i+1]
            if i > 0:
                level_nodes[i].prev = level_nodes[i-1]
        print('level:')
        traverse_level(level_nodes[0])
        level_node_list.append(level_nodes)

    # Stitch across the level
    for i, l in enumerate(level_node_list):
        if i == 0:
            continue
        for j, n in enumerate(l):
            if n.val:
                n.prev = None
                level_node_list[i-1][j].child = n
                break

    print(f'#'*80)
    print(f'# Final traverse')
    print(f'#'*80)
    # traverse again
    for i, l in enumerate(level_node_list):
        for n in l:
            if n.val:
                print(f'level {i}')
                traverse_level(n)
                break
    return level_node_list[0][0]

def traverse_level(node):
    def node_val(n):
        return n.val if n else None
    while node:
        prev, next, child = node.prev, node.next, node.child
        print(f'node {node.val}, prev = {node_val(prev)}, next = {node_val(next)}, child = {node_val(child)}')
        node = node.next

if __name__ == '__main__':
    nodeString = '[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]'
    nodeString = '[1,2,null,3]'
    linkListBuilder(nodeString)
