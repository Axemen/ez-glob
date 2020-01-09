from finder import Finder
from pathlib import Path

# finder = Finder(Path(r'testing_dir'))

# """
# TESTING Finder.find_file_type()
# ==================================================================
# """
# assert finder.find_file_type('.pdf') == ['test1.pdf',
#                                         'test2.pdf',
#                                         'test1.pdf',
#                                         'test2.pdf',
#                                         'test1.pdf',
#                                         'test2.pdf',
#                                         'test1.pdf',
#                                         'test2.pdf']

# """
# TESTING Finder.find_directories()
# ==================================================================
# """
# assert finder.find_directories(['AFT']) == ['testing_dir\\AFT']
# assert finder.find_directories(['AFT', 'HRM']) == ['testing_dir\\AFT',
#                                                     'testing_dir\\HRM']

# """
# TESTING Finder.find_files()
# ==================================================================
# """
# assert finder.find_files() == ['test1.pdf',
#                                 'test1.txt',
#                                 'test2.pdf',
#                                 'test2.txt',
#                                 'test1.pdf',
#                                 'test1.txt',
#                                 'test2.pdf',
#                                 'test2.txt',
#                                 'test1.pdf',
#                                 'test1.txt',
#                                 'test2.pdf',
#                                 'test2.txt',
#                                 'test1.pdf',
#                                 'test1.txt',
#                                 'test2.pdf',
#                                 'test2.txt']

# """
# TESTING Finder.count_file_types()
# ==================================================================
# """
# assert finder.count_files_types() == {'pdf': 8, 'txt': 8}

# """
# TESTING Finder.count_files()
# ==================================================================
# """

# assert finder.count_files() is 16

# """
# TESTING Finder.count_directories()
# ==================================================================
# """
# assert finder.count_directories() == 12


# print('Success')



finder = Finder(r'A:\Projects\NA02\C646 - Gorgon LNG Project\Archive')

print(finder.find_file_type('.pdf'))