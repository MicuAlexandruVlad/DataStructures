class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    if user in group.get_users():
        return True
    else:
        for subGroup in group.get_groups():
            return is_user_in_group(user, subGroup)

    return False

def tests():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)


    print(is_user_in_group("sub_child_user", parent))

    parent1 = Group("parent1")
    child1 = Group("child1")
    sub_child1 = Group("subchild1")
    sub_sub_child_1 = Group("subsubchild1")

    sub_child_user1 = "sub_child_user1"
    sub_sub_child_1.add_user(sub_child_user1)

    sub_child.add_group(sub_sub_child_1)
    child1.add_group(sub_child1)
    parent1.add_group(child)


    print(is_user_in_group("sub_child_user1", parent1))

    parent2 = Group("parent2")
    child2 = Group("child2")
    sub_child2 = Group("subchild2")
    ss_child = Group("subsubchild2")
    sss_child = Group("subsubsubchild2")


    sub_child_user2 = "sub_child_user"
    child_user = "child_user"
    ss_child.add_user(sub_child_user2)
    ss_child.add_group(sss_child)
    sub_child2.add_group(ss_child)
    child2.add_group(sub_child2)
    child2.add_user(child_user)
    parent2.add_group(child2)


    print(is_user_in_group("sub_child_user2", parent2))

tests()