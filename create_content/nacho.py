from datetime import datetime
from csv import reader

def create_content_nacho(dir_abs):

    print(dir_abs)
    content = _get_content_from_csv(dir_abs)
    
    saludation = 'Buenos días enano y féliz semana!'
    line_1 = 'Este lunes te traemos un mensaje de alguién que te quiere mucho.'
    line_2 = 'Esta semana toca: {name}'.format(name=content['name'])
    message = content['message']
    images = _get_images_hmtl(content['image'])
    goodbye_line = 'Eperamos que te haya gustado. La semana que viene más! A por la semana que empieza!!!'
    text = (starter_div.format(font_family=font_family) + saludation_html.format(saludation=saludation) + 
    icon_palmtree + normal_paragraph_html.format(text=line_1) + normal_paragraph_html.format(text=line_2) + 
    dotted_line + message_paragraph_html.format(text=message) + dotted_line + images + 
    dotted_line + icon_penguin + goodbye_html.format(text=goodbye_line) + signature_html.format(text= 'Ali & Blanca :)') + '<p></p>' + '</div>')


    return text




def _get_content_from_csv(dir_abs):
    content = {}

    nacho_message = ''

    with open(dir_abs + 'mensajes_para_nacho.csv', 'r') as nacho_messages:
        csv_reader = reader(nacho_messages, delimiter=';', quotechar='"')

        for line in csv_reader:
            if len(line) == 1:
                line_updated = line[0].split(';')
            else:
                line_updated = line
            # print(line_updated)

            print('b',datetime.today().strftime('%d-%m-%Y'))
            print('b',datetime.today().strftime('%d-%m-%Y'))
            if line_updated[0] == "message" and line_updated[1] == datetime.today().strftime('%d-%m-%Y'):
            # if line_updated[0] == "message" and line_updated[1] =='28-06-2021':
                print('here')
                content['name'] = line_updated[4]
                content['message'] = line_updated[5].replace('\n', '<br>')
                print(content['message'])
                content['image'] = line_updated[6]
                break

    return content

def _get_image_embeeding_url(sharing_url):
    image_id = sharing_url.split('/')[5]
    embeeding_url = 'https://drive.google.com/uc?export=view&id={image_id}'.format(image_id=image_id)
    # print(embeeding_url)

    return embeeding_url



def _get_images_hmtl(images):
    images_as_list = images.split(',')
    images_html = ''
    for image_sharing_url in images_as_list:
        embeeding_url=_get_image_embeeding_url(image_sharing_url)
        images_html= images_html + image_html.format(image=embeeding_url)
    # print(images_html)

    return images_html






## HTML
font_family = "'Open Sans','Helvetica Neue',Helvetica,Arial,sans-serif"
starter_div = '<div style="margin-left:10%; margin-right:10%">'
saludation_html='<h4 style="font-family:'+font_family+';font-size:20px;font-style:normal;font-weight:bold;line-height:150%;letter-spacing:1px;text-align:center">{saludation}</h4>'
icon_ballons = '<p style="text-align: center;"><img src="https://img.icons8.com/officel/80/000000/party-baloons.png"/>'
icon_palmtree = '<p style="text-align: center;"><img src="https://img.icons8.com/bubbles/100/000000/beach.png"/>'
normal_paragraph_html = '<p style="font-family:'+font_family+';font-size:18px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center">{text}<span>&nbsp;</span></p>'
dotted_line ='<hr style="text-align:center;color:gray;border: 0 none;border-top:dotted 1px;">'
message_paragraph_html = '<p style="color:#43404d;font-family:'+font_family+';font-size:16px;font-style:italic;font-weight:normal;line-height:120%;letter-spacing:2px;text-align:center"><span>{text}</span></p>'
image_html = '<p style="text-align: center;"><img src="{image}" alt= "" width="70%" height="auto""img" />'
icon_penguin = '<p style="text-align: center;"><img src="https://img.icons8.com/flat-round/64/000000/pinguin--v1.png"/>'
goodbye_html = '<p style="font-family:'+font_family+';font-size:18px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center">{text}</p>'
signature_html = '<p style="font-family:'+font_family+';font-size:18px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center">{text}&nbsp;</p>'


