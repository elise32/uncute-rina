from Uncute_Rina import *

report_message_reminder_unix = 0 #int(mktime(datetime.now().timetuple()))
selfies_delete_week_command_cooldown = 0

currency_options = {
    code: 0 for code in "AED,AFN,ALL,AMD,ANG,AOA,ARS,AUD,AWG,AZN,BAM,BBD,BDT,BGN,BHD,BIF,BMD,BND,BOB,BRL,BSD,BTC,BTN,BWP,BYN,BZD,CAD,CDF,"
                        "CHF,CLF,CLP,CNH,CNY,COP,CRC,CUC,CUP,CVE,CZK,DJF,DKK,DOP,DZD,EGP,ERN,ETB,EUR,FJD,FKP,GBP,GEL,GGP,GHS,GIP,GMD,GNF,"
                        "GTQ,GYD,HKD,HNL,HRK,HTG,HUF,IDR,ILS,IMP,INR,IQD,IRR,ISK,JEP,JMD,JOD,JPY,KES,KGS,KHR,KMF,KPW,KRW,KWD,KYD,KZT,LAK,"
                        "LBP,LKR,LRD,LSL,LYD,MAD,MDL,MGA,MKD,MMK,MNT,MOP,MRU,MUR,MVR,MWK,MXN,MYR,MZN,NAD,NGN,NIO,NOK,NPR,NZD,OMR,PAB,PEN,"
                        "PGK,PHP,PKR,PLN,PYG,QAR,RON,RSD,RUB,RWF,SAR,SBD,SCR,SDG,SEK,SGD,SHP,SLL,SOS,SRD,SSP,STD,STN,SVC,SYP,SZL,THB,TJS,"
                        "TMT,TND,TOP,TRY,TTD,TWD,TZS,UAH,UGX,USD,UYU,UZS,VES,VND,VUV,WST,XAF,XAG,XAU,XCD,XDR,XOF,XPD,XPF,XPT,YER,"
                        "ZAR,ZMW,ZWL".split(",")}
conversion_rates = { # [default 0, incrementation]
    "temperature":{
        "Celcius"    : [273.15, 1, "°C"],
        "Kelvin"     : [0, 1, "K"],
        "Fahrenheit" : [459.67, 1.8, "°F"],
        "Rankine"    : [0, 1.8, "°R"]
    },
    "length":{
        "kilometer"  : [0, 0.001, "km"],
        "hectometer" : [0, 0.01, "hm"],
        "meter"      : [0, 1, "m"],
        "decimeter"  : [0, 10, "dm"],
        "centimeter" : [0, 100, "cm"],
        "millimeter" : [0, 1000, "mm"],
        "micrometer" : [0, 10 ** 6, "μm"],
        "nanometer"  : [0, 10 ** 9, "nm"],
        "picometer"  : [0, 10 ** 12, "pm"],
        "femtometer" : [0, 10 ** 15, "fm"],
        "ångström"   : [0, 10 ** 10, "Å"],

        "mile"       : [0, 0.0006213711922373339, "mi"],
        "yard"       : [0, 1.09361329833770778652, "yd"],
        "foot"       : [0, 3.28083989501312335958, "ft"],
        "inch"       : [0, 39.37007874015748031496, "in"],

    },
    "surface area": {
        "square kilometer"  : [0, 0.000001, "km²"],
        "square meter"      : [0, 1, "m²"],
        "square centimeter" : [0, 10000, "cm²"],
        "square mile"       : [0, 0.00000038610215854781256, "mi²"],
        "square yard"       : [0, 1.19599, "yd²"],
        "square feet"       : [0, 10.76391, "ft²"],
        "square inch"       : [0, 1550, "in²"],
        "hectare"           : [0, 0.0001, "ha"],
        "acre"              : [0, 0.00024710538146716534, "ac"]
    },
    "volume": {
        "cubic meter"      : [0, 1, "m³"],
        "cubic centimeter" : [0, 1000000, "cm³"],
        "cubic feet"       : [0, 35.31466666, "ft³"],
        "quart"            : [0, 1056.688209, "qt"],
        "pint"             : [0, 2113.376419, "pt"],
        "fluid ounce"      : [0, 33814.0227, "fl oz"],
        "milliliter"       : [0, 1000000, "mL"],
        "liter"            : [0, 1000, "L"],
        "gallon"           : [0, 264.172052, "gal"],
        "cup"              : [0, 4226.752838, "cp"],
    },
    "speed": {
        "meter per second"    : [0, 1, "m/s"],
        "feet per second"     : [0, 3.28084, "ft/s"],
        "kilometers per hour" : [0, 3.6, "km/h"],
        "miles per hour"      : [0, 2.23694, "mph"],
        "knots"               : [0, 1.94384, "kn"]
    },
    "weight": {
        "kilogram"  : [0, 1, "kg"],
        "gram"      : [0, 1000, "g"],
        "milligram" : [0, 1000000, "mg"],
        "ounce"     : [0, 35.273962, "oz"], # 28.349523125
        "pound"     : [0, 2.20462262, "lb"], # 0.45359237
        "stone"     : [0, 0.157473],
        "US ton"    : [0, 0.001102311310924388],
        "UK ton"    : [0, 0.0009842065264486655],
        "Metric ton": [0, 0.001],
    },
    "currency":currency_options
}

def generateOutput(responses, author):
    output = ""
    if len(responses) > 0:
        output += f"""Hey there {author.mention},
Thank you for taking the time to answer our questions
If you don't mind, could you answer some more for us?"""

    keywords = ["First of all","Next","aaand..","Also","Lastly","PS","PPS","PPPS","PPPPS","PPPPPS","PPPPPPS"]
    for index in range(len(responses)):
        output += f"""

{keywords[index]},
{responses[index]}"""

    if len(output) > 0:
        output += """

Once again, if you dislike answering any of these or following questions, feel free to tell me. I can give others.
Thank you in advance :)"""
    else:
        output += "\n:warning: Couldn't think of any responses."
    return output

