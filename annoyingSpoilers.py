# -------------------------- Description ---------------------------
# 
# Discord spoiler text generator
# Run the program then input your message.
# Spoilered message will be printed to terminal.
# Every letter is spoilered spearately so it is annoying to 
# unspoiler and read.
# Paste into discord chats to annoy people.
#
# ------------------------------------------------------------------

msg = input('Message: ')
res = ''
for i in msg:
    res += f'||{i}||'
print(res)
