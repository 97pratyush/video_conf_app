# Form implementation generated from reading ui file 'meeting_design.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QSizePolicy,
    QMainWindow,
)


class MeetingPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1191, 691)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(
            "background-color: rgb(0, 0, 0);\n" "color: rgb(255, 255, 255);"
        )
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.meeting_container = QtWidgets.QWidget(parent=self.centralwidget)
        self.meeting_container.setGeometry(QtCore.QRect(0, 0, 951, 691))
        self.meeting_container.setStyleSheet("")
        self.meeting_container.setObjectName("meeting_container")
        self.video_container = QtWidgets.QWidget(parent=self.meeting_container)
        self.video_container.setGeometry(QtCore.QRect(0, 0, 951, 621))
        self.video_container.setStyleSheet("")
        self.video_container.setObjectName("video_container")
        self.gridLayout = QtWidgets.QGridLayout(self.video_container)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.self = QtWidgets.QLabel(parent=self.video_container)
        self.self.setStyleSheet(
            "border-color: rgb(255, 255, 255);\n" "color: rgb(255, 255, 255);"
        )
        self.self.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.self.setScaledContents(True)
        self.self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.self.setObjectName("self")
        self.gridLayout.addWidget(self.self, 0, 0, 2, 1)
        self.participant_1 = QtWidgets.QLabel(parent=self.video_container)
        self.participant_1.setStyleSheet(
            "border-color: rgb(255, 255, 255);\n" "color: rgb(255, 255, 255);"
        )
        self.participant_1.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.participant_1.setScaledContents(True)
        self.participant_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.participant_1.setObjectName("participant_1")
        self.gridLayout.addWidget(self.participant_1, 0, 1, 1, 1)
        self.participant_2 = QtWidgets.QLabel(parent=self.video_container)
        self.participant_2.setStyleSheet(
            "border-color: rgb(255, 255, 255);\n" "color: rgb(255, 255, 255);"
        )
        self.participant_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.participant_2.setScaledContents(True)
        self.participant_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.participant_2.setObjectName("participant_2")
        self.gridLayout.addWidget(self.participant_2, 1, 1, 1, 1)
        self.control_container = QtWidgets.QWidget(parent=self.meeting_container)
        self.control_container.setGeometry(QtCore.QRect(0, 620, 961, 71))
        self.control_container.setStyleSheet("")
        self.control_container.setObjectName("control_container")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.control_container)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            358,
            38,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout.addItem(spacerItem)
        self.end_meeting_2 = QtWidgets.QPushButton(parent=self.control_container)
        self.end_meeting_2.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(255, 255, 255);"
        )
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/icons/Icons/conference-multi-size.ico"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.end_meeting_2.setIcon(icon)
        self.end_meeting_2.setObjectName("end_meeting_2")
        self.horizontalLayout.addWidget(self.end_meeting_2)
        spacerItem1 = QtWidgets.QSpacerItem(
            115,
            38,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout.addItem(spacerItem1)
        self.end_meeting_3 = QtWidgets.QPushButton(parent=self.control_container)
        self.end_meeting_3.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(255, 255, 255);"
        )
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/icons/Icons/chat-4-multi-size.ico"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.end_meeting_3.setIcon(icon1)
        self.end_meeting_3.setObjectName("end_meeting_3")
        self.horizontalLayout.addWidget(self.end_meeting_3)
        spacerItem2 = QtWidgets.QSpacerItem(
            148,
            38,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout.addItem(spacerItem2)
        self.end_meeting = QtWidgets.QPushButton(parent=self.control_container)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_meeting.sizePolicy().hasHeightForWidth())
        self.end_meeting.setSizePolicy(sizePolicy)
        self.end_meeting.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(170, 0, 0);"
        )
        self.end_meeting.setObjectName("end_meeting")
        self.horizontalLayout.addWidget(self.end_meeting)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(960, 0, 231, 691))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.stackedWidget.sizePolicy().hasHeightForWidth()
        )
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(0, 0, 0);"
        )
        self.stackedWidget.setObjectName("stackedWidget")
        self.chat = QtWidgets.QWidget()
        self.chat.setObjectName("chat")
        self.label = QtWidgets.QLabel(parent=self.chat)
        self.label.setGeometry(QtCore.QRect(38, 40, 151, 61))
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.chat)
        self.participants = QtWidgets.QWidget()
        self.participants.setObjectName("participants")
        self.label_2 = QtWidgets.QLabel(parent=self.participants)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 161, 71))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.participants)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.end_meeting.clicked.connect(MainWindow.close)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.self.setText(_translate("MainWindow", "Self"))
        self.participant_1.setText(_translate("MainWindow", "Participant 3"))
        self.participant_2.setText(_translate("MainWindow", "Participant 2"))
        self.end_meeting_2.setText(_translate("MainWindow", "Participants"))
        self.end_meeting_3.setText(_translate("MainWindow", "Chat"))
        self.end_meeting.setText(_translate("MainWindow", "End Meeting"))
        self.label.setText(_translate("MainWindow", "Chat"))
        self.label_2.setText(_translate("MainWindow", "Participants"))


# if __name__ == "__main__":
#     import sys

#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = MeetingPage()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec())
