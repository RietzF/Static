from textnode import *
nodes = [TextNode("This is text with a `code block` word", TextType.NORMAL)]
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        
        split_nodes = []
        sections = old_node.text.split(delimiter)
        
        # Check for valid markdown - odd number of sections means we have paired delimiters
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        
        for i in range(len(sections)):
            if sections[i] == "" and (i == 0 or i == len(sections) - 1):
                # Skip empty first or last section
                continue
            
            # Even-indexed sections are normal text, odd-indexed are specially formatted
            current_type = TextType.NORMAL if i % 2 == 0 else text_type
            split_nodes.append(TextNode(sections[i], current_type))
        
        new_nodes.extend(split_nodes)
    
    return new_nodes


