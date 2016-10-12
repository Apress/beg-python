# Prints a sentence in a centered "box" of correct width

# Note that the integer division operator (//) only works in Python
# 2.2 and newer. In earlier versions, simply use plain division (/)


sentence = raw_input("Sentence: ")

screen_width = 80
text_width   = len(sentence)
box_width    = text_width + 6
left_margin  = (screen_width - box_width) // 2

print
print ' ' * left_margin + '+'   + '-' * (box_width-2)  +   '+'
print ' ' * left_margin + '|  ' + ' ' * text_width     + '  |'
print ' ' * left_margin + '|  ' +       sentence       + '  |'
print ' ' * left_margin + '|  ' + ' ' * text_width     + '  |'
print ' ' * left_margin + '+'   + '-' * (box_width-2)  +   '+'
print