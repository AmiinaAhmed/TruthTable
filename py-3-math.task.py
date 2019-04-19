######################### Propositions With Braces & Truth_Table ##########################

###========================================================================================
def not_(a):
    return not a
 
 
def and_(a, b):
    return a and b
 
 
def or_(a, b):
    return a or b
 
 
def imply(a, b):
    if a == True and b == False:
        return False
    else:
        return True
 
 
def back_imply(a, b):
    if a == True and b == False:
        return True
    else:
        return False
 
###========================================================================================

def is_balanced(expression):
   if len(expression) == 1 and expression >= "a" and expression <= "z":
      return True
 
   mapping = dict(zip('(', ')'))
   queue = []
   for letter in expression:
      if letter != ')' and letter != '(':
         continue
      elif letter in mapping:
         queue.append(mapping[letter])
      elif not (queue and letter == queue.pop()):
         return False
   return not queue
 
###========================================================================================

def grouppingUsingBrackets(inp):
   print("\nStep by step solution:");
   cnt = 1
 
   idx = 0
   moved = 0
   for letter in inp:
      if letter == '¬':
         inp = inp[: idx + moved] + '(' + inp[idx + moved: idx + moved + 2] + ')' + inp[idx + moved + 2:]
         moved += 2
         print(cnt, inp)
         cnt += 1
      idx += 1
 
   idx = 0
   moved = 0
   for letter in inp:
      if letter == '∧':
         left = -1
         right = -1
         for ch in range(idx + moved + 2, len(inp)+1):
            if is_balanced(inp[idx + moved + 1: ch]):
               right = ch
               break
 
         for ch in range(idx + moved - 1, -1, -1):
            if is_balanced(inp[ch: idx + moved]):
               left = ch
               break
         inp = inp[: left] + '(' + inp[left: right] + ')' + inp[right:]
         moved += 2
         print(cnt, inp)
         cnt += 1
      idx += 1
 
   idx = 0
   moved = 0
   for letter in inp:
      if letter == '∨':
         left = -1
         right = -1
         for ch in range(idx + moved + 2, len(inp) + 1):
            if is_balanced(inp[idx + moved + 1: ch]):
               right = ch
               break
 
         for ch in range(idx + moved - 1, -1, -1):
            if is_balanced(inp[ch: idx + moved]):
               left = ch
               break
         inp = inp[: left] + '(' + inp[left: right] + ')' + inp[right:]
         moved += 2
         print(cnt, inp)
         cnt += 1
      idx += 1
 
   idx = 0
   moved = 0
   for letter in inp:
      if letter == '⇒':
         left = -1
         right = -1
         for ch in range(idx + moved + 2, len(inp) + 1):
            if is_balanced(inp[idx + moved + 1: ch]):
               right = ch
               break
 
         for ch in range(idx + moved - 1, -1, -1):
            if is_balanced(inp[ch: idx + moved]):
               left = ch
               break
         inp = inp[: left] + '(' + inp[left: right] + ')' + inp[right:]
         moved += 2
         print(cnt, inp)
         cnt += 1
      idx += 1
 
   idx = 0
   moved = 0
   for letter in inp:
      if letter == '⇔':
         left = -1
         right = -1
         for ch in range(idx + moved + 2, len(inp) + 1):
            if is_balanced(inp[idx + moved + 1: ch]):
               right = ch
               break
 
         for ch in range(idx + moved - 1, -1, -1):
            if is_balanced(inp[ch: idx + moved]):
               left = ch
               break
         inp = inp[: left] + '(' + inp[left: right] + ')' + inp[right:]
         moved += 2
         print(cnt, inp)
         cnt += 1
      idx += 1
 
   return inp;
   
###========================================================================================

class WFF:
    precedence = {
        '¬': 1,
        '∧': 2,
        '∨': 3,
        '⇒': 4, 
        '⇔': 4,
    }
 
    operator = {
        '¬': not_,
        '∧': and_, 
        '∨': or_, 
        '⇒': imply, 
        '⇔': back_imply,
    }
    
