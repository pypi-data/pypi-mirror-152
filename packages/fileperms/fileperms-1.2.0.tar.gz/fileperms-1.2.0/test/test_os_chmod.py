import itertools
import os
import stat
import tempfile

from fileperms import Permissions


class TestOsChmod:
    def test(self):
        perms = '0 1 2 3 4 5 6 7'.split()
        path = tempfile.mkstemp()[1]

        try:
            perms = itertools.product(perms, perms, perms, perms)
            for item in perms:
                item = ''.join(item)
                assert len(item) == 4

                prm = Permissions.from_octal(item)
                os.chmod(path, int(prm))

                assert stat.filemode(os.stat(path).st_mode)[1:] == prm.to_filemode()
        finally:
            os.unlink(path)
