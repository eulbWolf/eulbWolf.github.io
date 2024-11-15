import random
import string

def generate_random_html_template():
    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Random Template</title>
    <style>

    </style

    </head>
    <body>
    """
    
    num_divs = random.randint(2, 5)
    for _ in range(num_divs):
        random_div = f'<div class="random-div">{generate_random_text()}</div>'
        template += random_div
    
    template += """

    </body>
    </html>
    """
    
    return template

def generate_random_text():
    text_length = random.randint(10, 30)
    random_text = ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=text_length))
    return random_text

if __name__ == "__main__":
    random_template = generate_random_html_template()
    print(random_template)

