def minimax(node, depth, maximizing, alpha, beta):
    if isinstance(node,int):  # leaf node
        return node
    if maximizing:
        value = -float('inf')
        for child in node:
            value = max(value, minimax(child, depth+1, False, alpha, beta))
            alpha = max(alpha,value)
            if beta <= alpha: break  # prune
        return value
    else:
        value = float('inf')
        for child in node:
            value = min(value, minimax(child, depth+1, True, alpha, beta))
            beta = min(beta,value)
            if beta <= alpha: break
        return value

# Example game tree
tree = [[3,5,6],[9,[1,2]]]
print("Best value for MAX:", minimax(tree,0,True,-float('inf'),float('inf')))
