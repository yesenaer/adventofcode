import uuid
from typing import List, Dict
from treelib import Node, Tree


class File:
    size: int

    def __init__(self, size):
        self.size = size


class FileSystem:
    root: Tree
    working_dir: str

    def __init__(self):
        self.root = Tree()
        self.root.create_node("/", identifier='/', data=File(0))
        self.working_dir = self.root.get_node('/')


    def process_command(self, command: str):
        if command.startswith('$ cd'):
            target_dir = (command.split())[2].strip()
            self.change_directory(target_dir)

        elif command.startswith('$ ls'):
            pass

        elif command.startswith('dir '):
            new_dir = command.replace('dir ', '').strip()
            self.root.add_node(Node(tag=new_dir, identifier=uuid.uuid1(), data=File(0)), parent=self.working_dir.identifier)

        else:
            file_info = command.strip().split()
            filesize, filename = int(file_info[0]), file_info[1]
            self.root.add_node(Node(tag=f'{filename} size={filesize}', identifier=uuid.uuid1(), data=File(filesize)), parent=self.working_dir.identifier)
            # update parent(s) size
            self.working_dir.data.size += filesize
            current_lvl = self.root.parent(self.working_dir.identifier)
            if not current_lvl.is_root():
                should_continue = True
                while should_continue:

                    current_lvl.data.size += filesize
                    new_lvl = self.root.parent(current_lvl.identifier)
                    if new_lvl.is_root():
                        new_lvl.data.size += filesize
                        should_continue = False
                    else:
                        current_lvl = new_lvl
            else:
                current_lvl.data.size += filesize

    def change_directory(self, target_dir: str):
        if not target_dir:
            raise Exception('target dir not specified')

        if target_dir == '/':
            self.working_dir = self.root.get_node('/')
        elif target_dir == '..':
            if self.working_dir.tag != '/':
                self.working_dir = self.root.parent(self.working_dir.identifier)
        else:
            identifier = self.get_node_identifier_by_tag(target_dir)
            self.working_dir = self.root.get_node(identifier)

    def get_node_identifier_by_tag(self, name: str):
        list_of_children = self.working_dir.fpointer
        for node in list_of_children:
            current = self.root.get_node(node)
            if current.tag == name:
                return current.identifier


def first_assignment(f: str) -> int:
    total_score = 0
    fs = FileSystem()
    with open(f) as file:
        for line in file:
            fs.process_command(line)

    fs.root.show( data_property='size')
    # print(','.join([fs.root[node].tag for node in fs.root.expand_tree(filter = lambda x: \
    #   not x.is_leaf() and x.data.size < 100000 )]))

    for node in fs.root.all_nodes_itr():
        if not node.is_leaf():
            if node.data.size <= 100000:
                total_score += node.data.size

    return total_score


def second_assignment(f: str) -> int:
    total_score = 0
    total_disk_space = 70000000
    required_free_space = 30000000

    fs = FileSystem()
    with open(f) as file:
        for line in file:
            fs.process_command(line)

    disk_space_in_use = fs.root.get_node('/').data.size
    # print(f'disk size in use is now: {disk_space_in_use}')
    required_size_deletion = disk_space_in_use - (total_disk_space - required_free_space)
    # print(f'required deletion size is: {required_size_deletion}')
    smallest_possible_node = fs.root.get_node('/')
    for node in fs.root.all_nodes_itr():
        if node.is_leaf():
            continue
        if node.data.size > required_size_deletion:
            if node.data.size < smallest_possible_node.data.size:
                smallest_possible_node = node
    total_score = smallest_possible_node.data.size

    return total_score


puzzle_input = 'resources/day7_input.txt'
print(f'answer to assignment 1 is: {first_assignment(puzzle_input)}')
print(f'answer to assignment 2 is: {second_assignment(puzzle_input)}')
