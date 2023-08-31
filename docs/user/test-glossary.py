def parse_tree(line):
    root = {'type': 'root', 'children': []}
    stack = [root]
    buffer = ''
    is_bold = False
    
    for c in line:
        if c == '*':
            if is_bold:
                is_bold = False
                stack[-1]['children'].append({'type': 'text', 'value': buffer})
                buffer = ''
                stack.pop()
            else:
                if buffer:
                    stack[-1]['children'].append({'type': 'text', 'value': buffer})
                buffer = ''
                new_node = {'type': 'bold', 'children': []}
                stack[-1]['children'].append(new_node)
                stack.append(new_node)
                is_bold = True
        else:
            buffer += c
            
    if buffer:
        stack[-1]['children'].append({'type': 'text', 'value': buffer})

    return root

def process_tree(node):
    if node['type'] == 'root':
        return ''.join(process_tree(child) for child in node['children'])
    elif node['type'] == 'text':
        text = node['value']
        terms = []
        while ':term:' in text:
            pre, post = text.split(':term:', 1)
            term, post = post.split('`', 1)
            term = ':term:`' + term + '`'
            terms.append(pre)
            terms.append(term)
            text = post
        terms.append(text)
        return ''.join(terms)
    elif node['type'] == 'bold':
        return '**' + ''.join(process_tree(child) for child in node['children']).strip() + '**'

# Test the function
test_lines = [
    "2) **Fill in Case Name in :term:`Case Information` and also**",
    "**Select :term:`Data Source` Type as \":term:`Disk Image or VM File`\"**",
    "2) **Fill in Case Name in :term:`Case Information`**",
    "2) **:term:`Case Information`**",
    "2) **:term:`Case Information` more info**"
]

for line in test_lines:
    tree = parse_tree(line)
    fixed_line = process_tree(tree)
    print(f"Original line: {line}")
    print(f"Fixed line:    {fixed_line}")
