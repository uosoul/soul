# 泛型的递归模板，

def recursion(level,param1,param2,...):
    # recursion terminator
    if level > max_level:
        process_result
        return

    # process logic in current level
    process(level,data..)

    # drill down
    self.recursion(level+1,p1,...)

    # reverse the current level status if needed
