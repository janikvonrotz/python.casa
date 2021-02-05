msg='1x1A1H1R1Y1J1S151g1H1o'
print(msg)

msg = msg[::-1][::2].replace('x', '0')

import webbrowser

youtube_id = msg
webbrowser.open('https://www.youtube.com/watch?v=%s' % (youtube_id))