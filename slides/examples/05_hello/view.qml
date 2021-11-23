import QtQuick 2.0
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.1
import QtQuick.Controls.Material 2.1

ApplicationWindow {
    id: page
    width: 700
    height: 300
    visible: true
    Material.theme: Material.Dark
    Material.accent: Material.Red

    ColumnLayout {
        spacing: 2
        anchors.centerIn: parent
        Layout.columnSpan: 1

        Text {
            id: label
            color: "white"
            font.pointSize: 42
            text: "Hello Qt for Python"
            Material.accent: Material.Green
            Layout.alignment: Qt.AlignCenter
        }

        Button {
            id: button
            text: "Color!"
            highlighted: true
            Material.accent: Material.Green
            onClicked: {
                label.color = con.get_color();
            }
            Layout.alignment: Qt.AlignCenter
        }
    }
}
