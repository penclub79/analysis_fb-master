s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""
s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""
s = s.replace("""
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>""","""

    
        Click
        Here
        
        	To connect to the most powerful tools in the world.
</html>""")
print(s)







     # s = s.split('\n')[1].split('<')[2].split('>')



# s = s.upper().replace(',', "").replace('.', "").replace('\n', "")



# states = ['Alabama', ' Georgia!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina   ', 'West virginia?']
#
#
# def clean_strings(strings, *funcs):
#     results = []
#     for string in strings:
#         for func in funcs:
#             string = func(string)
#         results.append(string)
#     return results
#
#
# states = clean_strings(states, str.strip, str.title)
# print(states)
