import os


def getFilesPaths(path, extensions):
    files = []
    for root, directories, file_names in os.walk(unicode(path)):
        for filename in file_names:
            if (extensions and filename.endswith(tuple(["." + ext for ext in extensions]))) or (extensions is None):
                files.append(os.path.join(root, filename))
    return files


def separatePathsAndFilesNameAndExt(files):
    return [("\\".join(os.path.splitext(f)[0].split('\\')[: -1]), os.path.splitext(f)[0].split('\\')[-1],
             os.path.splitext(f)[1]) for f in files]
