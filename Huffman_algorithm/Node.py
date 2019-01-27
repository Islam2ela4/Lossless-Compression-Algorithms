class Node(object):

    item = None
    frequancy = 0
    child_left = None
    child_right = None

    def __init__(self, i, f):
        self.item = i
        self.frequancy = f

    def setChildren(self, ln, rn):
        self.child_left = ln
        self.child_right = rn

    def __repr__(self):
        return "%s - %s -> %s _ %s" % (self.item, self.frequancy, self.child_left, self.child_right)

    # defining comparators less_than
    def __lt__(self, other):
        return self.frequancy < other.frequancy



