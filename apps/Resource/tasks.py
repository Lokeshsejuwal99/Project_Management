from celery import shared_task
import pika


@shared_task
def publish_user_created_event(user_id):
    connection = pika.BlockingConnection(pika.BlockingParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='user_created')
    channel.basic_publish(exchange='', routing_key='user_created', body=str(user_id))
    connection.close()
