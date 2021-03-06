from quart import Quart, render_template, request, session, url_for, redirect
from quart_discord import DiscordOAuth2Session
from discord.ext import ipc

app = Quart(__name__)
ipc_client = ipc.Client(secret_key = "Andrew")

app.config['SECRET_KEY'] = "test123"
app.config['DISCORD_CLIENT_ID'] = 920708831221272607
app.config['DISCORD_CLIENT_SECRET'] = "fWnXZrayYU7oPiEFKvcUZgQG7MEn1y7V"
app.config['DISCORD_REDIRECT_URI'] = "http://127.0.0.1:5000/callback"

discord = DiscordOAuth2Session(app)

@app.route('/')
async def home():
    return await render_template('index.html')

@app.route('/login')
async def login():
    return await discord.create_session()

@app.route('/callback')
async def callback():
    try:
        await discord.callback()
    except:
        return redirect(url_for("login"))
    
    user = await discord.fetch_user()
    return f"{user.name}#{user.discriminator}"

@app.route('/dashboard')
async def dashboard():
    guild_count = await ipc_client.request("get_guild_count")

    return f"O bot está em {guild_count} servers"

if __name__ == "__main__":
    app.run(debug=True)