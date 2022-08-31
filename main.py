
from pywebio.input import *
from pywebio.output import *
from pywebio.session import defer_call,info as sesion_info, run_async
from pywebio import start_server
import asyncio

online_users = []
message_store = []

async def refresh_page(users,msg):
    global message_store
    while True:
        await asyncio.sleep(0.5)
        for m in message_store:
            msg.append(m)



async def main():
    msg_box = output()
    name = await input(label = "Enter your name: ",validate = lambda n: "This name is already used!" if n in online_users else None)
    put_html(r"""
        <h1> ENTER YOUR MESSAGE </h1>
        """,position= 0)
    put_text(name, position= 0)
    msg_box.append(put_markdown("""A New user joined.."""))

    online_users.append(name)
    run_async(refresh_page(name,msg_box))
    with use_scope("scope1"):
        while True:
            for i in message_store:
                put_warning(i)
            
            message = await input(label = "Type your message here ",required = True)
            message_store.append(message)
            clear("scope1")
            

if __name__  == "__main__":
    start_server(main, debug = True, port = 8000)



