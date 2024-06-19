from PySide6.QtCore import QObject, Slot, Qt
import bsqt.utils.beatsaver.main as beatsaver


class MainController(QObject):
    def __init__(self, model, parent) -> None:
        super().__init__(parent=parent)
        self.load_maps = parent.load_maps
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
        # print(self._model._latest_after)
        # print(self._model._latest_before)
        # print(self._model._latest_automapper)
        # print(self._model._latest_sort)
        # print(self._model._latest_verified)
        maps = beatsaver.get_latest_maps(
            after=self._model._latest_after,
            before=self._model._latest_before,
            automapper=self._model._latest_automapper,
            sort=self._model._latest_sort,
            verified=self._model._latest_verified,
            page_size=self._model._latest_page_size,
        )
        # print(maps)
        self.load_maps(maps)
        self.s()
        # QTimer.singleShot(2000, lambda: self.s())

    @Slot(str)
    def latest_sort_cbox(self, value):
        self._model.latest_sort = value

    @Slot(int)
    def latest_page_size_spin(self, value):
        self._model.latest_page_size = value

    def s(self):
        self._model.latest_search_button = False
