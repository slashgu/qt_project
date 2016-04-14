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
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QTreeWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_tesla_q3
{
public:
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QTreeWidget *treeWidget;

    void setupUi(QWidget *tesla_q3)
    {
        if (tesla_q3->objectName().isEmpty())
            tesla_q3->setObjectName(QStringLiteral("tesla_q3"));
        tesla_q3->resize(678, 486);
        verticalLayout = new QVBoxLayout(tesla_q3);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        treeWidget = new QTreeWidget(tesla_q3);
        QTreeWidgetItem *__qtreewidgetitem = new QTreeWidgetItem(treeWidget);
        new QTreeWidgetItem(__qtreewidgetitem);
        treeWidget->setObjectName(QStringLiteral("treeWidget"));

        horizontalLayout->addWidget(treeWidget);


        verticalLayout->addLayout(horizontalLayout);


        retranslateUi(tesla_q3);

        QMetaObject::connectSlotsByName(tesla_q3);
    } // setupUi

    void retranslateUi(QWidget *tesla_q3)
    {
        tesla_q3->setWindowTitle(QApplication::translate("tesla_q3", "tesla_q3", 0));
        QTreeWidgetItem *___qtreewidgetitem = treeWidget->headerItem();
        ___qtreewidgetitem->setText(0, QApplication::translate("tesla_q3", "root", 0));

        const bool __sortingEnabled = treeWidget->isSortingEnabled();
        treeWidget->setSortingEnabled(false);
        QTreeWidgetItem *___qtreewidgetitem1 = treeWidget->topLevelItem(0);
        ___qtreewidgetitem1->setText(0, QApplication::translate("tesla_q3", "leaf 1", 0));
        QTreeWidgetItem *___qtreewidgetitem2 = ___qtreewidgetitem1->child(0);
        ___qtreewidgetitem2->setText(0, QApplication::translate("tesla_q3", "leaf 2", 0));
        treeWidget->setSortingEnabled(__sortingEnabled);

    } // retranslateUi

};

namespace Ui {
    class tesla_q3: public Ui_tesla_q3 {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_TESLA_Q3_H
