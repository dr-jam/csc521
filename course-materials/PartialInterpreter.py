import sys
import pprint

tree = ['Value0', ['Name1', 'SUB', 'IDENT:x']]

#start utilities
def lookup_in_scope_stack(name, scope):
    '''Returns values (including declared functions!)
    '''
    print(name in scope.keys())
    if name in scope:
        return scope[name]
    else:
        return lookup_in_scope_stack(name, scope["__parent__"])

def get_name_from_ident(tok):
    colon_index = tok.find(":")
    return tok[colon_index+1:]

def get_number_from_ident(tok):
    colon_index = tok.find(":")
    return float(tok[colon_index+1:])

def func_by_name(*args):
    name = args[0];
    pt = args[1]
    scope = args[2]
    name = globals()[name](pt, scope)
#end utilities

def SingleAssignment0(pt, scope):
    '''
    <SingleAssignment> -> VAR <Name> ASSIGN <Expression>
    '''
    name = func_by_name(pt[2][0], pt[2], scope)
    expression_value = func_by_name(pt[4][0], pt[4], scope)
    scope[name] = expression_value

def Value0(pt, scope, ):
    return func_by_name(pt[1][0], pt[1], scope)

def Value1(pt, scope):
    return func_by_name(pt[1][0], pt[1], scope)

def Name0(pt, scope):
    return lookup_in_scope_stack(get_name_from_ident(pt[1]), scope)

def Name1(pt, scope):
    return -lookup_in_scope_stack(get_name_from_ident(pt[2]), scope)

def Name2(pt, scope):
    return lookup_in_scope_stack(get_name_from_ident(pt[2]), scope)

def Number0(pt, scope):
    return get_number_from_ident(pt[1], scope)

def Number1(pt, scope):
    return -get_number_from_ident(pt[2], scope)

def Number(pt, scope):
    return get_number_from_ident(pt[2], scope)




if __name__ == '__main__':
    print("starting interpreter")
    print(func_by_name(tree[0], tree, {"x":4}))
