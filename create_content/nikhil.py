def create_content_nikhil():
    text = """
    Good Morning Nikhil!!!
    
    I just want to wish you a happy {day}th day in your new job!
    Have fun and learn a lot! 
    
    Here is your quote of the day to keep you motivated! (this time about {topic})
    
        "{quote}"
        -- {by}
        
    Best, 
    
    Ali's bot on behalf of Ali :) 
    """

    # get number of the day we are in
    first_day = datetime.strptime('2021-01-15', '%Y-%m-%d')
    # test = datetime.strptime('2021-01-28', '%Y-%m-%d')
    days_diff = (datetime.now() - first_day).days + 1
    # print(((days_diff+4)//7))
    day = days_diff - (((days_diff+4)//7) * 2)
    # print(day)



    with open(dir_abs + 'Quotes.csv', 'r') as quotes_file:
        # seed random number generator
        seed(day)
        # prepare a sequence
        sequence = [i for i in range(75900)]
        # make a choice
        selection = choice(sequence)
        daily_quote = quotes_file.readlines()[selection]
        daily_quote = daily_quote.rstrip()
        daily_quote = daily_quote.split(';')
        # print(daily_quote)

    return text.format(day=day, quote=daily_quote[0], by=daily_quote[1], topic=daily_quote[2])
