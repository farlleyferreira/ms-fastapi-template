import asyncio
from aio_pika import connect, Message


async def main(loop):
    # Perform connection
    connection = await connect(
        "amqp://farlley_ferreira:mstemplate123@localhost:5672", loop=loop
    )

    # Creating a channel
    channel = await connection.channel()

    # Sending the message
    await channel.default_exchange.publish(
        Message(b"Hello World!"),
        routing_key="hello",
    )

    print(" [x] Sent 'Hello World!'")

    await connection.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
