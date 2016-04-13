#ifndef TESLA_Q3_H
#define TESLA_Q3_H

#include <QWidget>

namespace Ui {
class tesla_q3;
}

class tesla_q3 : public QWidget
{
    Q_OBJECT

public:
    explicit tesla_q3(QWidget *parent = 0);
    ~tesla_q3();

private:
    Ui::tesla_q3 *ui;
};

#endif // TESLA_Q3_H
