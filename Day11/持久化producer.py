import pika

#建立连接
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

#声明管道
channel = connection.channel()

#声明queue
channel.queue_declare(queue='hello',durable=True)

#通过管道发消息
channel.basic_publish(exchange='',
                      routing_key='hello',  #hello就是queue的名称；将消息发送到这个queue
                      body='Hello World!',
                      properties=pika.BasicProperties(
                          delivery_mode=2,
                      ))

print("[x] Sent 'Hello World!'")

#直接关闭管道
connection.close()