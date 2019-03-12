# Boards
boards = {
    #Japanese Culture
    "a" : ["Anime and Manga", "favicon-ws.ico", "styles-ws.css"],
    "c" : ["Anime/Cute", "favicon-ws.ico", "styles-ws.css"],
    "w" : ["Anime/Wallpapers", "favicon-ws.ico", "styles-ws.css"],
    "m" : ["Mecha", "favicon-ws.ico", "styles-ws.css"],
    "cgl" : ["Cosplay and EGL", "favicon-ws.ico", "styles-ws.css"],
    "cm" : ["Cute/Male", "favicon-ws.ico", "styles-ws.css"],
    "f" : ["Flash", "favicon.ico", "styles.css"],
    "n" : ["Transportation", "favicon-ws.ico", "styles-ws.css"],
    "jp" : ["Otaku Culture", "favicon-ws.ico", "styles-ws.css"], 
    "vp" : ["Pokemon", "favicon-ws.ico", "styles-ws.css"],
    #Interests
    "v" : ["Video Games", "favicon-ws.ico", "styles-ws.css"],
    "vg" : ["Video Games Generals", "favicon-ws.ico", "styles-ws.css"],
    "vr" : ["Retro Games", "favicon-ws.ico", "styles-ws.css"],
    "co" : ["Comics & Cartoons", "favicon-ws.ico", "styles-ws.css"],
    "g" : ["Technology", "favicon-ws.ico", "styles-ws.css"],
    "tv" : ["Television & Film", "favicon-ws.ico", "styles-ws.css"],
    "k" : ["Weapons", "favicon-ws.ico", "styles-ws.css"],
    "o" : ["Auto", "favicon-ws.ico", "styles-ws.css"],
    "an" : ["Animals & Nature", "favicon-ws.ico", "styles-ws.css"],
    "tg" : ["Traditional Games", "favicon-ws.ico", "styles-ws.css"],
    "qst" : ["Quests",  "favicon-ws.ico", "styles-ws.css"],
    "sp" : ["Sports", "favicon-ws.ico", "styles-ws.css"],
    "asp" : ["Alternative Sports", "favicon-ws.ico", "styles-ws.css"],
    "sci" : ["Science & Math", "favicon-ws.ico", "styles-ws.css"],
    "int" : ["International",  "favicon-ws.ico", "styles-ws.css"],
    "out" : ["Outdoors", "favicon-ws.ico", "styles-ws.css"],
    "toy" : ["Toys", "favicon-ws.ico", "styles-ws.css"],
    "biz" : ["Business & Finance", "favicon-ws.ico", "styles-ws.css"],
    #Creative 
    "i" : ["Oekaki", "favicon.ico", "styles.css"],
    "po" : ["Papercraft & Origami", "favicon-ws.ico", "styles-ws.css"],
    "p" : ["Photography", "favicon-ws.ico", "styles-ws.css"],
    "ck" : ["Food & Cooking", "favicon-ws.ico", "styles-ws.css"],
    "ic" : ["Artwork/Critique", "favicon.ico", "styles.css"],
    "wg" : ["Wallpapers/General", "favicon.ico", "styles.css"],
    "mu" : ["Music", "favicon-ws.ico", "styles-ws.css"],
    "fa" : ["Fashion", "favicon-ws.ico", "styles-ws.css"],
    "3" : ["3DCG", "favicon-ws.ico", "styles-ws.css"],
    "gd" : ["Graphic Design", "favicon-ws.ico", "styles-ws.css"],
    "diy" : ["Do-It-Yourself", "favicon-ws.ico", "styles-ws.css"],
    "wsg" : ["Worksafe GIF", "favicon-ws.ico", "styles-ws.css"],
    #Adult
    "s" : ["Beautiful Women", "favicon.ico", "styles.css"],
    "hc" : ["Hardcore", "favicon.ico", "styles.css"],
    "hm" : ["Handsome Men", "favicon.ico", "styles.css"],
    "h" : ["Hentai", "favicon.ico", "styles.css"],
    "e" : ["Ecchi", "favicon.ico", "styles.css"],
    "u" : ["Yuri", "favicon.ico", "styles.css"],
    "d" : ["Hentai/Alternative", "favicon.ico", "styles.css"],
    "y" : ["Yaoi", "favicon.ico", "styles.css"],
    "t" : ["Torrents", "favicon.ico", "styles.css"],
    "hr" : ["High Resolution", "favicon.ico", "styles.css"],
    "gif" : ["Adult GIF", "favicon.ico", "styles.css"],
    #Other
    "trv" : ["Travel", "favicon-ws.ico", "styles-ws.css"],
    "fit" : ["Fitness", "favicon-ws.ico", "styles-ws.css"],
    "x" : ["Paranormal", "favicon-ws.ico", "styles-ws.css"],
    "lit" : ["Literature", "favicon-ws.ico", "styles-ws.css"],
    "adv" : ["Advice","favicon-ws.ico", "styles-ws.css"],
    "lgbt" : ["LGBT", "favicon-ws.ico", "styles-ws.css"],
    "mlp" : ["Pony", "favicon-ws.ico", "styles-ws.css"],
    #MISC
    "b" : ["Random", "favicon.ico", "styles.css"],
    "r" : ["Requests", "favicon.ico", "styles.css"],
    "r9k" : ["ROBOT9001", "favicon.ico", "styles.css"],
    "pol" : ["Politically Incorrect", "favicon.ico", "styles.css"],
    "soc" : ["Cams & Meetups", "favicon.ico", "styles.css"], 
    "s4s" : ["Shit 4chan Says", "favicon.ico", "styles.css"]
}

