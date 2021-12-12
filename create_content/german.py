from datetime import datetime


def create_content_german(dir_abs):
    font_family = "'Open Sans','Helvetica Neue',Helvetica,Arial,sans-serif"
    text = '''
    <div style="margin-left:10%; margin-right:10%">
    <h4 style="font-family:{font_family};font-size:20px;font-style:normal;font-weight:bold;line-height:150%;letter-spacing:1px;text-align:center">Hallo Blanchis Burger!</h4>
    <p style="text-align: center;"><img src="https://img.icons8.com/doodle/96/000000/sun--v1.png"/>
    <p style="font-family:{font_family};font-size:18px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center">Ich m&ouml;chte, dass wir perfekt Deutsch sprechen k&ouml;nnen. Daf&uuml;r m&uuml;ssen wir viele Redewendungen lernen.<span>&nbsp;</span></p>

    <p style="color:#43404d;font-family:{font_family};font-size:16px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:2px;text-align:center"><span>UNTEN FINDEST DU DIE HEUTIGEN REDEWENDUNGEN:</span></p>
    
    <hr style="text-align:center;color:gray;border: 0 none;border-top:dotted 1px;">

    <p style="color:#4485b8;font-family:{font_family};font-size:20px;font-style:normal;font-weight:bold;line-height:100%;text-align:center"><span>{idiom}</span></p>
    
    <hr style="text-align:center;color:gray;border: 0 none;border-top:dotted 1px;">

    <p style="color:#43404d;font-family:{font_family};font-size:16px;font-style:normal;font-weight:bold;line-height:100%;letter-spacing:1px;text-align:center"><span>W&ouml;rtliche &Uuml;bersetzung:</span></p>
    <p style="color:#43404d;font-family:{font_family};font-size:16px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center"><em>{literal_translation}</em></p>
    <p style="color:#43404d;font-family:{font_family};font-size:16px;font-style:normal;font-weight:bold;line-height:100%;letter-spacing:1px;text-align:center"><span>Englische &Uuml;bersetzung:</span></p>
    <p style="color:#43404d;font-family:{font_family};font-size:16px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center"><em>{english_translation}</em></p>
    <p style="color:#43404d;font-family:{font_family};font-size:16px;font-style:normal;font-weight:bold;line-height:100%;letter-spacing:1px;text-align:center"><span><b class="b5">Spanische</b> &Uuml;bersetzung:</span></p>
    <p style="color:#43404d;font-family:{font_family};font-size:16px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center"><em>{spanish_translation}</em></p>
    
    <hr style="text-align:center;color:gray;border: 0 none;border-top:dotted 1px;width:80%"">
    <p style="text-align: center;"><img src="{image}" alt= "" width="70%" height="auto""img" />
    
    <hr style="text-align:center;color:gray;border: 0 none;border-top:dotted 1px;"">
    
    <p style="font-family:{font_family};font-size:18px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center">Ich w&uuml;nsche dir einen sch&ouml;nen Tag!</p>
    <p style="font-family:{font_family};font-size:18px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center">Ali's german bot :)&nbsp;</p>
    <p></p>

    </div>
    '''
    # get index for idiom
    first_day = datetime.strptime('2021-06-20', '%Y-%m-%d')
    days_diff = (datetime.now() - first_day).days + 1
    #print(days_diff)

    with open(dir_abs + 'german_idioms.csv', 'r') as german_idioms:
        daily_idiom= german_idioms.readlines()[days_diff]
        daily_idiom = daily_idiom.split(';')

    print(daily_idiom[4])


    return text.format(font_family=font_family, idiom=daily_idiom[0], literal_translation=daily_idiom[1], english_translation=daily_idiom[2], spanish_translation=daily_idiom[3], image=daily_idiom[4])

