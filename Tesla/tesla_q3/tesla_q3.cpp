#include "tesla_q3.h"
#include "ui_tesla_q3.h"

tesla_q3::tesla_q3(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::tesla_q3)
{
    ui->setupUi(this);
}

tesla_q3::~tesla_q3()
{
    delete ui;
}