'''
Creates a new file with thread id as filename and adds
the html header information.
thread - thread number from url as string
cat - board thread belongs to (g, sci, lit etc...) as string
'''
def writeHeader(thread, cat):
    with open("{}/{}.html".format(cat, thread), "w") as html_file:
        html_file.write("<!DOCTYPE html>\n<html>\n<head>\n")
        html_file.write('\t<meta charset="utf-8"/>\n')
        html_file.write('\t<link rel="stylesheet" href="../css/{}">\n'.format(boards[cat][2]))
        html_file.write('\t<link rel="shortcut icon" type="image/png" href="favicon/{}">\n'.format(boards[cat][1]))
        html_file.write('\t<title>' + thread + '</title>\n')
        html_file.write('</head>\n<body>\n')
        html_file.write('<div class="boardTitle">/{}/ - {}</div>'.format(cat, boards[cat][0]))

'''
Appends to a file the OPs post with image.

thread - thread number from url as string
cat - board thread belongs to (g, sci, lit etc...) as string
op_name - OP's name  (usually anonymous) as string
op_img_src - location of image either on 4chan cdn or local with files preserved as string
op_img_text - original file name of image as string
op_date - date the post was made as string
op_message - message with original html formatting as string
'''
def writeOP(thread, cat, op_pid, op_name, op_img_src, op_img_text, op_date, op_message):
    with open("{}/{}.html".format(cat, thread), "a+") as html_file:
        # Title with link to media
        html_file.write('\t<div id="{}" class="post op">\n'.format(op_pid))
        html_file.write('\t\t<span class="name">{}</span>\n'.format(op_name))
        html_file.write('\t\tFile:\n')
        html_file.write('\t\t<a id="postlink" href="{}">{}</a>\n'.format(op_img_src, op_img_text))
        html_file.write('\t\t{}\n\t\t<br>\n'.format(op_date))

        # Media
        if op_img_src[-4:] == 'webm':
            html_file.write('\t\t<p style="float: left;">\n')
            html_file.write('\t\t\t<video height="450" controls>\n')
            html_file.write('\t\t\t\t<source src="{}" type="video/webm">\n\t\t\t</video>\n\t\t</p>\n'.format(op_img_src))

        else:
            html_file.write('\t\t<p style="float: left;">\n')
            html_file.write('\t\t\t<img src="{}" style="max-height: 250px">\n\t\t</p>\n'.format(op_img_src))

        # Message beside media
        html_file.write('\t\t<p style="float: left;">\n')
        html_file.write('\t\t\t{}\n'.format(op_message))

        # Fit the background with the text + media
        html_file.write('\t\t<div style="clear: both;"></div>\n\t</div>\n')

'''
Appends to a file the a reply with an image if passed in
'''
def writeReply(thread, reply_pid, reply_name, reply_img_src, reply_img_text, reply_date, reply_message, cat):
    with open("{}/{}.html".format(cat, thread), "a+") as html_file:
        # Title with link to media
        html_file.write('\t<div id="{}" class="post reply">\n'.format(reply_pid))
        html_file.write('\t\t<span class="name">{}</span>\n'.format(reply_name))

        # Media
        if reply_img_src != '':
            html_file.write('\t\tFile:\n')
            html_file.write('\t\t<a id="postlink" href="{}">{}</a>\n\t\t'.format(reply_img_src, reply_img_text))
        html_file.write('\t\t{}\n\t\t<br>\n'.format(reply_date))

        if reply_img_src != '':
            if reply_img_src[-4:] == 'webm':
                html_file.write('\t\t<p style="float: left;">\n')
                html_file.write('\t\t\t<video height="450" controls>\n')
                html_file.write('\t\t\t\t<source src="{}" type="video/webm">\n\t\t\t</video>\n\t\t</p>\n'.format(reply_img_src))

            else:
                html_file.write('\t\t<p style="float: left;">\n')
                html_file.write('\t\t\t<img src="{}" style="max-height: 250px">\n\t\t</p>\n'.format(reply_img_src))

        # Message beside media
        html_file.write('\t\t<p style="float: left;">\n')
        html_file.write('\t\t\t{}\n'.format(reply_message))

        # Fit the background with the text + media
        html_file.write('\t\t<div style="clear: both;"></div>\n\t</div>')