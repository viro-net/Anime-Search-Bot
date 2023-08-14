from pyrogram.types import Message
from pyrogram import filters
from AniPlay import app
from AniPlay.plugins.AnimeDex import AnimeDex
from AniPlay.plugins.button import BTN
from AniPlay.plugins.stats import day, over


@app.on_message(filters.command(['start', '']))
async def start(_, message: Message):
    try:
        await message.reply_text('जय श्री राम🚩,\n\n**I‘m Anime Search Bot, Creator- @StupidBoi69.**\n\nClick on /help to learn **How to use?** ')
    except:
        return


QUERY = '**Search Results:** `{}`'


@app.on_message(filters.command(['search', 's', 'gimme', 'iwant', 'find', 'anime']))
async def searchCMD(_, message: Message):
    try:
        user = message.from_user.id
        query = ' '.join(message.command[1:])
        if query == '':
            return await message.reply_text('Give me something to search; after cmd =⁠_⁠= ')
        data = AnimeDex.search(query)
        button = BTN.searchCMD(user, data, query)
        await message.reply_text(QUERY.format(query), reply_markup=button)
    except Exception as e:
        try:
            return await message.reply_text('**Anime Not Found...**\n\nProbably Incorrect Name, Try again')
        except:
            return


@app.on_message(filters.command('stats'))
async def stats(_, message: Message):
    try:
        await message.reply_text('Use /stats1, /todaystats For Day Wise Stats\nAnd /stats2, /overallstats For Overall Stats')
    except:
        return


@app.on_message(filters.command('stats1', 'todaystats'))
async def stats1(_, message: Message):
    try:
        img = day()
        await message.reply_photo(img, caption='**AnimeDex | Day Wise Stats**')
    except:
        return


@app.on_message(filters.command('stats2', 'overallstats'))
async def stats2(_, message: Message):
    try:
        img = over()
        await message.reply_photo(img, caption='**AnimeDex | Overall Stats**')
    except:
        return


@app.on_message(filters.command(['help', '']))
async def help(_, message: Message):
    try:
        await message.reply_text('To Get Started, Simply Use\n\n(**/search ‹anime name›,\n/find ‹anime name›,\n/iwant ‹anime name›.**)\n\n(**HINT: Choose Server5 for Downloading.**')
    except:
        return
