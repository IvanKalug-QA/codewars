# DESCRIPTION:
# On Unix system type files can be identified with the ls -l command which displays the type of the file in the first alphabetic letter of the file system permissions field.
# You can find more information about file type on Unix system on the wikipedia page.
#
# '-' A regular file ==> file.
# 'd' A directory ==> directory.
# 'l' A symbolic link ==> symlink.
# 'c' A character special file. It refers to a device that handles data as a stream of bytes (e.g: a terminal/modem) ==> character_file.
# 'b' A block special file. It refers to a device that handles data in blocks (e.g: such as a hard drive or CD-ROM drive) ==> block_file.
# 'p' a named pipe ==> pipe.
# 's' a socket ==> socket.
# 'D' a door ==> door.
# In this kata you should complete a function that return the filetype as a string regarding the file_attribute given by the ls -l command.
#
# For example if the function receive -rwxr-xr-x it should return file.

def linux_type(file_attribute):
    if file_attribute[0] == '-':
        return 'file'
    if file_attribute[0] == 'd':
        return 'directory'
    if file_attribute[0] == 'l':
        return 'symlink'
    if file_attribute[0] == 'c':
        return 'character_file'
    if file_attribute[0] == 'b':
        return 'block_file'
    if file_attribute[0] == 'p':
        return 'pipe'
    if file_attribute[0] == 's':
        return 'socket'
    if file_attribute[0] == 'D':
        return 'door'