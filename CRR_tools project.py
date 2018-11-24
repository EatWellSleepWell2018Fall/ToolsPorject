
class Node:
    def __init__(self, s0):
        """
        self.val: stock price
        self.val1: call option price
        self.val2: put option price
        self.left: one of the stock price's children increase to u*self.val with prob p
        self.right: the other of the stock price's children decrease to d*self.val with prob (1-p)
        """
        
        
        self.val = s0
        self.val1 = s0
        self.val2 = s0
        self.left = None
        self.right = None
        self.p = 1
        
def CRR_model(stock_price, strike_price, var, r_f, ttm, n_times):

    import numpy as np
    
    queue = []

    def bfs(root, n_times):
        queue.append(root)
        var_act = (var/365) * (ttm/n_times)
        u = np.exp(var_act*((ttm/n_times)**0.5))
        print("u: ",u)
        d = 1/u 
        print("d: ",d)
        p = (np.exp(r_f*(ttm/n_times) - d))/(u - d)
        print("p: ", p)
        
        n = pow(2,n_times) - 1 
        count = 1
        while queue is not None:
            top = queue.pop(0)
            left = Node(u*top.val)
            right = Node(d*top.val)
            left.p = p*top.p
            right.p = (1-p)*top.p
            top.left = left
            top.right = right
            queue.append(left)
            queue.append(right)
            count += 2
            if count >= n:
                break
                
    ans = []
    probs = []
    def dfs(root):
        if root.left is None:
            ans.append(root.val)
            probs.append(root.p)
            root.val1 = root.val2 = root.val
            
            root.val1 = max(root.val1-strike_price, 0)
            root.val2 = max(strike_price-root.val2, 0)
            print (root.val1, root.val2)
        else:
            dfs(root.left)
            dfs(root.right)

    def dfs1(root):
        if root.left is None:
            pass
            #print (root.val）
        else:
            root.val1 = dfs1(root.left)[0]*root.left.p + dfs1(root.right)[0]*root.right.p
            root.val2 = dfs1(root.left)[1]*root.left.p + dfs1(root.right)[1]*root.right.p
        return [root.val1, root.val2]

    root = Node(stock_price) 
    bfs(root,n_times)
    dfs(root)
    dfs1(root)
    
    #print (ans, ps)
    return (root.val1, root.val2)

stock_price = 100
strike_price = 100
var = 0.1
r_f = 0.03
n_times = 10
ttm = 1
CRR_model(stock_price, strike_price, var, r_f, ttm, m)
