from pathlib import PurePosixPath

root = PurePosixPath('/workspace')

def confined(path):
    p = PurePosixPath(path)
    if not p.is_absolute():
        p = root / p
    parts = p.parts
    return parts[:len(root.parts)] == root.parts and '..' not in parts

assert confined('/workspace/packages/a')
assert confined('packages/a')
assert not confined('/etc/passwd')
assert not confined('../outside')
print('formal_wave5_model: ok')
