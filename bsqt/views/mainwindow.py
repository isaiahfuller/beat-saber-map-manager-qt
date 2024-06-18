from PySide6.QtWidgets import QMainWindow
from bsqt.views.mainwindow_ui import Ui_MainWindow


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

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
