# Functions
def join(input,divider):
    return divider.join(str(x) for x in input if x)
def format(content,style):
    return f'{content}?style={style}'
# Lists/Dictionaries
colours = {
    'white':'fff',
    'grey':'888',
    'black':'000',
    'red':'f00',
    'orange':'f80',
    'yellow':'ff0',
    'green':'0f0',
    'blue':'00f',
    'purple':'80f',
    'pink':'f0f'
    }
# Variables
label = 'Example'
colour = colours['white']
style = 'for-the-badge'
# Formatting
content = join([label,colour],'-')
output = f'![Static Badge](https://img.shields.io/badge/{format(content,style)})'
# Output
with open('badge.md','w') as f:
    f.write(output)