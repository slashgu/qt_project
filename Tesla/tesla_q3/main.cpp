#include "tesla_q3.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    tesla_q3 w;
    w.show();

    return a.exec();
}
