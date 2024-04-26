# Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
try:
    a = open('file', 'w')
    b = a.read()
    print("file contents:", b)
except:
    raise PermissionError('Permissionissue')