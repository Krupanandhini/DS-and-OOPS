class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent =self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level+=1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' '*self.get_level()*4
        prefix = spaces +'* ' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_Vehicle():
    root = TreeNode('Vehicle')

    car = TreeNode('car')
    car.add_child(TreeNode('Audi'))
    car.add_child(TreeNode('BMW'))
    car.add_child(TreeNode('Ford'))

    bike = TreeNode('Bike')
    bike.add_child(TreeNode('Honda'))
    bike.add_child(TreeNode('TVS'))
    bike.add_child(TreeNode('Royal Enfield'))

    root.add_child(car)
    root.add_child(bike)

    root.print_tree()

if __name__ =='__main__':
    build_Vehicle()

