import chainlit as cl
import my_chain


@cl.on_chat_start
def on_chat_start():
    #チェーンをインスタンス化
    chain = my_chain.create_chain()

    #チェーンをセッションに保存
    cl.user_session.set("chain", chain)


@cl.on_message
async def on_message(query):
    #チェーンをセッションから取得
    chain = cl.user_session.get("chain")

    user_input = query.content

    #チェーンを呼び出し
    res = await chain.acall({"input": user_input}, callbacks=[cl.AsyncLangchainCallbackHandler()])

    #チェーンの応答を送信
    await cl.Message(content=res["text"]).send()
