def parse_path(path):
    if "\\" in path:
        path = path.replace("\\", "/")

    return path