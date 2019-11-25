boards = {
    #Japanese Culture
    "a" : ["Anime & Manga", "favicon-ws.ico", "variables-ws.css"],
    "c" : ["Anime/Cute", "favicon-ws.ico", "variables-ws.css"],
    "w" : ["Anime/Wallpapers", "favicon-ws.ico", "variables-ws.css"],
    "m" : ["Mecha", "favicon-ws.ico", "variables-ws.css"],
    "cgl" : ["Cosplay & EGL", "favicon-ws.ico", "variables-ws.css"],
    "cm" : ["Cute/Male", "favicon-ws.ico", "variables-ws.css"],
    "f" : ["Flash", "favicon.ico", "variables.css"],
    "n" : ["Transportation", "favicon-ws.ico", "variables-ws.css"],
    "jp" : ["Otaku Culture", "favicon-ws.ico", "variables-ws.css"], 
    #Video Games
    "v" : ["Video Games", "favicon-ws.ico", "variables-ws.css"],
    "vg" : ["Video Games Generals", "favicon-ws.ico", "variables-ws.css"],
    "vp" : ["Pokemon", "favicon-ws.ico", "variables-ws.css"],
    "vr" : ["Retro Games", "favicon-ws.ico", "variables-ws.css"],
    #Interests
    "co" : ["Comics & Cartoons", "favicon-ws.ico", "variables-ws.css"],
    "g" : ["Technology", "favicon-ws.ico", "variables-ws.css"],
    "tv" : ["Television & Film", "favicon-ws.ico", "variables-ws.css"],
    "k" : ["Weapons", "favicon-ws.ico", "variables-ws.css"],
    "o" : ["Auto", "favicon-ws.ico", "variables-ws.css"],
    "an" : ["Animals & Nature", "favicon-ws.ico", "variables-ws.css"],
    "tg" : ["Traditional Games", "favicon-ws.ico", "variables-ws.css"],
    "sp" : ["Sports", "favicon-ws.ico", "variables-ws.css"],
    "asp" : ["Alternative Sports", "favicon-ws.ico", "variables-ws.css"],
    "sci" : ["Science & Math", "favicon-ws.ico", "variables-ws.css"],
    "his" : ["History & Humanities", "favicon-ws-ico", "variables-ws.css"],
    "int" : ["International",  "favicon-ws.ico", "variables-ws.css"],
    "out" : ["Outdoors", "favicon-ws.ico", "variables-ws.css"],
    "toy" : ["Toys", "favicon-ws.ico", "variables-ws.css"],
    #Creative 
    "i" : ["Oekaki", "favicon.ico", "variables.css"],
    "po" : ["Papercraft & Origami", "favicon-ws.ico", "variables-ws.css"],
    "p" : ["Photography", "favicon-ws.ico", "variables-ws.css"],
    "ck" : ["Food & Cooking", "favicon-ws.ico", "variables-ws.css"],
    "ic" : ["Artwork/Critique", "favicon.ico", "variables.css"],
    "wg" : ["Wallpapers/General", "favicon.ico", "variables.css"],
    "lit" : ["Literature", "favicon-ws.ico", "variables-ws.css"],
    "mu" : ["Music", "favicon-ws.ico", "variables-ws.css"],
    "fa" : ["Fashion", "favicon-ws.ico", "variables-ws.css"],
    "3" : ["3DCG", "favicon-ws.ico", "variables-ws.css"],
    "gd" : ["Graphic Design", "favicon-ws.ico", "variables-ws.css"],
    "diy" : ["Do-It-Yourself", "favicon-ws.ico", "variables-ws.css"],
    "wsg" : ["Worksafe GIF", "favicon-ws.ico", "variables-ws.css"],
    "qst" : ["Quests",  "favicon-ws.ico", "variables-ws.css"],
    #Other
    "biz" : ["Business & Finance", "favicon-ws.ico", "variables-ws.css"],
    "trv" : ["Travel", "favicon-ws.ico", "variables-ws.css"],
    "fit" : ["Fitness", "favicon-ws.ico", "variables-ws.css"],
    "x" : ["Paranormal", "favicon-ws.ico", "variables-ws.css"],
    "adv" : ["Advice","favicon-ws.ico", "variables-ws.css"],
    "lgbt" : ["LGBT", "favicon-ws.ico", "variables-ws.css"],
    "mlp" : ["Pony", "favicon-ws.ico", "variables-ws.css"],
    "news" : ["Current News", "favicon-ws.ico", "variables-ws.css"],
    "wsr" : ["Worksafe Requests", "favicon-ws.ico", "variables-ws.css"],
    "vip" : ["Very Important Posts", "favicon-ws.ico", "variables-ws.css"],
    #Misc.
    "b" : ["Random", "favicon.ico", "variables.css"],
    "r9k" : ["ROBOT9001", "favicon.ico", "variables.css"],
    "pol" : ["Politically Incorrect", "favicon.ico", "variables.css"],
    "bant" : ["International/Random", "favicon.ico", "variables.css"],
    "soc" : ["Cams & Meetups", "favicon.ico", "variables.css"], 
    "s4s" : ["Shit 4chan Says", "favicon.ico", "variables.css"],
    #Adult
    "s" : ["Beautiful Women", "favicon.ico", "variables.css"],
    "hc" : ["Hardcore", "favicon.ico", "variables.css"],
    "hm" : ["Handsome Men", "favicon.ico", "variables.css"],
    "h" : ["Hentai", "favicon.ico", "variables.css"],
    "e" : ["Ecchi", "favicon.ico", "variables.css"],
    "u" : ["Yuri", "favicon.ico", "variables.css"],
    "d" : ["Hentai/Alternative", "favicon.ico", "variables.css"],
    "y" : ["Yaoi", "favicon.ico", "variables.css"],
    "t" : ["Torrents", "favicon.ico", "variables.css"],
    "hr" : ["High Resolution", "favicon.ico", "variables.css"],
    "gif" : ["Adult GIF", "favicon.ico", "variables.css"],
    "aco" : ["Adult Cartoons", "favicon.ico", "variables.css"],
    "r" : ["Adult Requests", "favicon.ico", "variables.css"],
}

class Reply:
    def __init__(self, name, date, message, pid, img_src=None, img_text=None, subject=None):
        self.name = name
        self.date = date
        self.message = message
        self.pid = pid
        self.img_src = img_src
        self.img_text = img_text
        self.subject = subject
        self.is_img = False
        self.is_webm = False
        self.set_conditionals()
    
    def set_conditionals(self):
        if (self.img_src != ""):
            if (self.img_src[-4:] == 'webm'):
                self.is_webm = True
            else:
                self.is_img = True

class Thread:
    def __init__(self, tid, board, url):
        self.tid = tid
        self.board = board
        self.url = url
        self.set_board()
    
    def set_board(self):
        self.board_name = boards[self.board][0]
        self.fav = boards[self.board][1]
        self.css = boards[self.board][2]