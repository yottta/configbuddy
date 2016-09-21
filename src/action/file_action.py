#!/usr/bin/python
import os

from action import *
from common import *

class FileAction(BaseAction):

    def __init__(self, content):
        super(FileAction, self).__init__(content)

    def get_attrs_to_be_parsed(self):
        return ['destination']

    def get_command(self):
        command = self.get_attribute('command')
        file_name = self.get_full_path(Constants.get_instance().conf_dir + "/" + self.get_attribute('file_name'))
        destination = self.get_attribute('destination')
        command = "%s %s %s" % (command ,file_name, destination)
        return command

    def parse_content(self, content):
        for value in content:
            for file_name, properties in value.items():
                setattr(self, 'file_name', file_name)
                for prop_key, prop_val in properties[0].items():
                    setattr(self, prop_key, prop_val)
