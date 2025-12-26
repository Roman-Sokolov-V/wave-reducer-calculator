import sys

from PySide6 import QtWidgets
from reducer.geometry import ReducerGeometry
from reducer.reduser_params import ReducerParams
from ui.ui_main_window import Ui_MainWindow

from services.reducervisualizer import ReducerVisualizer
from services.dxf_exporter import ReducerDXFExporter


#
# reducer_param = ReducerParams(
#     gear_number=5,
#     ball_diameter=12,
#     #requested_outer_radius=50,
#     #reducer_outer_diameter = 70
#
# )
#
# reducer_geometry = ReducerGeometry(reducer_param)
#
# print(reducer_geometry)
# print(reducer_geometry.gear_number)
# print(reducer_geometry.ball_diameter)
# print(reducer_geometry.requested_outer_radius)
# #print(reducer_geometry.reducer_outer_diameter)
# print(reducer_geometry.resolution)
# print(reducer_geometry.eccentricity)
# print(reducer_geometry.number_of_waves)
# print(reducer_geometry.min_inner_radius)
# print(reducer_geometry.balls_radius)
# print(reducer_geometry.separator_thickness)
# print(reducer_geometry.track_outer_radius)
# print(f"{reducer_geometry.track_inner_radius=}")
# print(f"{reducer_geometry.eccentric_radius=}")
# print(f"{reducer_geometry.radius_of_separator_outer=}")
# print(f"{reducer_geometry.radius_of_separator_inner=}")
# print(f"{reducer_geometry.xy=}")
# print(f"{reducer_geometry.stacked_xy=}")
# print(f"{reducer_geometry.balls_centers=}")
#
#
# visualisation = ReducerVisualizer(reducer_geometry)
# dxf = ReducerDXFExporter(reducer_geometry)
#
#
# dxf.write_profiles_to_files()
# visualisation.show(separator=False, eccentric=False)



reducer_param = ReducerParams()

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.visualize_pushButton.setCheckable(True)
        self.export_pushButton.setCheckable(True)

        self.visualize_pushButton.clicked.connect(self.vizualize_button_clicked)
        self.export_pushButton.clicked.connect(self.export_pushButton_clicked)

    def vizualize_button_clicked(self):
        print("Clicked")

    def export_pushButton_clicked(self):
        print("Clicked")


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()


