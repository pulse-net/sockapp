import os
import tarfile

def tar_dir(dir_path):
    base_path = os.path.dirname(dir_path)
    dir_name = os.path.basename(dir_path)
    tarball_path = os.path.join(base_path, f"{dir_name}.tar.gz")

    with tarfile.open(tarball_path, "w:gz") as tar_file:
        for root, dirs, files in os.walk(dir_path):
            print(dirs)
            for file in files:
                tar_file.add(os.path.join(root, file), arcname=os.path.join(root.replace(base_path, "")[1:], file))

    return tarball_path

def get_file_dir_path(path):
    if os.path.isdir(path):
        path = tar_dir(dir_path=path)

    return path