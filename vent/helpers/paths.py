import errno
import os
import platform

from vent.api.templates import Template


class PathDirs:
    """ Global path directories for vent """
    def __init__(self,
                 base_dir=os.path.join(os.path.expanduser("~"), ".vent/"),
                 plugins_dir="plugins/",
                 meta_dir=os.path.join(os.path.expanduser("~"), ".vent")):
        self.base_dir = base_dir
        self.plugins_dir = base_dir + plugins_dir
        self.meta_dir = meta_dir
        self.init_file = base_dir+"vent.init"

        # make sure the paths exists, if not create them
        self.ensure_dir(self.base_dir)
        self.ensure_dir(self.plugins_dir)
        self.ensure_dir(self.meta_dir)

    @staticmethod
    def ensure_dir(path):
        """
        Tries to create directory, if fails, checks if path already exists
        """
        try:
            os.makedirs(path)
        except OSError as e:  # pragma: no cover
            if e.errno == errno.EEXIST and os.path.isdir(path):
                return (True, "exists")
            else:
                return (False, e)
        return (True, path)

    @staticmethod
    def ensure_file(path):
        """ Checks if file exists, if fails, tries to create file """
        try:
            exists = os.path.isfile(path)
            if not exists:
                with open(path, 'w+') as fname:
                    fname.write("initialized")
                return (True, path)
            return (True, "exists")
        except OSError as e:  # pragma: no cover
            return (False, e)

    def host_config(self):
        """ Ensure the host configuration file exists """
        if platform.system() == 'Darwin':
            default_file_dir = os.path.join(os.path.expanduser("~"),
                                            "vent_files")
        else:
            default_file_dir = "/tmp/vent_files"
        self.ensure_dir(default_file_dir)
        config = Template(template=os.path.join(self.base_dir, "vent.cfg"))
        sections = {'main': {'files': default_file_dir},
                    'network-mapping': {},
                    'nvidia-docker-plugin': {'port': '3476'}}
        for s in sections:
            if sections[s]:
                for option in sections[s]:
                    config.add_option(s, option, sections[s][option])
            else:
                config.add_section(s)
        config.write_config()
        return
