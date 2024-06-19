import sys
from datetime import datetime
from PySide6 import QtWidgets
from bsqt.model.model import Model
from bsqt.controllers.maincontroller import MainController
from bsqt.views.mainwindow import MainView


class App(QtWidgets.QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = Model()
        self.main_controller = MainController(self.model, parent=self)
        self.main_view = MainView(self.model, self.main_controller)
        self.main_view.show()

    def load_maps(self, map_info):
        map_list = self.main_view._ui.map_tree
        map_list.clear()
        map_list.setHeaderLabels(["Name", "Mapper", "Date"])
        print(map_info)
        idx = 0
        for m in map_info:
            uploaded_date = datetime.strptime(
                m["uploaded"].split(".")[0], "%Y-%m-%dT%H:%M:%S"
            )
            map_list.addTopLevelItem(
                QtWidgets.QTreeWidgetItem(
                    [
                        m["name"],
                        m["uploader"]["name"],
                        uploaded_date.strftime("%m/%d/%Y %H:%M"),
                    ]
                )
            )
            map_list.resizeColumnToContents(idx)
            idx += 1


if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec())
