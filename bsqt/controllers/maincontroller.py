from PySide6.QtCore import QObject, Slot, Qt


class MainController(QObject):
    def __init__(self, model) -> None:
        super().__init__()
        self._model = model

    @Slot(bool)
    def latest_automapper(self, value):
        if value == Qt.CheckState.Checked:
            self._model.latest_automapper = True
        if value != Qt.CheckState.Checked:
            self._model.latest_automapper = False

    @Slot(bool)
    def latest_verified_exclude(self, value):
        if value is True:
            self._model.latest_verified = False

    @Slot(bool)
    def latest_verified_include(self, value):
        if value is True:
            self._model.latest_verified = None

    @Slot(bool)
    def latest_verified_only(self, value):
        if value is True:
            self._model.latest_verified = True
