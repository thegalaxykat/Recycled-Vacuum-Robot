import QtQuick 2.13
import QtQuick.Window 2.13
import QtQuick.Controls 2.15

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    Button {
        id: forward_button
        objectName: "forward_button"
        x: 270
        y: 144
        text: qsTr("Forward")

    Button {
        id: left_button
        objectName: "left_button"
        x: -72
        y: 49
        text: qsTr("Left")
    }

    Button {
        id: right_button
        objectName: "right_button"
        x: 70
        y: 49
        text: qsTr("Right")
    }

    Button {
        id: back_button
        objectName: "back_button"
        x: 0
        y: 95
        text: qsTr("Backward")
    }

    Button {
        id: stop_button
        objectName: "stop_button"
        x: 0
        y: 196
        text: qsTr("Stop")
    }
}
}
