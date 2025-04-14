def badgify(label,colour):
    if not label:
        label = 'Badge'
    if not colour:
        colour = 'white'
    print(f'{colour} | {label}')
    return f"<img src='https://img.shields.io/badge/{format(join([label,colours[colour]],'-'),'for-the-badge')}' alt='{label}'>"
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
badgeList =[
    ['Undead','purple']
]
def join(input,divider):
    return divider.join(str(x) for x in input if x)
def format(content,style):
    return f'{content}?style={style}'
with open('badge.md','w') as f:
    f.write('')
for i in range(badgeList.__len__()):
    with open('badge.md','a') as f:
        if badgeList[i] != '---':
            f.write(f'{badgify(badgeList[i][0],badgeList[i][1])}')
        else:
            f.write(f'{badgeList[i]}')
        f.write('\n\n')