import abc


class FileDriverBase(abc.ABC):

    def onLoad(self):
        pass

    @abc.abstractmethod
    def read(self, filename, **kwargs):
        pass
