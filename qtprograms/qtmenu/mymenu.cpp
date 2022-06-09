#include "mymenu.h" 
#include <QMenu>
#include <QMenuBar> 
#include <QApplication>
MyMenu::MyMenu(QWidget *parent)
                 : QMainWindow(parent)
{
 QAction *quit = new QAction("&Quit", this);
 QMenu *file;
 file = menuBar()->addMenu("&File");
 file->addAction(quit); 
 connect(quit, SIGNAL(triggered()), qApp, SLOT(quit()));
}