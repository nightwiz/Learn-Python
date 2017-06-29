import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

#声明queue；如果producer有写那么consumer就不需要写，但是实际上我们不知道那个先运行，所以可以重复声明。
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):     #ch,管道的内存对象
    print("-->", ch, method, properties)
    print("[x] Recevied %r" % body)


#消费消息；如果收到消息，就调用callback函数来处理消息
channel.basic_consume(callback, queue='hello', no_ack=True)

print('[*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()