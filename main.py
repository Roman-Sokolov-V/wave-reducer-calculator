import sys
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
)

from reducer.geometry import ReducerGeometry
from reducer.reduser_params import ReducerParams
from reducer.exeptions import TooSmallRequstedRadius

from services.reducervisualizer import ReducerVisualizer
from services.dxf_exporter import ReducerDXFExporter

from ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.reducer_geometry = None

        self.default_notification = (f"ball number = {self.ball_number.value()} - required\n"
                                   f"ball diameter = {self.ball_diameter.value()} - required\n"
                                   f"track outer radius = {self.track_outer_radius.value()} - if 0 value will be calculated (minimum possible) \n"
                                   f"reducer outer radius = {self.reducer_outer_diameter.value()} - if 0 will be calculated as track_outer_radius + 2 \n")
        self.to_small_track_outer_radius_notification = ("inputed track outer radius is too small\n"
                                                         "try to inputing biger number, or 0\n"
                                                         "or change ball diameter or ball number\n")


        self.exeption_hapened = False
        self.notifications.setText(self.default_notification)

        self.ball_number.valueChanged.connect(self.parameter_changed)
        self.ball_diameter.valueChanged.connect(self.parameter_changed)
        self.track_outer_radius.valueChanged.connect(self.parameter_changed)

        self.visualize_pushButton.setCheckable(True)
        self.export_pushButton.setCheckable(True)

        self.visualize_pushButton.clicked.connect(self.vizualize_button_clicked)
        self.export_pushButton.clicked.connect(self.export_push_button_clicked)


    def get_params(self) -> ReducerParams:
        print(f"{self.track_outer_radius.value()=}")
        print(f"{self.reducer_outer_diameter.value()=}")
        reducer_param = ReducerParams(
            gear_number=self.ball_number.value(),
            ball_diameter=self.ball_diameter.value(),
            requested_track_outer_radius=self.track_outer_radius.value() if self.track_outer_radius.value() != 0 else None,
            reducer_outer_diameter=self.reducer_outer_diameter.value() if self.reducer_outer_diameter.value() != 0 else None,
        )
        return reducer_param

    def clear_plot(self) -> None:
        layout = self.plotContainer.layout()
        if layout is None:
            return

        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def vizualize_button_clicked(self):
        if self.ball_number.value() == 0 or self.ball_diameter.value() == 0:
            self.notifications.setText("Input ball number and ball diameter")
            return
        try:
            self.reducer_geometry = ReducerGeometry(self.get_params())
            self.visualizer = ReducerVisualizer(self.reducer_geometry)
        except TooSmallRequstedRadius as e:
            print(str(e))
            self.notifications.setText(self.to_small_track_outer_radius_notification)
            self.exeption_hapened = True
            self.clear_plot()

        else:
            layout = self.plotContainer.layout()
            if layout is None:
                print("layout is None")
                layout = QVBoxLayout(self.plotContainer)

            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
            layout.addWidget(self.visualizer.canvas)
            self.visualizer.draw()



    def export_push_button_clicked(self):
        if self.reducer_geometry is None:
            self.notifications.setText("input parameters and make visualisation first")
            return

        export = ReducerDXFExporter(self.reducer_geometry)
        export.write_profiles_to_files(
            will_shape=self.checkBox_track.isChecked(),
            separator=self.checkBox_separator.isChecked(),
            eccentric=self.checkBox_eccentric.isChecked(),
        )
        self.notifications.setText("export done")


    def parameter_changed(self):
        if self.exeption_hapened:
            self.exeption_hapened = False
            self.notifications.setText(self.default_notification)



app = QApplication(sys.argv)
window = MainWindow()


if __name__ == "__main__":
    window.show()
    app.exec_()

