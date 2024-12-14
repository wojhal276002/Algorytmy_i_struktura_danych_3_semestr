class RootError(Exception):
    pass

class ChildError(Exception):
    pass

class ParentError(Exception):
    pass

class NodeError(Exception):
    pass
#błędy wyświetlane

#listy do wykorzystania przy klasie TreeNode oraz tokenizacji
all_symbols= ['+','-','*','/','^','(',')','sin','cos','exp','log']
funkcje = ['sin','cos','exp','log']

class TreeNode:
    #metody zaproponowane przez Pana
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value              # string, stored value
        self.left_child = left_child    # None or TreeNode instance
        self.right_child = right_child  # None or TreeNode instance

    def get_value(self):
        return self.value

    def add_left_child(self, value):
        self.left_child = value

    def add_right_child(self, value):
        self.right_child = value

    def get_left_child(self):
        if self.has_left_child:
            return self.left_child
        else:
            raise ChildError("Left child doesn't exist")

    def get_right_child(self):
        if self.has_right_child:
            return self.right_child
        else:
            raise ChildError("Right child doesn't exist")

    def has_left_child(self) -> bool:
        if self.left_child is not None:
            return True
        else:
            return False

    def has_right_child(self) -> bool:
        if self.right_child is not None:
            return True
        else:
            return False

    def is_leaf(self) -> bool:
        if self.has_left_child() or self.has_right_child():
            return False
        else:
            return True

    #metoda, która pozwala przedstawić instancję drzewa w formie przystępnej dla odbiorcy, czyli pisanej (nawiasy według normy)
    def __str__(self):
        if self.left_child is None:
            a = ""
        else:
            a = str(self.left_child)
        if self.right_child is None:
            b = ""
        else:
            b = str(self.right_child)
        if self.value in '+-*/^':
            return "("+a+str(self.value)+b+")"
        elif self.value in funkcje:
            return str(self.value) + "(" + b + ")"
        else:
            return a + str(self.value) + b

def tokenize(raw):
    raw = raw.replace(" ","")
    mark = 0
    tokens=[]
    n = len(raw)
    for j in range(n):
        if raw[j] in all_symbols:
            if mark != j:
                tokens.append(raw[mark:j])
            if raw[j] != '':
                tokens.append(raw[j])
            mark = j+1
    if mark != n:
        tokens.append(raw[mark:n])
    return tokens
#funkcje z wykładu z małymi modyfikacjami dla metod z listy funkcje
def build_expression_tree(tokens):
    S = []
    for t in tokens:
        if t in '+-*/^':
            S.append(t)
        elif t not in '()':
            if t in funkcje:
                S.append(t)
            else:
                S.append(TreeNode(t))
        elif t == ')':
            right = S.pop()
            op = S.pop()
            if op in funkcje:
                S.append(TreeNode(op,None,right))
            else:
                left = S.pop()
                S.append(TreeNode(op,left,right))
    return S.pop()

def derivative_on_tree(tree, var):
    """
    Rekurencyjna funkcja odpowiedzialna za wykonanie pochodnej na drzewie, które podajemy na początku

    Parametry:
    tree - TreeNode class
        drzewo wyrażenia,które chcemy poddać działaniu pochodnej
    var - str
        zmienna, po której chcemy dokonać różniczkowania
    Output:
        pochodna drzewa, którą chcemy uzyskać

    """
    if tree.is_leaf():
        if tree.value == var:
            return "1"
        else:
            return "0"
    else:
        if tree.value == "*":
            new_tree = TreeNode("+")
            new_tree.add_left_child(TreeNode('*', derivative_on_tree(tree.get_left_child(),var), tree.get_right_child()))
            new_tree.add_right_child(TreeNode('*', tree.get_left_child(), derivative_on_tree(tree.get_right_child(),var)))
            return new_tree
        elif tree.value == "+":
            new_tree = TreeNode("+")
            new_tree.add_left_child(derivative_on_tree(tree.get_left_child(),var))
            new_tree.add_right_child(derivative_on_tree(tree.get_right_child(),var))
            return new_tree
        elif tree.value == "-":
            new_tree = TreeNode("-")
            new_tree.add_left_child(derivative_on_tree(tree.get_left_child(),var))
            new_tree.add_right_child(derivative_on_tree(tree.get_right_child(),var))
            return new_tree
        elif tree.value == "/":
            new_tree = TreeNode("/")
            new_tree.add_left_child(
                TreeNode("-", TreeNode("*", derivative_on_tree(tree.get_left_child(), var), tree.get_right_child()),
                         TreeNode("*", tree.get_left_child(), derivative_on_tree(tree.get_right_child(), var))))
            new_tree.add_right_child(TreeNode("*", tree.get_right_child(), tree.get_right_child()))
            return new_tree
        elif tree.value == "^":
            new_tree = TreeNode("*")
            new_tree.add_left_child(derivative_on_tree(tree.get_left_child(),var))
            new_tree.add_right_child(TreeNode("*",tree.get_right_child(),TreeNode("^",tree.get_left_child(),TreeNode("-",tree.get_right_child(),"1"))))
            return new_tree
        elif tree.value == "sin":
            new_tree = TreeNode("*")
            new_tree.add_left_child(derivative_on_tree(tree.get_right_child(), var))
            new_tree.add_right_child(TreeNode("cos", None, tree.get_right_child()))
            return new_tree
        elif tree.value == "cos":
            new_tree = TreeNode("")
            new_tree.add_left_child(derivative_on_tree(tree.get_right_child(), var))
            new_tree.add_right_child(TreeNode("", TreeNode("-", "0", "1"), TreeNode("sin", None, tree.get_right_child())))
            return new_tree
        elif tree.value == "exp":
            new_tree = TreeNode("*")
            new_tree.add_left_child(derivative_on_tree(tree.get_right_child(),var))
            new_tree.add_right_child(TreeNode("exp",None,tree.get_right_child()))
            return new_tree
        elif tree.value == "log":
            new_tree = TreeNode("*")
            new_tree.add_left_child(derivative_on_tree(tree.get_right_child(),var))
            new_tree.add_right_child(TreeNode("/","1",tree.get_right_child()))
            return new_tree


def derivative(expression,var):
    """
    Funkcja odpowiedzialna za połączenie poprzednich metod, pozwalająca na otrzymanie pochodnej wyrażenia początkowego

    Parametry:
    expression - str
        wyrażenie do zróżniczkowania
    var - str
        zmienna, po której różniczkujemy
    Output:
    deriv - str
        pochodna funkcji początkowej w formie stringa

    """
    tokens = tokenize(expression)
    tree = build_expression_tree(tokens)
    deriv = derivative_on_tree(tree,var)
    return deriv

if __name__=="__main__":
    print(derivative("(sin(1/x))","x"))