ModularMailer-PluginBase
========================

Description
-----------
Defines abstract base classes that all plugins for the ModularMailer project should subclass from. Currently this will define only the requirements for creating a table import driver plugin (a plugin that allows a specific file type to be read and imported into the application).

If the future, it is planned that more plugins will be defined for different purposes in the ModularMailer application, and this package will be update accordingly as these are defined.

Use
---
Subclass from the desired plugin base class::

    from mmpluginbase import FileDriverBase

    class FileDriver(FileDriverBase):

        def read(self, filename, *args, **kwargs):
            return True

Installation
------------
Installation should be as simple as installing from PyPI using pip::

    pip install ModularMailer-PluginBase

There are currently no requirements or dependencies for this package.
