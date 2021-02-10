# -----------------------------------------------------------
# pyRef_os.py
# v.1.0
# Updated: 20210210
# -----------------------------------------------------------

"""
Outline of operations using the os library.
"""

import os

# -----------------------------------------------------------
# DIRECTORY OPERATIONS }}}))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

# Get current working directory.
print os.getcwd()

# Delete file.
os.unlink('pathToFileToBeDeleted')
# Error outputs when run with no existing file to delete. This
# is a permanent delete operation.

# Delete directory.
os.rmdir('pathToDirToBeDeleted')
# Error outputs when run on non-empty dir. This is a permanent
# delete operation.

# -----------------------------------------------------------
# DIRECTORY OPERATIONS }}}))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------