class Tags:
    class TagView(discord.ui.View):
        def __init__(self, embed, timeout=None):
            super().__init__()
            self.value = None
            self.timeout = timeout
            self.embed = embed

        @discord.ui.button(label='Send publicly', style=discord.ButtonStyle.primary)
        async def send_publicly(self, itx: discord.Interaction, _button: discord.ui.Button):
            self.value = 1
            self.embed.set_footer(text=f"Triggered by {itx.user.name} ({itx.user.id})")
            await itx.response.edit_message(content="Sent successfully!", embed=None, view=None)
            await itx.followup.send("", embed=self.embed, ephemeral=False, allowed_mentions=discord.AllowedMentions.none())
            self.stop()

        def on_timeout(self):
            self.send_publicly.disabled = True
            self.send_publicly.style = discord.ButtonStyle.gray

    @staticmethod
    async def send_report_info(context: [discord.Interaction, discord.TextChannel], additional_info=None, public=False):
        # additional_info = [message.author.name, message.author.id]
        embed = discord.Embed(
            color=discord.Colour.from_rgb(r=255, g=66, b=0), #a more saturated red orange color
            title='Reporting a message or scenario',
            description="Hi there! If anyone is making you uncomfortable, or you want to "
                        "report or prevent a rule-breaking situation, you can `Right Click "
                        "Message > Apps > Report Message` to notify our staff confidentially. "
                        "You can also create a mod ticket in <#995343855069175858> or DM a staff " # channel-id = #contact-staff
                        "member.")
        embed.set_image(url="https://i.imgur.com/jxEcGvl.gif")
        if isinstance(context, discord.Interaction):
            if public is True:
                await context.response.send_message(embed = embed)
            else:
                view = Tags().TagView(embed, timeout=60)
                await context.response.send_message(f"", embed=embed, view=view, ephemeral=True)
                if await view.wait():
                    await context.edit_original_response(view=view)
        else:
            if additional_info is not None:
                embed.set_footer(text=f"Triggered by {additional_info[0]} ({additional_info[1]})")
            await context.send(embed=embed)

    @staticmethod
    async def send_customvc_info(itx: discord.Interaction, client, public=True):
        collection = RinaDB["guildInfo"]
        query = {"guild_id": itx.guild.id}
        guild = collection.find_one(query)
        if guild is None:
            debug("Not enough data is configured to do this action! Please fix this with `/editguildinfo`!",
                  color="red")
            return
        vc_hub = guild["vcHub"]

        cmd_mention = client.getCommandMention('editvc')
        cmd_mention2 = client.getCommandMention('vctable about')
        embed = discord.Embed(
            color=discord.Colour.from_rgb(r=200, g=255, b=120), # greenish lime-colored
            title="TransPlace's custom voice channels (vc)",
            description=f"In our server, you can join <#{vc_hub}> to create a custom vc. You "
                        f"are then moved to this channel automatically. You can change the name and user "
                        f"limit of this channel with the {cmd_mention} command. When everyone leaves the "
                        f"channel, the channel is deleted automatically."
                        f"You can use {cmd_mention2} for additional features.")
        if public:
            await itx.response.send_message(embed=embed, ephemeral=False)
        else:
            view = Tags().TagView(embed, timeout=60)
            await itx.response.send_message(f"", embed=embed, view=view, ephemeral=True)
            if await view.wait():
                await itx.edit_original_response(view=view)

    @staticmethod
    async def send_triggerwarning_info(itx: discord.Interaction, public=True):
        embed = discord.Embed(
            color=discord.Colour.from_rgb(r=155, g=155, b=255), #bluer than baby blue ish. kinda light indigo
            title="Using trigger warnings correctly",
            description="Content or trigger warnings (CW and TW for short) are notices placed before a "
                        "(section of) text to warn the reader of potential traumatic triggers in it. Often, "
                        "people might want to avoid reading these, so a warning will help them be aware of "
                        "it.\n"
                        "You can warn the reader in the beginning or the middle of the text, and spoiler the "
                        "triggering section like so: \"TW: ||guns||: ||The gun was fired.||\".\n"
                        "\n"
                        r"You can spoiler messages with a double upright slash \|\|text\|\|.\n"
                        "Some potential triggers include (TW: triggers): abuse, bugs/spiders, death, "
                        "dieting/weight loss, injections, self-harm, transmed/truscum points of view or "
                        "transphobic content.")
        # embed.set_footer(text=f"Triggered by {itx.user.name} ({itx.user.id})")
        if public:
            await itx.response.send_message(embed=embed)
        else:
            view = Tags().TagView(embed, timeout=60)
            await itx.response.send_message(f"", embed=embed, view=view, ephemeral=True)
            if await view.wait():
                await itx.edit_original_response(view=view)

    @staticmethod
    async def send_toneindicator_info(itx: discord.Interaction, client, public=True):
        embed = discord.Embed(
            color=discord.Colour.from_rgb(r=142, g=237, b=221), # tealish aqua
            title="When to use tone indicators?",
            description="Tone indicators are a useful tool to clarify the meaning of a message.\n"
                        "Occasionally, people reading your comment may not be certain about the tone of "
                        "a message. Is it meant as positive feedback, a joke, or sarcasm?\n"
                        "\n"
                        "For example, you may playfully tease a friend. Without tone indicators, the "
                        "message may come across as rude or mean, but adding “/lh” (meaning light-"
                        "hearted) helps clarify that it was meant in good fun.\n"
                        "\n"
                        "Some tone indicators have multiple definitions depending on the context. For "
                        "example: \"/m\" can mean 'mad' or 'metaphor'. You can look up tone indicators by "
                        f"their tag or definition using {client.getCommandMention('toneindicator')}."
        )
        if public:
            await itx.response.send_message(embed=embed)
        else:
            view = Tags().TagView(embed, timeout=60)
            await itx.response.send_message(f"", embed=embed, view=view, ephemeral=True)
            if await view.wait():
                await itx.edit_original_response(view=view)

    @staticmethod
    async def send_trustedrole_info(itx: discord.Interaction, public=True):
        embed = discord.Embed(
            color=discord.Colour.from_rgb(r=220,g=155,b=255), # magenta
            title="The trusted role (and selfies)",
            description="The trusted role is the role we use to add an extra layer of protection to some "
                        "aspects of our community. Currently, this involves the selfie channel, but may be "
                        "expanded to other channels in future.\n"
                        "\n"
                        "You can obtain the trusted role by sending 500 messages or after gaining the "
                        "equivalent XP from voice channel usage. If you rejoin the server you can always "
                        "ask for the role back too!"
        )
        if public:
            await itx.response.send_message(embed=embed)
        else:
            view = Tags().TagView(embed, timeout=60)
            await itx.response.send_message(f"", embed=embed, view=view, ephemeral=True)
            if await view.wait():
                await itx.edit_original_response(view=view)

    @staticmethod
    async def send_minimodding_info(itx: discord.Interaction, public=True):
        embed = discord.Embed(
            color=discord.Colour.from_rgb(r=255,g=115,b=162),  # bright slightly reddish pink
            title="Correcting staff or minimodding",
            description="If you have any input on how members of staff operate, please open a ticket to "
                        "properly discuss."
                        "\n"
                        "Please do not interfere with moderator actions, as it can make situations worse. It can be seen as "
                        "harassment, and you could be warned."
        )
        if public:
            await itx.response.send_message(embed=embed)
        else:
            view = Tags().TagView(embed, timeout=60)
            await itx.response.send_message(f"", embed=embed, view=view, ephemeral=True)
            if await view.wait():
                await itx.edit_original_response(view=view)

