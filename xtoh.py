from template import righttopcrosshtml,lefttopcrosshtml,\
    leftbottomcrosshtml,rightbottomcrosshtml,templatehtml,templatehtmlend
import xml.dom.minidom
from math import ceil


__author__ = 'vsh'

dom = xml.dom.minidom.parse('monsters.xml')
monsternodes = dom.getElementsByTagName('monster')

monsters = [ ]
mechs = [ ]
scripts = "\n"
setting_suits = { 'Cavern Dwellers' : 'dung.png',
                  'Lower Depths' : 'lower.png' ,
                  'Twisted Experiments': 'twisted.png',
                  'Folk of the Realm': 'folks.png',
                  'Ravenous Hordes': 'hordes.png',
                  'Planar Powers': 'planar.png',
                  'Swamp Denizens': 'swamp.png',
                  'Legions of the Undead': 'dead.png',
                  'Gnarled Woods': 'woods.png'  }


elemnum = 1

def get_value(monster, tag):
    if monster.getElementsByTagName(tag).length == 0:
        return None
    return monster.getElementsByTagName(tag)[0].firstChild.toxml()

def get_values(monster, tag):
    for value in monster.getElementsByTagName(tag):
        try:
            yield value.firstChild.toxml()
        except:
            ""

def vruler():
    return '<td class="vruler">' +\
           '<div class="vruler_show"><img src="img/color.png" class="color"/></div>' +\
           '<div class="vruler_hide"></div>' +\
           '<div class="vruler_show"><img src="img/color.png" class="color"/></div>' +\
           '</td>'

def hruler(columns):
    html='<tr class="hruler">'
    html+='<td class="vruler">' +\
          '</td>'
    for column in range (0,columns):
        html+='<td class="hruler">' +\
              '<div class="hruler_left"><img src="img/color.png" class="color"/></div>' +\
              '<div class="hruler_right"><img src="img/color.png" class="color"/></div>' +\
              '</td>'
        html+='<td class="vruler"></td>'
    html+='</tr>'
    return html


for monster in monsternodes:
    #strict
    setting = get_value(monster, 'setting')
    setting_suit = 'img/' + setting_suits[setting]
    name = get_value(monster, 'name')
    description = get_value(monster, 'description')
    instinct = get_value(monster, 'instinct')
    moves = [move for move in get_values(monster, 'move')]

    #optional
    tags = [tag for tag in get_values(monster, "tag")]
    hp = get_value(monster, "hp")
    armor = get_value(monster, "armor")
    attack = get_value(monster, "attack")
    damage = get_value(monster, "damage")
    attacktags = [attacktag for attacktag in get_values(monster, "attacktag")]
    qualities = [quality for quality in get_values(monster, "quality") ]

    monstercode = """
    <div class="descript" id="descript%i">
    <div class="leftpic"></div><div class="rightpic"><img class="suit" src="%s"></div>
    <div class="name">%s</div>
    %s
    </div>
    """ % (elemnum, setting_suit, name, description)

    monsters.append(monstercode)

    left_text = ""
    if instinct != None:
        left_text += "Instinct: " + instinct + '<br/>'
    if len(tags)>0:
        left_text += "<em>%s</em></br>"%( ", ".join(tags))
    if len(qualities) != 0:
        left_text += "Special Qualities: "
        left_text += ", ".join(qualities)

    right_text = ""

    if(hp != None):
        right_text += "%s HP " %(hp)
    if(armor != None):
        right_text += "%s Armor" %(armor)
    if(hp != None or armor != None):
        right_text += "<br/>"
    if(attack != None):
        right_text += "(%s) "%(attack)
    if(damage != None):
        right_text += damage
    if(attack != None or damage != None):
        right_text += "<br/>"
    if len(attacktags)>0:
        right_text += "<em>%s</em></br>"%( ", ".join(attacktags))

    footer_text = ""
    if(len(moves)>0):
        footer_text += "<ul><li>%s</li></ul>"%( "</li><li>".join(moves) )


    mechcode = """
        <div class="descript" id="mech%i">
        <div class="leftpic"></div><div class="rightpic"><img class="suit" src="%s"></div>
        <div class="name">%s</div>
    <div class="left">%s
    </div>
    <div class="right">
    %s
    </div>
    <div class="footer">
    %s
    </div>
    </div>
        """%(elemnum, setting_suit, name, left_text, right_text, footer_text)
    mechs.append(mechcode)

    monsterscript = """$("#descript%i").boxfit({align_center: false, align_middle: false, multiline: true, maximum_font_size: 19});\n"""%(elemnum)
    monsterscript += """$("#mech%i").boxfit({align_center: false, align_middle: false, multiline: true, maximum_font_size: 19});\n"""%(elemnum)
    scripts += monsterscript
    elemnum+=1




rows = 4
columns = 3
num_per_table = rows*columns
tables_needed = int ( ceil( len(monsters)*1.0 / num_per_table ) )
#gen_table
html = "<center>"
for table in range(0,tables_needed):
    html+= "<table>"
    html+=hruler(columns)
    for row in range (table*rows + 0, table*rows + rows):
        html+='<tr>'
        html+=vruler()
        for column in range (0,columns):
            html+='<td>'
            try:
                html+=monsters[row*columns+column]
            except IndexError:
                html+=" "
            html+='</td>'
            html+=vruler()
        html+='</tr>'
        html+=hruler(columns)
    html+='</table>'



    html+= "<table>"
    html+=hruler(columns)
    for row in range (table*rows + 0, table*rows + rows):
        html+='<tr>'
        html+=vruler()
        for column in range (0,columns):
            html+='<td>'
            backcolumn = columns- 1 -column
            try:
                html+=mechs[row*columns+backcolumn]
            except IndexError:
                html+=" "
            html+='</td>'
            html+=vruler()
        html+='</tr>'
        html+=hruler(columns)
    html+='</table>'
html+="</center>"

html+="Monsters from Dungeon World by Adam Sage and Sage LaTorra and licensed under CC-BY. Images by am_(anmcarrow@gmail.com), licensed under CC-BY-SA. Layout by Vasiliy Shapovalov and completely free to use as you like."


html+="<script>"
html+=scripts
html+="</script>"


output = templatehtml+ (html) + templatehtmlend

file = open("monstercards.html", 'w')
file.write(output.encode("utf8"))
file.close()

