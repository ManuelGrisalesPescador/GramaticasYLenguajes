#Manuel Alejandro Grisales Pescador

class ASTTraverser(object):
    def __init__(self):
        pass


    ##############################
    ## Methods to visit the AST ##
    ##############################
    def visit(self, tree):
        #print("Visitor")
        #print("visit*- {}".format(tree))
        method = getattr(self, tree.head, None)
        # print("Visit for {} will call {}".format(tree.head, method))
        if method:
            return method(tree)
        else:
            print("Method {} is not defined by the class".format(method))

    def start(self, tree):
        #print("Start*- {}".format(tree))
        # la regla start solo puede tener un hijo (segun la gramatica) y estará
        # en tree.tail[0]
        le = tree.tail[0]
        self.visit(le)

    def program(self, tree):
        #print("program expression {}".format(tree))
        #print(len(tree.tail))
        if len(tree.tail) == 1:
            #print(tree.tail[0])
            print(self.visit(tree.tail[0]))
    
    def logicalexpression(self, tree, case = False):
        #print("Logical expression {}".format(tree))
        #print(len(tree.tail))
        #print(case)
        if case == True:
            
            if len(tree) == 1:
                #print(tree[0])
                #self.visit(tree.tail[0])
                #print(tree[0])
                return tree[0]
            elif (len(tree) == 2 and tree.tail[0] == 'not'):
                x = self.visit(tree.tail[1])
                return (f"(!{x})")
            else:
                
                leftExp = tree[0]
                
                y = self.visit(leftExp)
                #print("Got Case")
                rightExp = tree[2]
                x = self.visit(rightExp)
                rel = tree[1]
        else:
            if len(tree.tail) == 1:
                #print(tree.tail[0])
                #self.visit(tree.tail[0])
                #print(tree.tail[0])
                return tree.tail[0]
            elif (len(tree.tail) == 2 and tree.tail[0] == 'not'):
                x = self.visit(tree.tail[1])
                return (f"(!{x})")
            else:
                #More than one
                leftExp = tree.tail[0]
                y = self.visit(leftExp)
                rightExp = tree.tail[2]
                x = self.visit(rightExp)
                rel = tree.tail[1]
                #print("Individual Stuff:")
                #print(x)
                #print(y)
                #print(rel)

        if rel == "==":
            #print("eq")
            return (f"(({x} * {y}) + (!{x} * !{y}))")
            
        if rel == "!=":
            return (f"(({x} + {y}) * (!{x} + !{y}))")

        if rel == "or":
            return (f"({x} + {y})")
        
        if rel == "and":
            return (f"({x} * {y})")

        if rel == "nand":
            return (f"(!({x} * {y}))")

        if rel == "nor":
            return (f"(!({x} + {y}))")
        
        if rel == "xor":
            return (f"(({x} * !{y}) + (!{x} * {y}))")

        if rel == "xnor":
            return (f"(({x} * {y}) + (!{x} * !{y}))")
                
                
    
    def parexpression(self, tree):
        #print("parexpression {}".format(tree))
        #print(len(tree.tail))
        return self.visit(tree.tail[1])

    def conditional(self, tree, case = False, Index1 = 0, Index2 = 0):
        #print("Conditional pass")
        #print(tree.tail)
        #print(case)
        #print(Index1)
        #print(Index2)

        if case == "true":
            
            count = tree.tail.count('case')
            #print((4 * count))
            MainVar = tree.tail[1]
            #Index1 = 3
            #Index2 = 5
            if Index1 < (4 * count):
                #print(tree.tail[Index1])
                #print(tree.tail[Index2])
                #print("Get recursive")


                return(f"(({self.visit(tree.tail[Index2])}) * ({self.logicalexpression([tree.tail[Index1], '==', MainVar], True)})) + (({self.conditional(tree, 'true', Index1 + 4, Index2 + 4)}) * !({self.logicalexpression([tree.tail[Index1], '==', MainVar], True)}))")
                #return(f"{self.visit(tree.tail[Index2])} * {self.visit(logicalexpression({tree.tail[index1]} == {MainVar}))}")
                #Index1 += 4
                #Index2 += 4


                #f"({self.visit(tree.tail[Index2])} * {self.visit(logicalexpression(f"'{tree.tail[index1]}' == '{MainVar}'"))}) + ({self.visit(tree.tail[Index2])} * !{self.visit(logicalexpression(f"'{tree.tail[index1]}' == '{MainVar}'"))})"


            else:
                return self.visit(tree.tail[len(tree.tail) - 1]) 
        else:
            #print(f"({self.visit(tree.tail[3])} * {self.visit(tree.tail[1])}) + ({self.visit(tree.tail[5])} + !{self.visit(tree.tail[1])})")


            #Return a mux which evaluates the expression at the "if", if true/1, evaluates then, otherwise evaluates else

            return(f"({self.visit(tree.tail[3])} * {self.visit(tree.tail[1])}) + ({self.visit(tree.tail[5])} * !{self.visit(tree.tail[1])})")

            #self.visit(tree.tail[0])
            pass

    def switchexpression(self, tree):
        print(tree.tail)
        return self.conditional(tree, "true", 3, 5)
        pass

    def boolexpression(self, tree):
        #print(tree.tail)
        #return the bool expression "x and y"
        return(f"({self.visit(tree.tail[0])} {tree.tail[1]} {self.visit(tree.tail[2])})")

    def listexpression(self, tree):
        print(tree.tail)
        array = []
        for x in tree.tail:
            if (x != '(') and (x != ')') and (x != ',') and (x != 'list'):
                array.append(self.visit(x))

        if len(array) == 0:
            return "null"
        else:
            return(array)

    def functiondef(self, tree):
        print("g")
        print(tree.tail)

    def variable(self, tree):
        name = tree.tail[0]
        #print("Variable*- {}".format(name))
        #return the name of the variable "x"
        return name

    def number(self, tree):
        number = tree.tail[0]
        return number

   