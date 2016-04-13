/********************************************************************************
** Form generated from reading UI file 'tesla_q3.ui'
**
** Created by: Qt User Interface Compiler version 5.6.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_TESLA_Q3_H
#define UI_TESLA_Q3_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QTreeWidget>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_tesla_q3
{
public:
    QTreeWidget *treeWidget;

    void setupUi(QWidget *tesla_q3)
    {
        if (tesla_q3->objectName().isEmpty())
            tesla_q3->setObjectName(QStringLiteral("tesla_q3"));
        tesla_q3->resize(527, 396);
        treeWidget = new QTreeWidget(tesla_q3);
        new QTreeWidgetItem(treeWidget);
        new QTreeWidgetItem(treeWidget);
        new QTreeWidgetItem(treeWidget);
        treeWidget->setObjectName(QStringLiteral("treeWidget"));
        treeWidget->setGeometry(QRect(90, 70, 256, 192));

        retranslateUi(tesla_q3);

        QMetaObject::connectSlotsByName(tesla_q3);
    } // setupUi

    void retranslateUi(QWidget *tesla_q3)
    {
        tesla_q3->setWindowTitle(QApplication::translate("tesla_q3", "tesla_q3", 0));
        QTreeWidgetItem *___qtreewidgetitem = treeWidget->headerItem();
        ___qtreewidgetitem->setText(1, QApplication::translate("tesla_q3", "1", 0));
        ___qtreewidgetitem->setText(0, QApplication::translate("tesla_q3", "2", 0));

        const bool __sortingEnabled = treeWidget->isSortingEnabled();
        treeWidget->setSortingEnabled(false);
        QTreeWidgetItem *___qtreewidgetitem1 = treeWidget->topLevelItem(0);
        ___qtreewidgetitem1->setText(1, QApplication::translate("tesla_q3", "hello", 0));
        QTreeWidgetItem *___qtreewidgetitem2 = treeWidget->topLevelItem(1);
        ___qtreewidgetitem2->setText(0, QApplication::translate("tesla_q3", "Cheng", 0));
        QTreeWidgetItem *___qtreewidgetitem3 = treeWidget->topLevelItem(2);
        ___qtreewidgetitem3->setText(1, QApplication::translate("tesla_q3", "world", 0));
        treeWidget->setSortingEnabled(__sortingEnabled);

    } // retranslateUi

};

namespace Ui {
    class tesla_q3: public Ui_tesla_q3 {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_TESLA_Q3_H
