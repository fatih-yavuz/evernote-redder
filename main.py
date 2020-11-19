from richxerox import pasteboard

try:
    html = pasteboard.get_contents(format='html')
    text = pasteboard.get_contents(format='text')
    html = html.replace(text, f'<span style="color:rgb(255, 0, 42)">{text}</span>')
    pasteboard.set_contents(html=html)
except Exception as e:
    pass