###========================================================================================
 
    def __init__(self, wff):
        self.wff = wff.replace(' ', '')
        self.postForm = self.postFormTransfer()
        self.pVars = self.get_pVars()
        self.ptvDicts = self.possibleTruthValueDictList()
        self.truthTable = [self.logicEval(ptvDict) for ptvDict in self.ptvDicts]
        
###========================================================================================
 
    def get_pVars(self):
        pVarSet = set()
        for i in self.wff:
            if i.isalpha(): pVarSet.add(i)
        pVars = list(pVarSet)
        pVars.sort()
        return pVars
        
###========================================================================================
 
    def possibleTruthValueDictList(self):
        def TorF(n=0, d={}):
            if n == len(self.pVars):
                ptvd = d.copy()
                ptvDicts.append(ptvd)
                return None
            for i in [True, False]:
                d[self.pVars[n]] = i
                TorF(n + 1, d)
 
        ptvDicts = []
        TorF()
        return ptvDicts
 
###========================================================================================

    def postFormTransfer(self):
        postForm = []
        tmpList = []
        for i in self.wff:
            if i.isalpha():
                postForm.append(i)
            elif i == ')':
                while True:
                    op = tmpList.pop()
                    if op == '(':
                        break
                    else:
                        postForm.append(op)
            else:
                try:
                    while WFF.precedence[tmpList[-1]] >= WFF.precedence[i]:
                        postForm.append(tmpList.pop())
                    tmpList.append(i)
                except:
                    tmpList.append(i)
        while len(tmpList) > 0:
            postForm.append(tmpList.pop())
        return postForm
 
###========================================================================================

    def logicEval(self, truthValueDict):
        container = []
        for i in self.postForm:
            if i.isalpha():
                container.append(truthValueDict[i])
            else:
                op = WFF.operator[i]
                if i == '¬':
                    container.append(op(container.pop()))
                else:
                    container.append(op(container.pop(-2), container.pop()))
        return container[0]
 
###========================================================================================

if __name__ == '__main__':
    print("Enter the proposition without any spaces or brackets:")
    wff = WFF(grouppingUsingBrackets(input()))
    print()
 
    print("Truth Table")
    #First row of the table
    for letter in wff.pVars:
        print(letter, end="\t")
    print(wff.wff)
 
    #Body of the table
    for i in range(0, len(wff.truthTable)):
        for letter in wff.pVars:
            print(wff.ptvDicts[i][letter], end="\t")
        print(wff.truthTable[i])
 
###========================================================================================

    ### Testcases:
    ### p∨q⇒p∧q
    ### p∨q∧r⇒p∧r∨q
    ### p⇒q⇒p
    ### p∧¬q∨¬p⇔q
    ### F∨G∧¬F∧G
    ### p⇒q∨p⇒¬q
    ### ¬p∨q∧q⇒¬r∧¬p∧p∨r
    ### p∧¬q⇒p∧q
    ### p⇒q∧¬q
    ### p⇒p⇒p
    ### p⇒q∧¬q⇒¬p
    ### p⇒q⇒p⇒¬q
    ### p∨q⇒r∨p∨q
    ### p∨q∧p⇒r∧q∧q⇒¬r∧p
    ### p⇒q⇒r⇒p⇒q⇒p⇒r
    ### p∨q∧¬q∧¬p
    ### ¬p⇒q∨p∧¬r⇔q
    ### p⇒q∧p⇒¬q
    ### p⇒q∨r∨r⇒¬p
    ### D⇒B∧C
    ### C⇒¬A∧¬B
    ### D⇔C∧¬A
    ### D⇒¬C⇒A
    ### ¬D⇒C∧D⇒¬B
    ### A⇒¬B∧¬C⇒D
    ### A∧B∧C⇔¬D∧¬A∧¬B⇒D⇔C
    
###========================================================================================