class SearchAddons(commands.Cog):
    def __init__(self, client: Bot):
        self.client = client

    nameusage = app_commands.Group(name='nameusage', description='Get data about which names are used in the server')

    @nameusage.command(name="gettop", description="See how often different names occur in this server")
    @app_commands.choices(mode=[
        discord.app_commands.Choice(name='Search most-used usernames', value=1),
        discord.app_commands.Choice(name='Search most-used nicknames', value=2),
        discord.app_commands.Choice(name='Search nicks and usernames', value=3),
    ])
    # @app_commands.describe(string="What sentence or word do you want to blacklist? (eg: 'good girl' or 'girl')")
    async def nameusage_gettop(self, itx: discord.Interaction, mode: int):#, mode: int, string: str):
        await itx.response.defer(ephemeral=True)
        sections = {}
        for member in itx.guild.members:
            member_sections = []
            if mode == 1:
                names = [member.name]
            elif mode == 2 and member.nick is not None:
                names = [member.nick]
            elif mode == 3:
                names = [member.name]
                if member.nick is not None:
                    names.append(member.nick)
            else:
                continue

            _pronouns = [
                "she", "her",
                "he", "him",
                "they", "them",
                "it", "its"
            ]
            pronouns = []
            for pronounx in _pronouns:
                for pronouny in _pronouns:
                    pronouns.append(pronounx + " " + pronouny)

            for index in range(len(names)):
                new_name = ""
                for char in names[index]:
                    if char.lower() in "abcdefghijklmnopqrstuvwxyz":
                        new_name += char
                    else:
                        new_name += " "

                for pronoun in pronouns:
                    _name_backup = new_name + " "
                    while new_name != _name_backup:
                        _name_backup = new_name
                        new_name = re.sub(pronoun, "", new_name, flags=re.IGNORECASE)

                names[index] = new_name

            def add(part):
                if part not in member_sections:
                    member_sections.append(part)

            for name in names:
                for section in name.split():
                    if section in member_sections:
                        pass
                    else:
                        parts = []
                        match = 1
                        while match:
                            match = re.search("[A-Z][a-z]*[A-Z]", section, re.MULTILINE)
                            if match:
                                caps = match.span()[1]-1
                                parts.append(section[:caps])
                                section = section[caps:]
                        if len(parts) != 0:
                            for part in parts:
                                add(part)
                            add(section)
                        else:
                            add(section)

            for section in member_sections:
                section = section.lower()
                if section in ["the", "any", "not"]:
                    continue
                if len(section) < 3:
                    continue
                if section in sections:
                    sections[section] += 1
                else:
                    sections[section] = 1

        sections = sorted(sections.items(), key=lambda x:x[1], reverse=True)
        pages = []
        for i in range(int(len(sections)/20+0.999)+1):
            result_page = ""
            for section in sections[0+20*i:20+20*i]:
                result_page += f"{section[1]} {section[0]}\n"
            if result_page == "":
                result_page = "_"
            pages.append(result_page)
        page = 0
        class Pages(discord.ui.View):
            def __init__(self, pages, timeout=None):
                super().__init__()
                self.value   = None
                self.timeout = timeout
                self.page    = 0
                self.pages   = pages

            # When the confirm button is pressed, set the inner value to `True` and
            # stop the View from listening to more input.
            # We also send the user an ephemeral message that we're confirming their choice.
            @discord.ui.button(label='Previous', style=discord.ButtonStyle.blurple)
            async def previous(self, itx: discord.Interaction, _button: discord.ui.Button):
                # self.value = "previous"
                self.page -= 1
                if self.page < 0:
                    self.page += 1
                    await itx.response.send_message("This is the first page, you can't go to a previous page!",ephemeral=True)
                    return
                result_page = self.pages[self.page*2]
                result_page2 = self.pages[self.page*2+1]
                embed = discord.Embed(color=8481900, title=f'Most-used {"user" if type==1 else "nick"}names leaderboard!')
                embed.add_field(name="Column 1",value=result_page)
                embed.add_field(name="Column 2",value=result_page2)
                embed.set_footer(text="page: "+str(self.page+1)+" / "+str(int(len(self.pages)/2)))
                await itx.response.edit_message(embed=embed)

            @discord.ui.button(label='Next', style=discord.ButtonStyle.blurple)
            async def next(self, itx: discord.Interaction, _button: discord.ui.Button):
                self.page += 1
                try:
                    result_page = self.pages[self.page*2]
                    result_page2 = self.pages[self.page*2+1]
                except IndexError:
                    await itx.response.send_message("This is the last page, you can't go to a next page!",ephemeral=True)
                    return
                embed = discord.Embed(color=8481900, title=f'Most-used {"user" if type==1 else "nick"}names leaderboard!')
                embed.add_field(name="Column 1",value=result_page)
                embed.add_field(name="Column 2",value=result_page2)
                embed.set_footer(text="page: "+str(self.page+1)+" / "+str(int(len(self.pages)/2)))
                try:
                    await itx.response.edit_message(embed=embed)
                except discord.errors.HTTPException:
                    self.page -= 1
                    await itx.response.send_message("This is the last page, you can't go to a next page!",ephemeral=True)

        result_page = pages[page]
        result_page2 = pages[page+1]
        embed = discord.Embed(color=8481900, title=f'Most-used {"user" if type==1 else "nick" if type==2 else "username and nick"}names leaderboard!')
        embed.add_field(name="Column 1",value=result_page)
        embed.add_field(name="Column 2",value=result_page2)
        embed.set_footer(text="page: "+str(page+1)+" / "+str(int(len(pages)/2)))
        view = Pages(pages, timeout=60)
        await itx.followup.send(f"",embed=embed, view=view,ephemeral=True)
        await view.wait()
        if view.value is None:
            await itx.edit_original_response(view=None)

    @nameusage.command(name="name", description="See how often different names occur in this server")
    @app_commands.describe(name="What specific name are you looking for?")
    @app_commands.choices(type=[
        discord.app_commands.Choice(name='usernames', value=1),
        discord.app_commands.Choice(name='nicknames', value=2),
        discord.app_commands.Choice(name='Search both nicknames and usernames', value=3),
    ])
    async def nameusage_name(self, itx: discord.Interaction, name: str, type: int):
        await itx.response.defer(ephemeral=True)
        count = 0
        type_string = ""
        if type == 1:
            for member in itx.guild.members:
                if name.lower() in member.name.lower():
                    count += 1
            type_string = "username"
        elif type == 2:
            for member in itx.guild.members:
                if member.nick is not None:
                    if name.lower() in member.nick.lower():
                        count += 1
            type_string = "nickname"
        elif type == 3:
            for member in itx.guild.members:
                if member.nick is not None:
                    if name.lower() in member.nick.lower() or name.lower() in member.name.lower():
                        count += 1
                elif name.lower() in member.name.lower():
                    count += 1
            type_string = "username or nickname"
        await itx.followup.send(f"I found {count} people with '{name.lower()}' in their {type_string}",ephemeral=True)

    @app_commands.command(name="equaldex", description="Find info about LGBTQ+ laws in different countries!")
    @app_commands.describe(country_id="What country do you want to know more about? (GB, US, AU, etc.)")
    async def equaldex(self, itx: discord.Interaction, country_id: str):
        response_api = requests.get(
            f"https://www.equaldex.com/api/region?regionid={country_id}&formatted=true").text
        # returns ->  <pre>{"regions":{...}}</pre>  <- so you need to remove the <pre> and </pre> parts
        # it also has some <br \/>\r\n strings in there for some reason..? so uh
        response_api = response_api.replace(r"<br \/>\r\n", r"\n").replace("<pre>","").replace("</pre>","")
        data = json.loads(response_api)
        if "error" in data:
            if country_id.lower() == "uk":
                await itx.response.send_message(f"I'm sorry, I couldn't find '{country_id}'...\nTry 'GB' instead!", ephemeral=True)
            else:
                await itx.response.send_message(f"I'm sorry, I couldn't find '{country_id}'...",ephemeral=True)
            return

        class Region:
            def __init__(self, data):
                self.id = data['region_id']
                self.name = data['name']
                self.continent = data['continent']
                self.url = data['url']
                self.issues = data['issues']

        region = Region(data['regions']['region'])

        embed = discord.Embed(color=7829503, title=region.name)
        for issue in region.issues:
            if type(region.issues[issue]['current_status']) is list:
                value = "No data"
            else:
                value = region.issues[issue]['current_status']['value_formatted']
                # if region.issues[issue]['current_status']['value'] in ['Legal',
                #                                                        'Equal',
                #                                                        'No censorship',
                #                                                        'Legal, '
                #                                                        'surgery not required',
                #                                                        "Sexual orientation and gender identity",
                #                                                        "Recognized"]:
                #     value = "❤️ " + value
                # elif region.issues[issue]['current_status']['value'] in ["Illegal"]:
                #     value = "🚫 " + value
                # elif region.issues[issue]['current_status']['value'] in ["Not legally recognized",
                #                                                          "Not banned",
                #                                                          "Varies by Region"]:
                #     value = "🟨 " + value
                # else:
                #     value = "➖ " + value
                if len(region.issues[issue]['current_status']['description']) > 0:
                    value += f" ({region.issues[issue]['current_status']['description']})"
                elif len(region.issues[issue]['description']) > 0:
                    value += f" ({region.issues[issue]['description']})"
                if len(value) > 1024:
                    value = value[:1020]+"..."
            embed.add_field(name   = region.issues[issue]['label'],
                            value  = value,
                            inline = False)
        embed.set_footer(text=f"For more info, click the button below,")
        class MoreInfo(discord.ui.View):
            def __init__(self, url):
                super().__init__()
                link_button = discord.ui.Button(style = discord.ButtonStyle.gray,
                                                label = "More info",
                                                url = url)
                self.add_item(link_button)
        view = MoreInfo(region.url)
        await itx.response.send_message(embed=embed, view=view, ephemeral=True)

    async def tag_autocomplete(self, _itx: discord.Interaction, current: str):
        options = ["report", "customvc", "trigger warnings", "tone indicators",
                   "trusted role", "minimodding or correcting staff"]
        return [
            app_commands.Choice(name=term, value=term)
            for term in options if current.lower() in term
        ][:15]

    @app_commands.command(name="tag", description="Look up something through a tag")
    @app_commands.describe(tag="What tag do you want more information about?")
    @app_commands.describe(public="Show everyone in chat? (default: no)")
    @app_commands.autocomplete(tag=tag_autocomplete)
    async def tag(self, itx: discord.Interaction, tag: str, public: bool = False):
        if tag == "report":
            await Tags.send_report_info(itx, public=public)
        elif tag == "customvc":
            await Tags.send_customvc_info(itx, self.client, public=public)
        elif tag == "trigger warnings":
            await Tags.send_triggerwarning_info(itx, public=public)
        elif tag == "tone indicators":
            await Tags.send_toneindicator_info(itx, self.client, public=public)
        elif tag == "trusted role":
            await Tags.send_trustedrole_info(itx, public=public)
        elif tag == "minimodding or correcting staff":
            await Tags.send_minimodding_info(itx, public=public)
        else:
            await itx.response.send_message("No tag found with this name!", ephemeral=True)

