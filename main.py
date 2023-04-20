import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = '6141871984:AAERW-uxORhNtZCk2MbFmNOFOk6A01hE0DE'
openai.api_key = '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' 

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler()
def send(message : types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= "",
        temperature=0.9,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop = ["You: "]
    )
        await message.answer(response['choices'][0]['text'])
executor.start_polling(dp, skip_updatees = True)