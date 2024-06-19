from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QDateTime
from bsqt.views.mainwindow_ui import Ui_MainWindow


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self._ui.latest_after_edit.setDateTime(QDateTime.currentDateTime().addDays(-7))
        self._ui.latest_after_edit.dateTimeChanged.connect(
            self._main_controller.latest_after
        )
        self._ui.latest_before_edit.setDateTime(QDateTime.currentDateTime())
        self._ui.latest_before_edit.dateTimeChanged.connect(
            self._main_controller.latest_before
        )
        self._ui.latest_automapper_checkbox.checkStateChanged.connect(
            self._main_controller.latest_automapper
        )
        self._ui.latest_verified_exclude.toggled.connect(
            self._main_controller.latest_verified_exclude
        )
        self._ui.latest_verified_include.toggled.connect(
            self._main_controller.latest_verified_include
        )
        self._ui.latest_verified_only.toggled.connect(
            self._main_controller.latest_verified_only
        )
        self._ui.latest_search_button.pressed.connect(
            self._main_controller.latest_search_button
        )
        self._model.latest_search_button_changed.connect(
            self._ui.latest_search_button.setDisabled
        )

        self._ui.latest_sort_cbox.currentIndexChanged.connect(
            self._main_controller.latest_sort_cbox
        )

        self._ui.latest_page_size.valueChanged.connect(
            self._main_controller.latest_page_size_spin
        )
