import os
'''print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))'''

# templates
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print(BASE_DIR)
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
print(TEMPLATE_DIR)
