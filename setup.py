
from logging import Filter
from telegram.error import TimedOut
from telegram.ext import CommandHandler,Updater , MessageHandler
from telegram.ext.conversationhandler import ConversationHandler
from telegram.ext.filters import Filters, MessageFilter
from telegram.ext.utils.types import UD
from telegram import ChatAction, chat, message
from telegram.update import Update
ENTRADA_DEL_PEDIDO = 0
Poner_Canal = 1
Canaldereplica = ""
def start(update,context):
    update.message.reply_text('usa /pedido para hacer un pedido')
def inciode_pedido(update,context):
    update.message.reply_text('Envie el nombre de su pedido y sera atendido')
    return ENTRADA_DEL_PEDIDO
def ponga_elpedido(update,context):
    texto = "@"+ update.message.chat.username+ "Desea" + update.message.text 
    context.bot.send_message(chat_id="-1001583112440",text=texto )
    update.message.reply_text("El pedido se ha completado 🆗")
    return ConversationHandler.END
def EnviarMensajealchat(chat,mensaje):
    chat.send_chat_action(action=ChatAction.TYPING)
    chat.send_message(text =mensaje)
    pass
def Linkchannel(update,text):
    update.message.reply_text('ponga en nombre del canal al que va a enviar los pedidos')

    return Poner_Canal
def Canal_deReplicas(update,context):
    chat = update.message.chat
    EnviarMensajealchat(chat,"Se cambio el canal al que se envian los pedidos correctamente")
    Canaldereplica = update.message.text
    print(update)
    return ConversationHandler.END
    pass
if __name__ == '__main__':  
    update = Updater(token="aqui va tu toquen",use_context=True)
    despachador =  update.dispatcher
    #add handler

    despachador.add_handler(CommandHandler('start',start))
    despachador.add_handler(ConversationHandler(
        entry_points=
        [
            CommandHandler('pedido',inciode_pedido),
            CommandHandler('channel',Linkchannel)
        ],
        states=
        {
            ENTRADA_DEL_PEDIDO: [MessageHandler(Filters.text,ponga_elpedido)],
            Poner_Canal : [MessageHandler(Filters.text,Canal_deReplicas)]
        },
        fallbacks=[]

    ))
    update.start_polling()
    update.idle()
