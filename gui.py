import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from core import *
from qt_material import apply_stylesheet

class air_gui_demo(QWidget):
    def __init__(self):
        # init gui
        super(air_gui_demo, self).__init__()
        # main window set
        self.resize(1440,900)
        self.setWindowTitle('城市空气质量查询器')
        
        # AQI information query
        self.air_info = air_quality()

        # label init
        self.setStyleSheet(
                   "QLabel{color:rgb(255,255,70,120);font-size:20px;font-weight:bold;font-family:Roman times;}"
                   "QLabel:hover{color:rgb(255,255,70,250);}")

        self.l_1 = QLabel(self)
        self.l_1.setGeometry(150,30,1100,50)
        self.l_1.setText("aqi指数:")

        self.l_2 = QLabel(self)
        self.l_2.setGeometry(150,80,1100,50)
        self.l_2.setText("数据来源url:")

        self.l_3 = QLabel(self)
        self.l_3.setGeometry(150,130,1100,50)
        self.l_3.setText("测量机构:")

        self.l_4 = QLabel(self)
        self.l_4.setGeometry(150,180,500,50)
        self.l_4.setText("城市:")

        self.l_5 = QLabel(self)
        self.l_5.setGeometry(150,230,500,50)
        self.l_5.setText("经纬度:")

        self.l_6 = QLabel(self)
        self.l_6.setGeometry(150,280,500,50)
        self.l_6.setText("测量时间:")

        self.l_7 = QLabel(self)
        self.l_7.setGeometry(150,330,500,50)
        self.l_7.setText("空气湿度:")

        self.l_8 = QLabel(self)
        self.l_8.setGeometry(150,380,500,50)
        self.l_8.setText("大气压:")

        self.l_9 = QLabel(self)
        self.l_9.setGeometry(150,430,500,50)
        self.l_9.setText("温度:")

        self.l_10 = QLabel(self)
        self.l_10.setGeometry(150,480,500,50)
        self.l_10.setText("风力:")

        self.l_11 = QLabel(self)
        self.l_11.setGeometry(800,180,500,50)
        self.l_11.setText("co浓度:")

        self.l_12 = QLabel(self)
        self.l_12.setGeometry(800,230,500,50)
        self.l_12.setText("no2浓度:")

        self.l_13 = QLabel(self)
        self.l_13.setGeometry(800,280,500,50)
        self.l_13.setText("o3浓度:")

        self.l_14 = QLabel(self)
        self.l_14.setGeometry(800,330,500,50)
        self.l_14.setText("so2浓度:")

        self.l_15 = QLabel(self)
        self.l_15.setGeometry(800,380,500,50)
        self.l_15.setText("pm2.5浓度:")

        self.l_16 = QLabel(self)
        self.l_16.setGeometry(800,430,500,50)
        self.l_16.setText("pm10浓度:")

        self.l_17 = QLabel(self)
        self.l_17.setGeometry(800,480,500,50)
        self.l_17.setText("不同信息源提供指标不同，-1代表未查到数据")

        # button1 init
        self.btn1 = QPushButton(self)
        self.btn1.setGeometry(150,600,150,50)
        self.btn1.setText('获取aqi信息')
        self.btn1.clicked.connect(self.btn1_click)

    def btn1_click(self):
        # button1 reflection
        text, ok = QInputDialog.getText(self, "dialog", "输入城市名")
        if ok and text and self.air_info.info_get(text):
            # succeed
            self.l_1.setText("aqi指数:"+str(self.air_info.data_aqi_current)+" "+\
                             aqi_classify(self.air_info.data_aqi_current))
            self.l_2.setText("数据来源url:"+self.air_info.data_source_url)
            self.l_3.setText("测量机构:"+self.air_info.data_source_organization)
            self.l_4.setText("城市:"+self.air_info.data_city_name)
            self.l_5.setText("经纬度:"+"("+str(self.air_info.data_city_location[1])+","+\
                             str(self.air_info.data_city_location[0])+")")
            self.l_6.setText("测量时间:"+self.air_info.data_time_current)
            self.l_7.setText("空气湿度:"+str(self.air_info.data_humidity_current)+"%")
            self.l_8.setText("大气压:"+str(self.air_info.data_pressure_current)+"百帕")
            self.l_9.setText("温度:"+str(self.air_info.data_t_current)+"摄氏度")
            self.l_10.setText("风力:"+str(self.air_info.data_wind_current)+"级")
            self.l_11.setText("co浓度:"+str(self.air_info.data_co_current)+"mg/m3")
            self.l_12.setText("no2浓度:"+str(self.air_info.data_no2_current)+"μg/m3")
            self.l_13.setText("o3浓度:"+str(self.air_info.data_o3_current)+"μg/m3")
            self.l_14.setText("so2浓度:"+str(self.air_info.data_so2_current)+"μg/m3")
            self.l_15.setText("pm2.5浓度:"+str(self.air_info.data_pm25_current)+"μg/m3")
            self.l_16.setText("pm10浓度:"+str(self.air_info.data_pm10_current)+"μg/m3")
            
        else :
            # fail
            QMessageBox.warning(self, "warning", "未查询到相关信息", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        return 



if __name__ == "__main__":
    app =QApplication(sys.argv)
    widget = air_gui_demo()
    apply_stylesheet(app, theme='dark_yellow.xml')
    widget.show()
    sys.exit(app.exec_())