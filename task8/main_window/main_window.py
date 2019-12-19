from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from math import exp, sin

from tables import main_table

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.task_swith = QtWidgets.QTabWidget(self.centralwidget)
        self.task_swith.setObjectName("task_swith")
        self.main_tab = QtWidgets.QWidget()
        self.main_tab.setObjectName("main_tab")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.main_tab)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.main_task = QtWidgets.QTabWidget(self.main_tab)
        self.main_task.setObjectName("main_task")
        self.main_task_tab = QtWidgets.QWidget()
        self.main_task_tab.setObjectName("main_task_tab")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.main_task_tab)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.main_description = QtWidgets.QTextEdit(self.main_task_tab)
        self.main_description.setReadOnly(True)
        self.main_description.setObjectName("main_description")
        self.gridLayout_10.addWidget(self.main_description, 2, 1, 1, 1)
        self.main_start_values = QtWidgets.QGroupBox(self.main_task_tab)
        self.main_start_values.setTitle("")
        self.main_start_values.setObjectName("main_start_values")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.main_start_values)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.main_koshi_task = QtWidgets.QGroupBox(self.main_start_values)
        self.main_koshi_task.setObjectName("main_koshi_task")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.main_koshi_task)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.main_x0_label = QtWidgets.QLabel(self.main_koshi_task)
        self.main_x0_label.setObjectName("main_x0_label")
        self.gridLayout_12.addWidget(self.main_x0_label, 0, 0, 1, 1)
        self.main_x0_input = QtWidgets.QLineEdit(self.main_koshi_task)
        self.main_x0_input.setObjectName("main_x0_input")
        self.gridLayout_12.addWidget(self.main_x0_input, 0, 1, 1, 1)
        self.main_u0_label = QtWidgets.QLabel(self.main_koshi_task)
        self.main_u0_label.setObjectName("main_u0_label")
        self.gridLayout_12.addWidget(self.main_u0_label, 1, 0, 1, 1)
        self.main_u0_input = QtWidgets.QLineEdit(self.main_koshi_task)
        self.main_u0_input.setObjectName("main_u0_input")
        self.gridLayout_12.addWidget(self.main_u0_input, 1, 1, 1, 1)
        self.gridLayout_11.addWidget(self.main_koshi_task, 1, 0, 1, 1)
        self.main_start = QtWidgets.QPushButton(self.main_start_values)
        self.main_start.setObjectName("main_start")
        self.main_start.clicked.connect(self.main_calculate)
        self.gridLayout_11.addWidget(self.main_start, 2, 0, 1, 1)
        self.main_alghoritm_params = QtWidgets.QGroupBox(self.main_start_values)
        self.main_alghoritm_params.setObjectName("main_alghoritm_params")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.main_alghoritm_params)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.main_niter_label = QtWidgets.QLabel(self.main_alghoritm_params)
        self.main_niter_label.setObjectName("main_niter_label")
        self.gridLayout_13.addWidget(self.main_niter_label, 0, 0, 1, 1)
        self.main_right_break_label = QtWidgets.QLabel(self.main_alghoritm_params)
        self.main_right_break_label.setObjectName("main_right_break_label")
        self.gridLayout_13.addWidget(self.main_right_break_label, 1, 0, 1, 1)
        self.main_epsilon_label = QtWidgets.QLabel(self.main_alghoritm_params)
        self.main_epsilon_label.setObjectName("main_epsilon_label")
        self.gridLayout_13.addWidget(self.main_epsilon_label, 3, 0, 1, 1)
        self.main_q1_label = QtWidgets.QLabel(self.main_alghoritm_params)
        self.main_q1_label.setObjectName("main_q1_label")
        self.gridLayout_13.addWidget(self.main_q1_label, 4, 0, 1, 1)
        self.main_q2_label = QtWidgets.QLabel(self.main_alghoritm_params)
        self.main_q2_label.setObjectName("main_q2_label")
        self.gridLayout_13.addWidget(self.main_q2_label, 5, 0, 1, 1)
        self.main_barrier_label = QtWidgets.QLabel(self.main_alghoritm_params)
        self.main_barrier_label.setObjectName("main_barrier_label")
        self.gridLayout_13.addWidget(self.main_barrier_label, 6, 0, 1, 1)
        self.main_h0_label = QtWidgets.QLabel(self.main_alghoritm_params)
        self.main_h0_label.setObjectName("main_h0_label")
        self.gridLayout_13.addWidget(self.main_h0_label, 2, 0, 1, 1)
        self.main_niter_input = QtWidgets.QLineEdit(self.main_alghoritm_params)
        self.main_niter_input.setObjectName("main_niter_input")
        self.gridLayout_13.addWidget(self.main_niter_input, 0, 1, 1, 1)
        self.main_right_break_input = QtWidgets.QLineEdit(self.main_alghoritm_params)
        self.main_right_break_input.setObjectName("main_right_break_input")
        self.gridLayout_13.addWidget(self.main_right_break_input, 1, 1, 1, 1)
        self.main_h0_input = QtWidgets.QLineEdit(self.main_alghoritm_params)
        self.main_h0_input.setObjectName("main_h0_input")
        self.gridLayout_13.addWidget(self.main_h0_input, 2, 1, 1, 1)
        self.main_epsilon_input = QtWidgets.QLineEdit(self.main_alghoritm_params)
        self.main_epsilon_input.setObjectName("main_epsilon_input")
        self.gridLayout_13.addWidget(self.main_epsilon_input, 3, 1, 1, 1)
        self.main_q1_input = QtWidgets.QLineEdit(self.main_alghoritm_params)
        self.main_q1_input.setObjectName("main_q1_input")
        self.gridLayout_13.addWidget(self.main_q1_input, 4, 1, 1, 1)
        self.main_q2_input = QtWidgets.QLineEdit(self.main_alghoritm_params)
        self.main_q2_input.setObjectName("main_q2_input")
        self.gridLayout_13.addWidget(self.main_q2_input, 5, 1, 1, 1)
        self.main_barrier_input = QtWidgets.QLineEdit(self.main_alghoritm_params)
        self.main_barrier_input.setObjectName("main_barrier_input")
        self.gridLayout_13.addWidget(self.main_barrier_input, 6, 1, 1, 1)
        self.gridLayout_11.addWidget(self.main_alghoritm_params, 1, 1, 1, 1)
        self.gridLayout_10.addWidget(self.main_start_values, 2, 0, 1, 1)
        self.main_graphics_box = QtWidgets.QGroupBox(self.main_task_tab)
        self.main_graphics_box.setObjectName("main_graphics_box")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.main_graphics_box)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.main_figure = Figure()
        self.main_graphic = FigureCanvas(self.main_figure)
        self.main_ax = self.main_figure.add_subplot(111)
        #self.main_graphic = QtWidgets.QGraphicsView(self.main_graphics_box)
        self.main_graphic.setObjectName("main_graphic")
        self.gridLayout_14.addWidget(self.main_graphic, 1, 0, 1, 1)
        self.gridLayout_10.addWidget(self.main_graphics_box, 3, 0, 1, 2)
        self.main_task.addTab(self.main_task_tab, "")
        self.main_table_tab = QtWidgets.QWidget()
        self.main_table_tab.setObjectName("main_table_tab")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.main_table_tab)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.main_table = main_table.main_table(self.main_table_tab)
        self.main_table.setObjectName("main_table")
        self.gridLayout_15.addWidget(self.main_table, 0, 0, 1, 1)
        self.main_task.addTab(self.main_table_tab, "")
        self.gridLayout_17.addWidget(self.main_task, 0, 0, 1, 1)
        self.task_swith.addTab(self.main_tab, "")
        self.info_tab = QtWidgets.QWidget()
        self.info_tab.setObjectName("info_tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.info_tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.info = QtWidgets.QTextEdit(self.info_tab)
        self.info.setReadOnly(True)
        self.info.setObjectName("info")
        self.gridLayout_5.addWidget(self.info, 0, 0, 1, 1)
        self.task_swith.addTab(self.info_tab, "")
        self.gridLayout.addWidget(self.task_swith, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.task_swith.setCurrentIndex(0)
        self.main_task.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Численные методы. Задача 8. Решение ДУ методом РК 4 порядка"))
        self.main_description.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Описание задачи</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Рассматривается дифференциальное уравнение:</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">du/dx = 0.25(Q</span><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\">1</span><span style=\" font-size:12pt; font-weight:600;\"> - Q</span><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\">2</span><span style=\" font-size:12pt; font-weight:600;\">); u(x</span><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\">0</span><span style=\" font-size:12pt; font-weight:600;\">) = u</span><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\">0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">где <span style=\" font-weight:600;\">Q</span><span style=\" font-weight:600; vertical-align:sub;\">1</span> - количество энергии, выделяемая нагревателем,<br /><span style=\" font-weight:600;\">Q</span><span style=\" font-weight:600; vertical-align:sub;\">2</span> - потери энергии в окружающую среду,<br /><span style=\" font-weight:600;\">u(x)</span> - температура в момент времени <span style=\" font-weight:600;\">x</span>.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Устанавливается значение <span style=\" font-weight:600;\">u</span><span style=\" font-weight:600; vertical-align:sub;\">b</span> , после достижения которого подача тепла прекращается (<span style=\" font-weight:600;\">Q</span><span style=\" font-weight:600; vertical-align:sub;\">1</span><span style=\" font-weight:600;\"> = 0</span>). Подача тепла возобнавляется, когда значение <span style=\" font-weight:600;\">u(x)</span> снова станет меньше значения <span style=\" font-weight:600;\">u</span><span style=\" font-weight:600; vertical-align:sub;\">b </span>.</p></body></html>"))
        self.main_koshi_task.setTitle(_translate("MainWindow", "Задача Коши"))
        self.main_x0_label.setText(_translate("MainWindow", "<html><head/><body><p>x<span style=\" vertical-align:sub;\">0</span></p></body></html>"))
        self.main_x0_input.setText(_translate("MainWindow", "0"))
        self.main_u0_label.setText(_translate("MainWindow", "<html><head/><body><p>u<span style=\" vertical-align:sub;\">0</span></p></body></html>"))
        self.main_u0_input.setText(_translate("MainWindow", "0"))
        self.main_start.setText(_translate("MainWindow", "Численно вычислить"))
        self.main_alghoritm_params.setTitle(_translate("MainWindow", "Параметры алгоритма"))
        self.main_niter_label.setText(_translate("MainWindow", "Количество итераций"))
        self.main_right_break_label.setText(_translate("MainWindow", "Правая граница"))
        self.main_epsilon_label.setText(_translate("MainWindow", "Контроль локальной погрешности"))
        self.main_q1_label.setText(_translate("MainWindow", "Q1"))
        self.main_q2_label.setText(_translate("MainWindow", "Q2"))
        self.main_barrier_label.setText(_translate("MainWindow", "Барьер"))
        self.main_h0_label.setText(_translate("MainWindow", "Шаг интегрирования"))
        self.main_niter_input.setText(_translate("MainWindow", "1000"))
        self.main_right_break_input.setText(_translate("MainWindow", "100"))
        self.main_h0_input.setText(_translate("MainWindow", "0.001"))
        self.main_epsilon_input.setText(_translate("MainWindow", "0"))
        self.main_q1_input.setText(_translate("MainWindow", "30000"))
        self.main_q2_input.setText(_translate("MainWindow", "500"))
        self.main_barrier_input.setText(_translate("MainWindow", "22"))
        self.main_graphics_box.setTitle(_translate("MainWindow", "График"))
        self.main_task.setTabText(self.main_task.indexOf(self.main_task_tab), _translate("MainWindow", "Задача"))
        self.main_task.setTabText(self.main_task.indexOf(self.main_table_tab), _translate("MainWindow", "Таблица"))
        self.task_swith.setTabText(self.task_swith.indexOf(self.main_tab), _translate("MainWindow", "Основная задача"))
        self.task_swith.setTabText(self.task_swith.indexOf(self.info_tab), _translate("MainWindow", "Справка"))
        self.info.setHtml("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Максимальная оценка локальной погрешности: </span><span style=" font-size:14pt; font-weight:600;">0</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Максимальный шаг: </span><span style=" font-size:14pt; font-weight:600;">0</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Минимальный шаг: </span><span style=" font-size:14pt; font-weight:600;">0</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Количество раз, когда шаг увеличивался: </span><span style=" font-size:14pt; font-weight:600;">0</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Количество раз, когда шаг уменьшался: </span><span style=" font-size:14pt; font-weight:600;">0</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Количество итераций: </span><span style=" font-size:14pt; font-weight:600;">0</span></p></body></html>""")

    def get_stats(self, s_list : list, h_list : list, c1_list : list, c2_list : list):
        number_iter = len(s_list)
        max_s = s_list[0]
        max_h = h_list[0]
        min_h = h_list[0]
        c1_count = 0
        c2_count = 0
        for i in range(number_iter):
            max_s = max(max_s, s_list[i])
            max_h = max(max_h, h_list[i])
            min_h = min(min_h, h_list[i])
            c1_count += c1_list[i]
            c2_count += c2_list[i]
        return max_s, max_h, min_h, c1_count, c2_count, number_iter

    def update_info(self, max_s : float, max_h : float, min_h : float, c1 : int, c2 : int, iter_count : int):
        self.info.setHtml("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Максимальная оценка локальной погрешности: </span><span style=" font-size:14pt; font-weight:600;">""" + str(max_s) +"""</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Максимальный шаг: </span><span style=" font-size:14pt; font-weight:600;">""" + str(max_h) + """</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Минимальный шаг: </span><span style=" font-size:14pt; font-weight:600;">""" + str(min_h) + """</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Количество раз, когда шаг увеличивался: </span><span style=" font-size:14pt; font-weight:600;">""" + str(c2) + """</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Количество раз, когда шаг уменьшался: </span><span style=" font-size:14pt; font-weight:600;">""" + str(c1) + """</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Количество итераций: </span><span style=" font-size:14pt; font-weight:600;">""" + str(iter_count - 1) + """</span></p></body></html>""")

    def plot(self, graphic, ax, x_list : list, v_list : list):
        ax.clear()
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid(True)
        ax.plot(x_list, v_list, label = "Численное решение")
        ax.legend()
        graphic.draw()
    
    def parse_main_start_values(self):
        x0 = float(self.main_x0_input.text())
        u0 = float(self.main_u0_input.text())
        niter = int(self.main_niter_input.text())
        right_break = float(self.main_right_break_input.text())
        h0 = float(self.main_h0_input.text())
        epsilon = float(self.main_epsilon_input.text())
        q1 = int(self.main_q1_input.text())
        q2 = int(self.main_q2_input.text())
        barrier = int(self.main_barrier_input.text())
        return x0, u0, niter, right_break, h0, epsilon, q1, q2, barrier

    def f_main(self, x : float, v : float, q1 : int, q2 : int):
        return 0.25 * (q1 - q2)

    def k1(self, x : float, v : float, h : float, q1 : int, q2 : int, f):
        return f(x, v, q1, q2)
    
    def k2(self, x : float, v : float, h : float, k1 : float, q1 : int, q2 : int, f):
        return f(x + h / 2, v + k1 * h / 2, q1, q2)

    def k3(self, x : float, v : float, h : float, k2 : float, q1 : int, q2 : int, f):
        return f(x + h / 2, v + k2 * h / 2, q1, q2)

    def k4(self, x : float, v : float, h : float, k3 : float, q1 : int, q2 : int, f):
        return f(x + h, v + k3 * h, q1, q2)

    def calculate_iter_rk4(self, x_curr : float, v_curr : float, h_curr : float, q1 : int, q2 : int, f):
        k1 = self.k1(x_curr, v_curr, h_curr, q1, q2, f)
        k2 = self.k2(x_curr, v_curr, h_curr, k1, q1, q2, f)
        k3 = self.k3(x_curr, v_curr, h_curr, k2, q1, q2, f)
        k4 = self.k4(x_curr, v_curr, h_curr, k3, q1, q2, f)

        x_next = x_curr + h_curr
        v_next = v_curr + (k1 + k2 * 2 + k3 * 2 + k4) * h_curr / 6
        return x_next, v_next
    
    def calculate_rk4_h_const(self, x0 : float, u0 : float, h0 : float, niter : int, right_break : float, q1 : int, q2 : int, barrier : int, f):
        x_list = [x0]
        v_list = [u0]
        v2_list = [u0]
        dv_list = [0]
        s_list = [0]
        h_list = [h0]
        c1_list = [0]
        c2_list = [0]

        x_curr = x0
        v_curr = u0
        h_curr = h0

        for i in range(niter):
            if right_break <= x_curr: break
            try:
                if barrier + 1 < v_curr:
                    q1 = 0
                elif v_curr < barrier - 1:
                    q1 = 30000
                x_next, v_next = self.calculate_iter_rk4(x_curr, v_curr, h_curr, q1, q2, f)

                x05, v05 = self.calculate_iter_rk4(x_curr, v_curr, h_curr / 2, q1, q2, f)
                if barrier + 1 < v_curr:
                    q1 = 0
                elif v_curr < barrier - 1:
                    q1 = 30000
                _, v2_next = self.calculate_iter_rk4(x05, v05, h_curr / 2, q1, q2, f)

                x_curr = x_next
                v_curr = v_next

                x_list.append(x_curr)
                v_list.append(v_curr)
                v2_list.append(v2_next)
                dv_list.append(v_curr - v2_next)
                s_list.append(abs((v_curr - v2_next) / 15))
                h_list.append(h0)
                c1_list.append(0)
                c2_list.append(0)
            except Exception:
                break
        return x_list, v_list, v2_list, dv_list, s_list, h_list, c1_list, c2_list

    def calculate_rk4(self, x0 : float, u0 : float, h0 : float, epsilon, niter : int, right_break : float, q1 : int, q2 : int, barrier : int, f):
        x_list = [x0]
        v_list = [u0]
        v2_list = [u0]
        dv_list = [0]
        s_list = [0]
        h_list = [h0]
        c1_list = [0]
        c2_list = [0]

        x_curr = x0
        v_curr = u0
        h_curr = h0

        for i in range(niter):
            if right_break <= x_curr: break
            try:
                s_curr = 0
                c1_curr = 0
                c2_curr = 0
                while (True):
                    if barrier + 1 < v_curr:
                        q1 = 0
                    elif v_curr < barrier - 1:
                        q1 = 30000
                    x_next, v_next = self.calculate_iter_rk4(x_curr, v_curr, h_curr, q1, q2, f)

                    x05, v05 = self.calculate_iter_rk4(x_curr, v_curr, h_curr / 2, q1, q2, f)
                    if barrier + 1 < v_curr:
                        q1 = 0
                    elif v_curr < barrier - 1:
                        q1 = 30000
                    _, v2_next = self.calculate_iter_rk4(x05, v05, h_curr / 2, q1, q2, f)

                    s_curr = abs((v_next - v2_next) / 15)
                    if epsilon < s_curr:
                        c1_curr += 1
                        h_curr /= 2
                        continue
                    if epsilon / 15 <= s_curr <= epsilon:
                        h_next = h_curr
                        break
                    if s_curr < epsilon / 15:
                        h_next = h_curr * 2
                        c2_curr += 1
                        break

                x_curr = x_next
                v_curr = v_next
                h_list.append(h_curr)
                h_curr = h_next

                x_list.append(x_curr)
                v_list.append(v_curr)
                v2_list.append(v2_next)
                dv_list.append(v_curr - v2_next)
                s_list.append(abs((v_curr - v2_next) / 15))
                c1_list.append(c1_curr)
                c2_list.append(c2_curr)
            except Exception:
                break
        return x_list, v_list, v2_list, dv_list, s_list, h_list, c1_list, c2_list
    
    def main_calculate(self):
        x0, u0, niter, right_break, h0, epsilon, q1, q2, barrier = self.parse_main_start_values()
        if 0 == epsilon:
            x_list, v_list, v2_list, dv_list, s_list, h_list, c1_list, c2_list = self.calculate_rk4_h_const(x0, u0, h0, niter, right_break, q1, q2, barrier, self.f_main)
            self.main_table.print_table(x_list, v_list, v2_list, dv_list, s_list, h_list, c1_list, c2_list)
        else:
            x_list, v_list, v2_list, dv_list, s_list, h_list, c1_list, c2_list = self.calculate_rk4(x0, u0, h0, epsilon, niter, right_break, q1, q2, barrier, self.f_main)
            self.main_table.print_table(x_list, v_list, v2_list, dv_list, s_list, h_list, c1_list, c2_list)
        self.update_info(*self.get_stats(s_list, h_list, c1_list, c2_list))
        self.plot(self.main_graphic, self.main_ax, x_list, v_list)