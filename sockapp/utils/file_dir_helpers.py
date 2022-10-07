import os
import tarfile
from collections import namedtuple

from .error import InvalidStartingDirectory


def tar_dir(dir_path):
    base_path = os.path.dirname(dir_path)
    dir_name = os.path.basename(dir_path)
    tarball_path = os.path.join(base_path, f"{dir_name}.tar.gz")

    with tarfile.open(tarball_path, "w:gz") as tar_file:
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                tar_file.add(os.path.join(root, file), arcname=os.path.join(root.replace(base_path, "")[1:], file))

    return tarball_path

def get_file_dir_path(path):
    is_dir = False
    
    if(path[-1] == "/"):
        path = path[:-1]

    if os.path.isdir(path):
        is_dir = True
        path = tar_dir(dir_path=path)

    return path, is_dir

def untar_tarball(tarball_path):
    dir_name = os.path.basename(tarball_path)
    dir_name = dir_name.replace(".tar.gz", "")

    with tarfile.open(tarball_path) as tar_file:
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tar_file)

    os.remove(tarball_path)

def check_starting_directory(dir_path):
    if not os.path.exists(dir_path):
        raise InvalidStartingDirectory(message=f"Path {dir_path} does not exist!")

    if not os.path.isdir(dir_path):
        raise InvalidStartingDirectory(message=f"Path {dir_path} is not a directory!")