class OtherAddons(commands.Cog):
    def __init__(self, client: Bot):
        global RinaDB
        self.client = client
        RinaDB = client.RinaDB
        self.headpatWait = 0

    @commands.Cog.listener()
    async def on_message(self, message):
        global report_message_reminder_unix
        try: # mention targeted user if added to mod-ticket with /add target:@user
            if message.channel.category.id in [995330645901455380, 995330667665707108, 1086349703182041089]:
                print("embeds:", len(message.embeds), "| message.author.id:", message.author.id)
                if message.author.id == 557628352828014614 and len(message.embeds) == 1:
                    # if ticket tool adds a user to a ticket, reply by mentioning the newly added user
                    components = message.embeds[0].description.split(" ")
                    print("components:", repr(components))
                    print("@" in components[0])
                    print(f'{components[1]} {components[2]} {components[3]} == "added to ticket"', f"{components[1]} {components[2]} {components[3]}" == "added to ticket")
                    if "@" in components[0] and f"{components[1]} {components[2]} {components[3]}" == "added to ticket":
                        await message.channel.send("Obligatory ping to notify newly added user: " + components[0], allowed_mentions=discord.AllowedMentions.all())
        except AttributeError:
            pass

        if message.author.bot:
            return

        #random cool commands
        self.headpatWait += 1
        if self.headpatWait >= 1000:
            ignore = False
            if type(message.channel) is discord.Thread:
                if message.channel.parent == 987358841245151262: # <#welcome-verify>
                    ignore = True
            if message.channel.name.startswith('ticket-') or message.channel.name.startswith('closed-'):
                ignore = True
            if message.channel.category.id in [959584962443632700, 959590295777968128, 959928799309484032, 1041487583475138692,
                                               995330645901455380, 995330667665707108]:
                # <#Bulletin Board>, <#Moderation Logs>, <#Verifier Archive>, <#Events>, <#Open Tickets>, <#Closed Tickets>
                ignore = True
            if message.guild.id in [981730502987898960]: # don't send in Mod server
                ignore = True
            if not ignore:
                self.headpatWait = 0
                try:
                    await message.add_reaction("<:TPF_02_Pat:968285920421875744>") #headpatWait
                except discord.errors.HTTPException:
                    await logMsg(message.guild, f'**:warning: Warning: **Couldn\'t add pat reaction to {message.jump_url}. They might have blocked Rina...')
                    try:
                        await message.add_reaction("☺") # relaxed
                    except discord.errors.Forbidden:
                        pass

        for staff_role_mention in ["<@&981735650971775077>", "<@&1012954384142966807>", "<@&981735525784358962>"]:
            if staff_role_mention in message.content:
                time_now = int(mktime(datetime.now().timetuple())) # get time in unix
                if time_now - report_message_reminder_unix > 900: # 15 minutes
                    await Tags.send_report_info(message.channel, additional_info=[message.author.name, message.author.id])
                    report_message_reminder_unix = time_now
                    break

        if self.client.user.mention in message.content.split():
            msg = message.content.lower()
            if ((("cute" or "cutie" or "adorable" in msg) and "not" in msg) or "uncute" in msg) and "not uncute" not in msg:
                try:
                    await message.add_reaction("<:this:960916817801535528>")
                except:
                    await logMsg(message.guild, f'**:warning: Warning: **Couldn\'t add pat reaction to {message.jump_url}')
                    raise
            elif "cutie" in msg or "cute" in msg:
                responses = [
                    "I'm not cute >_<",
                    "I'm not cute! I'm... Tough! Badass!",
                    "Nyaa~",
                    "Who? Me? No you're mistaken.",
                    "I very much deny the cuteness of someone like myself",
                    "If you think I'm cute, then you must be uber-cute!!",
                    "I don't think so.",
                    "Haha. Good joke. Tell me another tomorrow",
                    "Ehe, cutie what do u need help with?",
                    "No, I'm !cute.",
                    "You too!",
                    "No, you are <3",
                    "[shocked] Wha- w. .. w what?? .. NOo? no im nott?\nwhstre you tslking about?",
                    "Oh you were talking to me? I thought you were talking about everyone else here,",
                    "Nope. I doubt it. There's no way I can be as cute as you",
                    "Maybe.. Maybe I am cute.",
                    "If the sun was dying, would you still think I was cute?",
                    "Awww. Thanks sweety, but you've got the wrong number",
                    ":joy: You *reaaally* think so? You've gotta be kidding me.",
                    "If you're gonna be spamming this, .. maybe #general isn't the best channel for that.",
                    "You gotta praise those around you as well. "+(message.author.nick or message.author.name)+", for example, is very cute.",
                    "Oh by the way, did I say "+(message.author.nick or message.author.name)+" was cute yet? I probably didn't. "+(message.author.nick or message.author.name)+"? You're very cute",
                    "Such nice weather outside, isn't it? What- you asked me a question?\nNo you didn't, you're just talking to youself.",
                    "".join(random.choice("acefgilrsuwnopacefgilrsuwnopacefgilrsuwnop;;  ") for _ in range(random.randint(10,25))), # 3:2 letters to symbols
                    "Oh I heard about that! That's a way to get randomized passwords from a transfem!",
                    "Cuties are not gender-specific. For example, my cat is a cutie!\nOh wait, species aren't the same as genders. Am I still a catgirl then? Trans-species?",
                    "...",
                    "Hey that's not how it works!",
                    "Hey my lie detector said you are lying.",
                    "You know i'm not a mirror, right?",
                    "*And the oscar for cutest responses goes to..  YOU!!*",
                    "No I am not cute",
                    "k",
                    (message.author.nick or message.author.name)+", stop lying >:C",
                    "BAD!",
                    "You're also part of the cuties set",
                    "https://cdn.discordapp.com/emojis/920918513969950750.webp?size=4096&quality=lossless",
                    "[Checks machine]; Huh? Is my lie detector broken? I should fix that..",
                    "Hey, you should be talking about yourself first! After all, how do you keep up with being such a cutie all the time?"]
                respond = random.choice(responses)
                if respond == "BAD!":
                    await message.channel.send("https://cdn.discordapp.com/emojis/902351699182780468.gif?size=56&quality=lossless", allowed_mentions=discord.AllowedMentions.none())
                await message.channel.send(respond, allowed_mentions=discord.AllowedMentions.none())
            else:
                cmd_mention = self.client.getCommandMention("help")
                await message.channel.send(f"I use slash commands! Use /command  and see what cool things might pop up! or try {cmd_mention}\nPS: If you're trying to call me cute: no, I'm not", delete_after=8)

    @app_commands.command(name="say",description="Force Rina to repeat your wise words")
    @app_commands.describe(text="What will you make Rina repeat?")
    async def say(self, itx: discord.Interaction, text: str):
        if not isStaff(itx):
            await itx.response.send_message("Hi. sorry.. It would be too powerful to let you very cool person use this command.",ephemeral=True)
            return
        collection = RinaDB["guildInfo"]
        query = {"guild_id": itx.guild.id}
        guild = collection.find_one(query)
        if guild is None:
            debug("Not enough data is configured to do this action! Please fix this with `/editguildinfo`!",color="red")
            await itx.response.send_message("Couldn't send your message. You can't send messages in this server because the bot setup seems incomplete",ephemeral=True)
            return
        try:
            vcLog      = guild["vcLog"]
            logChannel = itx.guild.get_channel(vcLog)
            await logChannel.send(f"{itx.user.nick or itx.user.name} ({itx.user.id}) said a message using Rina: {text}", allowed_mentions=discord.AllowedMentions.none())
            text = text.replace("[[\\n]]","\n").replace("[[del]]","")
            await itx.channel.send(f"{text}", allowed_mentions=discord.AllowedMentions(everyone=False,users=True,roles=True,replied_user=True))
        except discord.Forbidden:
            await itx.response.send_message("Forbidden! I can't send a message in this channel/thread because I can't see it or because I'm not added to it yet!\n(Add me to the thread by mentioning me, or let Rina see this channel)",ephemeral=True)
            return
        except:
            await itx.response.send_message("Oops. Something went wrong!",ephemeral=True)
            raise
        await itx.response.send_message("Successfully sent!", ephemeral=True)

    @app_commands.command(name="compliment", description="Complement someone fem/masc/enby")
    @app_commands.describe(user="Who do you want to compliment?")
    async def compliment(self, itx: discord.Interaction, user: discord.User):
        # await itx.response.send_message("This command is currently disabled for now, since we're missing compliments. Feel free to suggest some, and ping @MysticMia#7612",ephemeral=True)
        # return
        try:
            user: discord.Member # make IDE happy, i guess
            userroles = user.roles[:]
        except AttributeError:
            await itx.response.send_message("Aw man, it seems this person isn't in the server. I wish I could compliment them but they won't be able to see it!", ephemeral=True)
            return

        async def call(itx, user, type):
            quotes = {
                "fem_quotes": [
                    # "Was the sun always this hot? or is it because of you?",
                    # "Hey baby, are you an angel? Cuz I’m allergic to feathers.",
                    "I bet you sweat glitter.",
                    "Your hair looks stunning!",
                    "Being around you is like being on a happy little vacation.",
                    "Good girll",
                    "Who's a good girl?? You are!!",
                    "Amazing! Perfect! Beautiful! How **does** she do it?!",
                    "I can tell that you are a very special and talented girl!",
                    "Here, have this cute sticker!"
                ],
                "masc_quotes": [
                    "You are the best man out there.",
                    "You are the strongest guy I know.",
                    "You have an amazing energy!",
                    "You seem to know how to fix everything!",
                    "Waw, you seem like a very attractive guy!",
                    "Good boyy!",
                    "Who's a cool guy? You are!!",
                    "I can tell that you are a very special and talented guy!",
                    "You're such a gentleman!",

                ],
                "they_quotes": [
                    "I can tell that you are a very special and talented person!",
                    "Their, their... ",
                ],
                "it_quotes": [
                    "I bet you do the crossword puzzle in ink!",
                ],
                "unisex_quotes": [ #unisex quotes are added to each of the other quotes later on.
                    "Hey I have some leftover cookies.. \\*wink wink\\*",
                    # "_Let me just hide this here-_ hey wait, are you looking?!", #it were meant to be cookies TwT
                    "Would you like a hug?",
                    "Would you like to walk in the park with me? I gotta walk my catgirls",
                    "morb",
                    "You look great today!",
                    "You light up the room!",
                    "On a scale from 1 to 10, you’re an 11!",
                    'When you say, “I meant to do that,” I totally believe you.',
                    "You should be thanked more often. So thank you!",
                    "You are so easy to have a conversation with!",
                    "Ooh you look like a good candidate to give my pet blahaj to!",
                    "Here, have a sticker!"



                ]
            }
            type = {
                "she/her"   : "fem_quotes",
                "he/him"    : "masc_quotes",
                "they/them" : "they_quotes",
                "it/its"    : "it_quotes",
                "unisex"    : "unisex_quotes", #todo
            }[type]

            for x in quotes:
                if x == "unisex_quotes":
                    continue
                else:
                    quotes[x] += quotes["unisex_quotes"]

            collection = RinaDB["complimentblacklist"]
            query = {"user": user.id}
            search = collection.find_one(query)
            if search is None:
                blacklist = []
            else:
                blacklist = search["list"]
            for string in blacklist:
                dec = 0
                for x in range(len(quotes[type])):
                    if string in quotes[type][x-dec]:
                        del quotes[type][x-dec]
                        dec += 1
            if len(quotes[type]) == 0:
                quotes[type].append("No compliment quotes could be given... This person seems to have blacklisted every quote.")

            base = f"{itx.user.mention} complimented {user.mention}!\n"
            if itx.response.is_done():
                # await itx.edit_original_response(content=base+random.choice(quotes[type]), view=None)
                await itx.followup.send(content=base+random.choice(quotes[type]), allowed_mentions=discord.AllowedMentions(everyone=False, users=[user], roles=False, replied_user=False))
            else:
                await itx.response.send_message(base+random.choice(quotes[type]), allowed_mentions=discord.AllowedMentions(everyone=False, users=[user], roles=False, replied_user=False))
        async def confirm_gender():
            # Define a simple View that gives us a confirmation menu
            class Confirm(discord.ui.View):
                def __init__(self, timeout=None):
                    super().__init__()
                    self.value = None
                    self.timeout = timeout

                # When the confirm button is pressed, set the inner value to `True` and
                # stop the View from listening to more input.
                # We also send the user an ephemeral message that we're confirming their choice.
                @discord.ui.button(label='She/Her', style=discord.ButtonStyle.green)
                async def feminine(self, itx: discord.Interaction, _button: discord.ui.Button):
                    self.value = "she/her"
                    await itx.response.edit_message(content='Selected She/Her pronouns for compliment', view=None)
                    self.stop()

                @discord.ui.button(label='He/Him', style=discord.ButtonStyle.green)
                async def masculine(self, itx: discord.Interaction, _button: discord.ui.Button):
                    self.value = "he/him"
                    await itx.response.edit_message(content='Selected He/Him pronouns for the compliment', view=None)
                    self.stop()

                @discord.ui.button(label='They/Them', style=discord.ButtonStyle.green)
                async def enby_them(self, itx: discord.Interaction, _button: discord.ui.Button):
                    self.value = "they/them"
                    await itx.response.edit_message(content='Selected They/Them pronouns for the compliment', view=None)
                    self.stop()

                @discord.ui.button(label='It/Its', style=discord.ButtonStyle.green)
                async def enby_its(self, itx: discord.Interaction, _button: discord.ui.Button):
                    self.value = "it/its"
                    await itx.response.edit_message(content='Selected It/Its pronouns for the compliment', view=None)
                    self.stop()

                @discord.ui.button(label='Unisex/Unknown', style=discord.ButtonStyle.grey)
                async def unisex(self, itx: discord.Interaction, _button: discord.ui.Button):
                    self.value = "unisex"
                    await itx.response.edit_message(content='Selected Unisex/Unknown gender for the compliment', view=None)
                    self.stop()

            view = Confirm(timeout=60)
            await itx.response.send_message(f"{user.mention} doesn't have any pronoun roles! Which pronouns would like to use for the compliment?", view=view,ephemeral=True)
            await view.wait()
            if view.value is None:
                await itx.edit_original_response(content=':x: Timed out...', view=None)
            else:
                await call(itx, user, view.value)

        roles = ["he/him", "she/her", "they/them", "it/its"]
        random.shuffle(userroles) # pick a random order for which pronoun role to pick
        for role in userroles:
            if role.name.lower() in roles:
                await call(itx, user, role.name.lower())
                return
        await confirm_gender()

    @app_commands.command(name="complimentblacklist", description="If you dislike words in certain compliments")
    @app_commands.choices(mode=[
        discord.app_commands.Choice(name='Add a string to your compliments blacklist', value=1),
        discord.app_commands.Choice(name='Remove a string from your compliments blacklist', value=2),
        discord.app_commands.Choice(name='Check your blacklisted strings', value=3)
    ])
    @app_commands.describe(string="What sentence or word do you want to blacklist? (eg: 'good girl' or 'girl')")
    async def complimentblacklist(self, itx: discord.Interaction, mode: int, string: str):
        if mode == 1: # add an item to the blacklist
            if len(string) > 150:
                await itx.response.send_message("Please make strings shorter than 150 characters...",ephemeral=True)
                return
            collection = RinaDB["complimentblacklist"]
            query = {"user": itx.user.id}
            search = collection.find_one(query)
            if search is None:
                blacklist = []
            else:
                blacklist = search['list']
            blacklist.append(string)
            collection.update_one(query, {"$set":{f"list":blacklist}}, upsert=True)
            await itx.response.send_message(f"Successfully added {repr(string)} to your blacklist. ({len(blacklist)} item{'s'*(len(blacklist)!=1)} in your blacklist now)",ephemeral=True)

        elif mode == 2: # Remove item from black list
            try:
                string = int(string)
            except ValueError:
                await itx.response.send_message("To remove a string from your blacklist, you must give the id of the string you want to remove. This should be a number... You didn't give a number...", ephemeral=True)
                return
            collection = RinaDB["complimentblacklist"]
            query = {"user": itx.user.id}
            search = collection.find_one(query)
            if search is None:
                await itx.response.send_message("There are no items on your blacklist, so you can't remove any either...",ephemeral=True)
                return
            blacklist = search["list"]

            try:
                del blacklist[string]
            except IndexError:
                cmd_mention = self.client.getCommandMention("complimentblacklist")
                await itx.response.send_message(f"Couldn't delete that ID, because there isn't any item on your list with that ID.. Use {cmd_mention} `mode:Check` to see the IDs assigned to each item on your list",ephemeral=True)
                return
            collection.update_one(query, {"$set":{f"list":blacklist}}, upsert=True)
            await itx.response.send_message(f"Successfully removed '{string}' from your blacklist. Your blacklist now contains {len(blacklist)} string{'s'*(len(blacklist)!=1)}.", ephemeral=True)
        elif mode == 3:
            collection = RinaDB["complimentblacklist"]
            query = {"user": itx.user.id}
            search = collection.find_one(query)
            if search is None:
                await itx.response.send_message("There are no strings in your blacklist, so.. nothing to list here....",ephemeral=True)
                return
            blacklist = search["list"]
            length = len(blacklist)

            ans = []
            for id in range(length):
                ans.append(f"`{id}`: {blacklist[id]}")
            ans = '\n'.join(ans)
            await itx.response.send_message(f"Found {length} string{'s'*(length!=1)}:\n{ans}",ephemeral=True)

    @app_commands.command(name="roll", description="Roll a die or dice with random chance!")
    @app_commands.describe(dice="How many dice do you want to roll?",
                           faces="How many sides does every die have?",
                           mod="Do you want to add a modifier? (add 2 after rolling the dice)",
                           advanced="Roll more advanced! example: 1d20+3*2d4. Overwrites dice/faces given; 'help' for more")
    async def roll(self, itx: discord.Interaction, dice: int, faces: int, public: bool = False, mod: int = None, advanced: str = None):
        if advanced is None:
            if dice < 1 or faces < 1:
                await itx.response.send_message("You can't have negative dice/faces! Please give a number above 0",ephemeral=True)
                return
            if dice > 100000:
                await itx.response.send_message(f"Sorry, if I let you roll `{dice:,}` dice, then the universe will implode, and Rina will stop responding to commands. Please stay below 1 million dice...",ephemeral=True)
                return
            if faces > 100000:
                await itx.response.send_message(f"Uh.. At that point, you're basically rolling a sphere. Even earth has fewer faces than `{faces:,}`. Please bowl with a sphere of fewer than 1 million faces...",ephemeral=True)
                return
            rolls = []
            for die in range(dice):
                rolls.append(random.randint(1,faces))

            if mod is None:
                if dice == 1:
                    out = f"I rolled {dice} di{'c'*(dice>1)}e with {faces} face{'s'*(faces>1)}: " +\
                          f"{str(sum(rolls))}"
                else:
                    out = f"I rolled {dice} di{'c'*(dice>1)}e with {faces} face{'s'*(faces>1)}:\n" +\
                          f"{' + '.join([str(roll) for roll in rolls])}  =  {str(sum(rolls))}"
            else:
                out = f"I rolled {dice} {'die' if dice == 0 else 'dice'} with {faces} face{'s'*(faces>1)} and a modifier of {mod}:\n" +\
                      f"({' + '.join([str(roll) for roll in rolls])}) + {mod}  =  {str(sum(rolls)+mod)}"
            if len(out) > 300:
                out = f"I rolled {dice:,} {'die' if dice == 0 else 'dice'} with {faces:,} face{'s'*(faces>1)}"+f" and a modifier of {(mod or 0):,}"*(mod is not None)+":\n" +\
                      f"With this many numbers, I've simplified it a little. You rolled `{sum(rolls)+(mod or 0):,}`."
                roll_db = {}
                for roll in rolls:
                    try:
                        roll_db[roll] += 1
                    except KeyError:
                        roll_db[roll] = 1
                # order dict by the eyes rolled: {"eyes":"count",1:4,2:1,3:4,4:1}
                # x.items() gives a list of tuples [(1,4),(2,1),(3,4),(4,1)] that is then sorted by the first item in the tuple
                roll_db = dict(sorted([x for x in roll_db.items()]))
                details = "You rolled "
                for roll in roll_db:
                    details += f"'{roll}'x{roll_db[roll]}, "
                if len(details) > 1500:
                    details = ""
                elif len(details) > 300:
                    public = False
                out = out + "\n" + details
            elif len(out) > 300:
                public = False
            await itx.response.send_message(out,ephemeral=not public)
        else:
            advanced = advanced.replace(" ","")
            def prod(list: list):
                a = 1
                for x in list:
                    a *= x
                return a

            def generate_roll(query: str):
                # print(query)
                temp = query.split("d")
                ## 2d4 = ["2","4"]
                ## 2d3d4 = ["2","3","4"] (huh?)
                ## 4 = 4
                ## [] (huh?)
                if len(temp) > 2:
                    raise ValueError("Can't have more than 1 'd' in the query of your die!")
                if len(temp) == 1:
                    try:
                        temp[0] = int(temp[0])
                    except ValueError:
                        raise TypeError(f"You can't do operations with '{temp[0]}'")
                    return [temp[0]]
                if len(temp) < 1:
                    raise ValueError(f"I couldn't understand what you meant with {query} ({str(temp)})")
                dice = temp[0]
                faces = ""
                for x in temp[1]:
                    if x in "0123456789":
                        faces += x
                    else:
                        break
                remainder = temp[1][len(faces):]
                try:
                    dice = int(dice)
                except ValueError:
                    raise ValueError(f"You have to roll a numerical number of dice! (You tried to roll '{dice}' dice)")
                try:
                    faces = int(faces)
                except ValueError:
                    raise TypeError(
                        f"You have to roll a die with a numerical number of faces! (You tried to roll {dice} dice with '{faces}' faces)")
                if len(remainder) > 0:
                    raise TypeError("Idk what happened, but you probably filled something in incorrectly.")
                if dice > 1000000:
                    raise OverflowError(f"Sorry, if I let you roll `{dice:,}` dice, then the universe will implode, and Rina will stop responding to commands. Please stay below 1 million dice...")
                if faces > 1000000:
                    raise OverflowError(f"Uh.. At that point, you're basically rolling a sphere. Even earth has fewer faces than `{faces:,}`. Please bowl with a sphere of fewer than 1 million faces...")
                return [random.randint(1, faces) for _ in range(dice)]

            for char in advanced:
                if char not in "0123456789d+*":  # kKxXrR": #!!pf≤≥
                    await itx.response.send_message(f"Invalid input! This command doesn't have support for '{char}' yet!",ephemeral=True)
                    return
            add = advanced.split('+')
            # print("add:       ",add)
            multiply = []
            for section in add:
                multiply.append(section.split('*'))
            # print("multiply:  ",multiply)
            try:
                result = [[sum(generate_roll(query)) for query in section] for section in multiply]
            except (TypeError,ValueError) as ex:
                ex = repr(ex).split("(",1)
                ex_type = ex[0]
                ex_message = ex[1][1:-2]
                await itx.response.send_message(f"Wasn't able to roll your dice!\n  {ex_type}: {ex_message}",ephemeral=True)
                return
            # print("result:    ",result)
            out = ["Input:  " + advanced]
            if "*" in advanced:
                out += [' + '.join([' * '.join([str(x) for x in section]) for section in result])]
            if "+" in advanced:
                out += [' + '.join([str(prod(section)) for section in result])]
            out += [str(sum([prod(section) for section in result]))]
            output = discord.utils.escape_markdown('\n= '.join(out))
            if len(output) >= 1950:
                output = "Your result was too long! I couldn't send it. Try making your rolls a bit smaller, perhaps by splitting it into multiple operations..."
            if len(output) >= 500:
                public = False
            try:
                await itx.response.send_message(output,ephemeral=not public)
            except discord.errors.NotFound:
                await itx.user.send("Couldn't send you the result of your roll because it took too long or something. Here you go: \n"+output)

    @app_commands.command(name="help", description="A help command to learn more about me!")
    async def help(self, itx: discord.Interaction):
        out = f"""\
Hi there! This bot has a whole bunch of commands. Let me introduce you to some:
{self.client.getCommandMention('compliment')}: Rina can compliment others (matching their pronoun role)
{self.client.getCommandMention('convert_unit')}: Convert a value from one to another! Distance, speed, currency, etc.
{self.client.getCommandMention('dictionary')}: Search for an lgbtq+-related or dictionary term!
{self.client.getCommandMention('equaldex')}: See LGBTQ safety and rights in a country (with API)
{self.client.getCommandMention('help')}: See this help page
{self.client.getCommandMention('nameusage gettop')}: See how many people are using the same name
{self.client.getCommandMention('pronouns')}: See someone's pronouns or edit your own
{self.client.getCommandMention('qotw')}: Suggest a Question Of The Week to staff
{self.client.getCommandMention('roll')}: Roll some dice with a random result
{self.client.getCommandMention('reminder reminders')}: Make or see your reminders
{self.client.getCommandMention('tag')}: Get information about some of the server's extra features
{self.client.getCommandMention('todo')}: Make, add, or remove items from your to-do list
{self.client.getCommandMention('toneindicator')}: Look up which tone tag/indicator matches your input (eg. /srs)

Make a custom voice channel by joining "Join to create VC" (use {self.client.getCommandMention('tag')} `tag:customvc` for more info)
{self.client.getCommandMention('editvc')}: edit the name or user limit of your custom voice channel
{self.client.getCommandMention('vctable about')}: Learn about making your voice chat more on-topic!
"""
# Check out the #join-a-table channel: In this channel, you can claim a channel for roleplaying or tabletop games for you and your group!
# The first person that joins/creates a table gets a Table Owner role, and can lock, unlock, or close their table.
# {self.client.getCommandMention('table lock')}, {self.client.getCommandMention('table unlock')}, {self.client.getCommandMention('table close')}
# You can also transfer your table ownership to another table member, after they joined your table: {self.client.getCommandMention('table newowner')}\
# """
        await itx.response.send_message(out, ephemeral=True)

    @app_commands.command(name="delete_week_selfies", description="Remove selfies and messages older than 7 days")
    async def delete_week_selfies(self, itx: discord.Interaction):
        global selfies_delete_week_command_cooldown
        if not isStaff(itx):
            await itx.response.send_message("You don't have permissions to use this command. (for ratelimit reasons)", ephemeral=True)
            return
        time_now = int(mktime(datetime.now().timetuple()))  # get time in unix
        if time_now - selfies_delete_week_command_cooldown < 86400:  # 1 day
            await itx.response.send_message("This command has already been used yesterday! Please give it some time and prevent ratelimiting.", ephemeral=True)
            return
        if 'selfies' != itx.channel.name or not isinstance(itx.channel, discord.channel.TextChannel):
            await itx.response.send_message("You need to send this in a text channel named \"selfies\"", ephemeral=True)
            return
        output = "Attempting deletion...\n"
        await itx.response.send_message(output+"...", ephemeral=True)
        try:
            await logMsg(itx.guild,f"{itx.user} ({itx.user.id}) deleted messages older than 7 days, in {itx.channel.mention} ({itx.channel.id}).")

            message_delete_count = 0
            async for message in itx.channel.history(limit=None, before = datetime.now()-timedelta(days=6,hours=23,minutes=30), oldest_first=True):
                message_date = int(mktime(message.created_at.timetuple()))
                if time_now-message_date > 7*86400: # 7 days ; technically redundant due to loop's "before" kwarg, but better safe than sorry
                    if "[info]" in message.content.lower():
                        class Interaction:
                            def __init__(self, member: discord.Member):
                                self.user = member
                                self.guild = member.guild
                        if isStaff(Interaction(message.author)): # nested to save having to look through function 1000 times
                            continue
                    await message.delete()
                    # print("----Deleted---- ["+str(message.created_at)+f"] {message.author}: {message.content}")
                    message_delete_count += 1
                    if message_delete_count % 50 == 0:
                        try:
                            await itx.edit_original_response(content=output+f"\nRemoved {message_delete_count} messages older than 7 days in {itx.channel.mention} so far...")
                        except discord.errors.HTTPException:
                            pass # ephemeral message timed out or something..
                    continue
                # print("++++Not deleted++++ ["+str(message.created_at)+f"] {message.author}: {message.content}")

            selfies_delete_week_command_cooldown = time_now
            await itx.followup.send(f"Removed {message_delete_count} messages older than 7 days successfully!", ephemeral=True)
        except:
            await itx.followup.send_message("Something went wrong!")
            raise

    async def unit_autocomplete(self, itx: discord.Interaction, current: str):
        options = conversion_rates.copy()
        if itx.namespace.mode not in options:
            return [] # user hasn't selected a mode yet.
        options = options[itx.namespace.mode]
        if itx.namespace.mode == "currency":
            return [
                app_commands.Choice(name=option, value=option)
                for option in options if option.lower().startswith(current.lower())
            ][:10]
        else:
            return [
                app_commands.Choice(name=option, value=option)
                for option in options if current.lower() in option.lower()
            ][:25]

    @app_commands.command(name="convert_unit", description="Convert temperature or distance from imperial to metric etc.")
    @app_commands.choices(mode=[
        discord.app_commands.Choice(name='Temperature (Fahrenheit, C, K, etc.)', value="temperature"),
        discord.app_commands.Choice(name='Length (miles,km,inch)', value="length"),
        discord.app_commands.Choice(name='Surface area (sq.ft., m^2)', value="surface area"),
        discord.app_commands.Choice(name='Volume (m^3)', value="volume"),
        discord.app_commands.Choice(name='Speed (mph, km/h, m/s, etc.)', value="speed"),
        discord.app_commands.Choice(name='Weight (pounds, ounces, kg, gram, etc.)', value="weight"),
        discord.app_commands.Choice(name='Currency (USD, EUR, CAD, etc.)', value="currency"),
        # discord.app_commands.Choice(name='Currency/money (USD, EUR, CAD)', value="currency"),
    ])
    @app_commands.describe(mode="What category of unit do you want to convert",
                           from_unit="Which unit do you want to convert from?",
                           public="Do you want to share the result with everyone in chat?")
    @app_commands.rename(from_unit='from')
    @app_commands.autocomplete(from_unit=unit_autocomplete)
    @app_commands.rename(from_unit='to')
    @app_commands.autocomplete(to_unit=unit_autocomplete)
    async def convert_unit(self, itx:discord.Interaction, mode: str, from_unit: str, value: float, to_unit: str, public: bool = False):
        rates = conversion_rates.copy()
        if mode not in rates:
            await itx.response.send_message("You didn't give a valid conversion method/mode!", ephemeral=True)
            return
        if mode == "currency":
            # more info: https://docs.openexchangerates.org/reference/latest-json
            api_key = self.client.api_tokens['Open Exchange Rates']
            response_api = requests.get(
                f"https://openexchangerates.org/api/latest.json?app_id={api_key}&show_alternative=true").text
            data = json.loads(response_api)
            if data.get("error",0):
                await itx.response.send_message(f"I'm sorry, something went wrong while trying to get the latest data", ephemeral=True)
                return
            options = {x:[0,data['rates'][x],x] for x in data['rates']}
            from_unit = from_unit.upper()
            to_unit = to_unit.upper()
        else:
            options = rates[mode]
        if from_unit not in options or to_unit not in options:
            await itx.response.send_message("Your unit conversion things need to be options that are in the list/database (as given by the autocomplete)!",ephemeral=True)
            return
        base_value = (value + options[from_unit][0]) / options[from_unit][1]
        # base_value is essentially the "x" in the conversion rates
        #      {"Celcius": [273.15, 1],
        #       "Fahrenheit": [459.67, 1.8]}
        # x = (273.15 + C degrees Celcius) / 1
        # result = x * 1.8 - 459.67
        result = (base_value * options[to_unit][1]) - options[to_unit][0]
        result = round(result,12)
        if mode == "currency":
            await itx.response.send_message(f"Converting {mode} from {value} {from_unit} to {result} {options[to_unit][2]}", ephemeral=not public)
        else:
            await itx.response.send_message(f"Converting {mode} from {value} {from_unit} to {to_unit}: {result} {options[to_unit][2]}", ephemeral=not public)

async def setup(client):
    await client.add_cog(OtherAddons(client))
    await client.add_cog(SearchAddons(client))
