#ifndef SOCKETSERVER_H
#define SOCKETSERVER_H

#include <QtCore/QObject>
#include <QtCore/QList>
#include <QtCore/QByteArray>

QT_FORWARD_DECLARE_CLASS(QWebSocketServer)
QT_FORWARD_DECLARE_CLASS(QWebSocket)

class SocketServer : public QObject
{
    Q_OBJECT
public:
    explicit SocketServer(quint16 port, bool debug = false, QObject *parent = nullptr);
    ~SocketServer();

Q_SIGNALS:
    void closed();

private Q_SLOTS:
    void onNewConnection();
    void processTextMessage(QString message);
    void sendTextMessage(QString message);
    void socketDisconnected();

private:
    QWebSocketServer *webSocketServer;
    QList<QWebSocket *> socketClients;
    bool m_debug;
};

#endif // SOCKETSERVER_H
