class Tree_height:
    def __init__(self, tree_heightVal=0):
        self.tree_heightVal = tree_heightVal
    
    def get_height(self):
        return self.tree_heightVal


class WhitebarkTree(Tree_height):
    def irrigate(self):
        self.tree_heightVal = self.tree_heightVal + 2
        return self.tree_heightVal


class FoxtailPine(Tree_height):
    def irrigate(self):
        self.tree_heightVal = self.tree_heightVal + 1


class Lumberjack:
    def canCut(self, Tree_height):
        if Tree_height.get_height() > 4:
            True
        else:
            False


class Forest:
    def __init__(self, allTree=[]):
        self.allTree = allTree
    
    def getTrees(self):
        return self.allTree
    
    def rain(self):
        for tr in self.allTree:
            tr.irrigate()
    
    def cut_trees(self, lumberjack):
        self.allTree = [tr for tr in self.allTree if not lumberjack.canCut(tr)]
    
    def is_empty(self):
        if len(self.allTree) == 0:
            return True
        else:
            return False
    
    def get_status(self):
        statusReport = []
        for tr in self.allTree:
            statusReport.append(f"There is a {tr.get_height()} tall FoxtailPine in the forest.")
        return statusReport

