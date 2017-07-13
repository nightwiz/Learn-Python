import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

#声明queue；如果producer有写那么consumer就不需要写，但是实际上我们不知道那个先运行，所以可以重复声明。
channel.queue_declare(queue='hello1')

#回调函数，函数执行完就代表消息处理完。
def callback(ch, method, properties, body):     #ch,管道的内存对象
    print("-->", ch, method, properties)
    #time.sleep(30)
    print("[x] Recevied %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


#消费消息；如果收到消息，就调用callback函数来处理消息
#加上no_ack=True,表示消息不管是否处理完都不返回消息；默认为ack
channel.basic_consume(callback,
                      queue='hello',
                      )

print('[*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()