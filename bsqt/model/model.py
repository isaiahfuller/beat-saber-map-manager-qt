from PySide6.QtCore import QObject, Signal


class Model(QObject):
    latest_automapper_changed = Signal(bool)
    latest_verified_changed = Signal(int)

    @property
    def latest_automapper(self):
        return self._latest_automapper

    @latest_automapper.setter
    def latest_automapper(self, value):
        self._latest_automapper = value
        self.latest_automapper_changed.emit(value)

    @property
    def latest_verified(self):
        return self._latest_verified

    @latest_verified.setter
    def latest_verified(self, value):
        self._latest_verified = value
        self.latest_verified_changed.emit(value)

    def __init__(self):
        super().__init__()
