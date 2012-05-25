import subprocess
from .mountutils import MountTable

class AlreadyMounted(Exception):
    pass

class FakeMountVerify(object):
    def is_mounted(self, *args):
        return False

class OverlayFS(object):
    @classmethod
    def mount(cls, mount_point, lower_dir, upper_dir, mount_table=None):
        """Execute the mount. This requires root"""
        # Load the mount table it isn't given
        if not mount_table:
            mount_table = MountTable.load()
        # Check if the mount_point is in use
        if mount_table.is_mounted(mount_point):
            # Throw an error if it is
            raise AlreadyMounted()
        # Build mount options
        options = "rw,lowerdir=%s,upperdir=%s" % (lower_dir, upper_dir)
        # Run the actual mount
        process = subprocess.Popen(['mount', '-t', 'overlayfs', '-o', options,
            'overlayfs', mount_point])
        # Wait for the mount to complete
        process.wait()
        return cls(mount_point, lower_dir, upper_dir)

    def unmount(self):
        process = subprocess.Popen(['umount', self.mount_point])
        process.wait()

    def __init__(self, mount_point, lower_dir, upper_dir):
        self.mount_point = mount_point
        self.lower_dir = lower_dir
        self.upper_dir = upper_dir
