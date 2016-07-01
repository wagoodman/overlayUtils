from .overlay import OverlayFS, OverlayFSManager, OverlayFSDoesNotExist

def mount(directory, lower_dir, upper_dir, mount_table=None):
    return OverlayFS.mount(directory, lower_dir, upper_dir,
            mount_table=mount_table)

def umount(directory):
    return OverlayFS.umount(directory)

def list(mount_table=None):
    return OverlayFSManager.list(mount_table=mount_table)

def get(mount_point, mount_table=None):
    return OverlayFSManager.get(mount_point, mount_table=mount_table)
