__author__ = 'vsh'
import xml.dom.minidom
from math import ceil
import re
import os


impl = xml.dom.minidom.getDOMImplementation()
monsterdoc = impl.createDocument(None, "monsters", None)
topelement = monsterdoc.documentElement

def makeTag(tag, value):
    xname = monsterdoc.createElement(tag)
    xname.appendChild(monsterdoc.createTextNode(value))
    return xname

def splitTags(tag, values):
    for value in values.split(","):
        xname = monsterdoc.createElement(tag)
        xname.appendChild(monsterdoc.createTextNode(value.strip()))
        yield xname

def process_file(fn):

    input = open(fn, "r")
    document = input.read()
    input.close()

    dom = xml.dom.minidom.parseString(document)

    paragraphs =  dom.getElementsByTagName('h1')

    if(paragraphs.length == 1):
        monster_setting = paragraphs[0].firstChild.toxml()
    else:
        exit("more than one header")

    (main, asasfasdff ,fasdfsadf ) = document.rpartition("</Body>")


    mname = "<p aid:pstyle=\"MonsterName\">"
    monsterstext = main.split(mname)
    xmlmname='<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Root xmlns:aid="http://ns.adobe.com/AdobeInDesign/4.0/">' + mname
    monsterstext = [xmlmname + monster + "</Root>" for monster in monsterstext[1:]]




    for monster in monsterstext:

        melement = dom.createElement("monster")

        melement.appendChild(makeTag("setting", monster_setting))

        dom = xml.dom.minidom.parseString(monster)
        paragraphs =  dom.getElementsByTagName('p')
        plen = len(paragraphs)
        if plen!=2 and plen!=4 and plen!=3 and plen!=5 :
            print "can't do it! less than four or more than five paragraphs"
            print len(paragraphs)
            print monster
            continue

        has_attack = True
        has_qualities = True
        has_tags = True


        if(plen == 2):
            has_qualities=has_attack=False
            [pname, pdescription] = paragraphs
        elif plen ==3:
            has_attack=False
            [pname, pqualities, pdescription] = paragraphs
        elif plen == 4:
            has_qualities=False
            [pname, pattack, pattacktags, pdescription] = paragraphs
        elif plen == 5:
            [pname, pattack, pattacktags, pqualities, pdescription] = paragraphs


        name = pname.firstChild.toxml().rstrip('\t')
        melement.appendChild(makeTag("name", name))

        try:
            tags = pname.lastChild.firstChild.toxml()
            for xtag in splitTags("tag", tags):
                melement.appendChild(xtag)
        except:
            has_tags = False


        if has_attack:

            attacks = pattack.firstChild.toxml()

            regex = re.compile("(\S+)\s+\((.*)\)\s+(\S+)\s+HP\s+(\S+).*Armor")
            if len(regex.findall(attacks))<1:
                exit("no hp or armor")
            (attack, damage, hp, armor) = regex.findall(attacks)[0]

            melement.appendChild(makeTag("attack", attack))
            melement.appendChild(makeTag("damage", damage))
            melement.appendChild(makeTag("hp", hp))
            melement.appendChild(makeTag("armor", armor))

            attacktags = pattacktags.firstChild.firstChild.toxml()

            for xtag in splitTags("attacktag", attacktags):
                melement.appendChild(xtag)

        if(has_qualities):
            qualities = pqualities.lastChild.toxml()
            for xtag in splitTags("quality", qualities):
                melement.appendChild(xtag)


        description = pdescription.firstChild.toxml()
        melement.appendChild(makeTag("description", description.rstrip()))

        instinct = pdescription.lastChild.toxml()

        melement.appendChild(makeTag("instinct", instinct.lstrip(": ") ) )

        uls = dom.getElementsByTagName('ul')
        if(len(uls)!=1):
            exit("can't do it! more than one list")
        moves = uls[0].getElementsByTagName("li")
        for move in moves:
            melement.appendChild(makeTag("move", move.firstChild.toxml() ) )

        topelement.appendChild(melement)



for fn in os.listdir('./monster_settings'):
    process_file('./monster_settings/'+fn)

out = open ("monsters.xml", 'w')
out.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
out.write(topelement.toxml().encode("utf8"))
out.close()









