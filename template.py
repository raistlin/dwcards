__author__ = 'vsh'

templatehtml = """\
<html><head>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js"></script>
    <script src="jquery.boxfit.js"></script>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
@media print { @page { size: landscape; margin: 0.2cm } }
table
{
border-collapse:collapse;
page-break-after: always;
margin-left: auto ;
margin-right: auto ;
}
table, th, td
{
border: 1px solid transparent;
}
tr
{
height:4.6cm;
}

tr.hruler
{
height: 1px;
border: 0px;
background-color:transparent;
}

td
{
width:7.8cm;
padding:0.2cm;
position: relative;
z-index: 1;
}
td.hruler
{
padding:0px;
}
td.vruler
{
width: 1px;
border: 0px;
background-color:transparent;
padding:0px;
}

ul
{
padding-top: 0px;
margin-top: 0px;
}
div.descript
{
height:4.5cm;
width:7.8cm;
text-align: left;
}
div.name
{
text-align: center;
width:100%;
font-weight:bold;
font-size: 22px;
margin-top:0px;
}

div.leftpic
{
    width:6mm;
    height:6mm;
    float:left;
}
div.rightpic
{
    width:6mm;
    height:6mm;
    float:right;
}

img.suit
{
    width:6mm;
}

div.left
{
width:45%;
float:left;
padding-right:5%;
}

div.right
{
width:45%;
float:right;
padding-left:5%;

}
div.footer
{
padding-top:0.1px;

width:100%;
clear:both;
border-color:grey;
}
img.color
{
height:100%;
width:100%;
}
div.vruler_show
{
height:10px;
width:1px;
}
div.vruler_hide
{
height:165px;
width:1px;
}
div.hruler_left
{
height:1px;
width:10px;
float:left;
}
div.hruler_right
{
height:1px;
width:10px;
float:right;
}

</style>
</head>
<body>
<table><tr><td></td></tr></table>
"""

templatehtmlend='''</body></html>'''

cross = '<div class="vcross" style="{0}:-0.75px; {1}:-6px;"></div><div class="hcross" style="{0}:-6px; {1}:-0.75px;"></div>'
rightbottomcrosshtml = cross.format('right', 'bottom')
leftbottomcrosshtml = cross.format('left', 'bottom')
righttopcrosshtml = cross.format('right', 'top')
lefttopcrosshtml = cross.format('left', 'top')


vrulershtml='''<tr class="vrulers">
<td class="corner">%s</td><td class="vrulers">%s</td><td class="vrulers">%s</td><td class="vrulers">%s</td><td class="corner"></td>
</tr>
'''%(rightbottomcrosshtml,rightbottomcrosshtml,rightbottomcrosshtml,rightbottomcrosshtml)

beginrow='''<td class="hrulers">%s</td>'''%(rightbottomcrosshtml)
endrow = '''<td class="hrulers"></td>'''


