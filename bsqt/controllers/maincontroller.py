from PySide6.QtCore import QObject, Slot, Qt, QTimer
from bsqt.utils.beatsaver.enums import BeatSaverLatestSort


class MainController(QObject):
    def __init__(self, model) -> None:
        super().__init__()
        self._model = model

    @Slot(str)
    def latest_after(self, value):
        print(value.toUTC().toPython().strftime("%Y-%m-%dT%H:%M:%S") + "+00:00")
        self._model.latest_after = (
            value.toUTC().toPython().strftime("%Y-%m-%dT%H:%M:%S") + "+00:00"
        )

    @Slot(str)
    def latest_before(self, value):
        print(value.toUTC().toPython().strftime("%Y-%m-%dT%H:%M:%S") + "+00:00")
        self._model.latest_before = (
            value.toUTC().toPython().strftime("%Y-%m-%dT%H:%M:%S") + "+00:00"
        )

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

    @Slot(bool)
    def latest_search_button(self):
        self._model.latest_search_button = True
        QTimer.singleShot(2000, lambda: self.s())

    @Slot(str)
    def latest_sort_cbox(self, value):
        self._model.latest_sort = BeatSaverLatestSort(value + 1).name

    def s(self):
        self._model.latest_search_button = False
