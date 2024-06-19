from PySide6.QtCore import QObject, Signal, QDateTime


class Model(QObject):
    latest_after_changed = Signal(str)
    latest_automapper_changed = Signal(bool)
    latest_before_changed = Signal(str)
    latest_verified_changed = Signal(int)
    latest_search_button_changed = Signal(bool)
    latest_sort_changed = Signal(str)
    latest_page_size_changed = Signal(int)

    @property
    def latest_after(self):
        return self._latest_after

    @latest_after.setter
    def latest_after(self, value):
        self._latest_after = value
        self.latest_after_changed.emit(value)

    @property
    def latest_before(self):
        return self._latest_after

    @latest_before.setter
    def latest_before(self, value):
        self._latest_before = value
        self.latest_before_changed.emit(value)

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

    @property
    def latest_search_button(self):
        return self._latest_search_button

    @latest_search_button.setter
    def latest_search_button(self, value):
        self._search_button = value
        self.latest_search_button_changed.emit(value)

    @property
    def latest_sort(self):
        return self._latest_sort

    @latest_sort.setter
    def latest_sort(self, value):
        self._latest_sort = value
        self.latest_sort_changed.emit(value)

    @property
    def latest_page_size(self):
        return self._latest_page_size

    @latest_page_size.setter
    def latest_page_size(self, value):
        self._latest_page_size = value
        self.latest_page_size_changed.emit(value)

    def __init__(self):
        super().__init__()
        self._latest_after = (
            QDateTime.currentDateTime()
            .addDays(-7)
            .toUTC()
            .toPython()
            .strftime("%Y-%m-%dT%H:%M:%S")
            + "+00:00"
        )
        self._latest_before = (
            QDateTime.currentDateTime().toUTC().toPython().strftime("%Y-%m-%dT%H:%M:%S")
            + "+00:00"
        )
        self._latest_automapper = False
        self._latest_page_size = 20
        self._latest_sort = 0
        self._latest_verified = None
