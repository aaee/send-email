from random import seed, choice
def create_content_ice_breaker(dir_abs):
    font_family = "'Open Sans','Helvetica Neue',Helvetica,Arial,sans-serif"
    text = """

    <div style="margin-left:20%; margin-right:20%">
    <h4 style="font-family:{font_family};font-size:20px;font-style:normal;font-weight:bold;line-height:150%;letter-spacing:1px;text-align:center">Good Morning Everyone!!!</h4>

    <p style="text-align: center;"><img src="https://img.icons8.com/doodle/96/000000/sun--v1.png"/>
    <p style="font-family:{font_family};font-size:18px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center">I would like to brighten up the start of your day by sharing a super funny joke. Here you have:<span>&nbsp;</span></p>
    <hr style="text-align:center;color:gray;border: 0 none;border-top:dotted 1px;">
    <p style="text-align: center;"><img src="https://img.icons8.com/doodle/96/000000/garland.png"/>
 
    <p style="color:#43404d;font-family:{font_family};font-size:16px;font-style:italic;font-weight:normal;line-height:120%;letter-spacing:2px;text-align:center"><span>{joke}</span></p>

    <hr style="text-align:center;color:gray;border: 0 none;border-top:dotted 1px;">

    
    <p style="font-family:{font_family};font-size:18px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center">Moreover, I would like to share some wisdom about <strong> {topic}</strong>. Here you have a super deep and useful quote. Please reflect on it and try to find its meaning and moral.<span>&nbsp;</span></p>
    <hr style="text-align:center;color:gray;border: 0 none;border-top:dotted 1px;">
    <p style="text-align: center;"><img src="https://img.icons8.com/bubbles/100/000000/comments.png"/>

    <p style="color:#43404d;font-family:{font_family};font-size:16px;font-style:italic;font-weight:normal;line-height:120%;letter-spacing:2px;text-align:center"><span>"{quote}"</span></p>
    <p style="color:#43404d;font-family:{font_family};font-size:16px;font-style:normal;font-weight:normal;line-height:120%;letter-spacing:2px;text-align:center"><span>-- {by}</span></p>

    <hr style="text-align:center;color:gray;border: 0 none;border-top:dotted 1px;">

    <p style="text-align: center;"><img src="https://img.icons8.com/officel/80/000000/idea.png"/>
    <p style="font-family:{font_family};font-size:18px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center">Any thoughts? I'm sure you can share something interesting!<span>&nbsp;</span></p>

   
    <p style="font-family:{font_family};font-size:18px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center">Have an awesome day! <span>&nbsp;</span></p>

    <p style="font-family:{font_family};font-size:18px;font-style:normal;font-weight:normal;line-height:100%;letter-spacing:1px;text-align:center">Ali's bot on behalf of Ali :) <span>&nbsp;</span></p>
    </div>
    """



    with open(dir_abs + 'Quotes.csv', 'r') as quotes_file:
        # prepare a sequence
        lines_quote = [i for i in range(75900)]
        # make a choice
        selection_quote = choice(lines_quote)
        daily_quote = quotes_file.readlines()[selection_quote]
        daily_quote = daily_quote.rstrip()
        daily_quote = daily_quote.split(';')
        # print(daily_quote)
    
    # source of jokes: https://github.com/amoudgl/short-jokes-dataset
    with open(dir_abs + 'reddit-cleanjokes.csv', 'r') as jokes_file:
        # choose a line
        lines_joke = [i for i in range(1,1622)]  
        selection_joke = choice(lines_joke)    
        daily_joke = jokes_file.readlines()[selection_joke]
        daily_joke = daily_joke.split(',', maxsplit=1)
      
    return text.format(font_family=font_family, joke=daily_joke[1], quote=daily_quote[0], by=daily_quote[1], topic=daily_quote[2])

