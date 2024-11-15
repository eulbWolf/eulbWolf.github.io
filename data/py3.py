class HTMLTemplateModifier:
    def __init__(self, template_content):
        self.template_content = template_content

    def insert_custom_stylesheet(self, stylesheet_link):
        closing_head_tag_position = self.template_content.rfind('</head>')
        modified_content = (
            self.template_content[:closing_head_tag_position]
            + stylesheet_link
            + '\n'
            + self.template_content[closing_head_tag_position:]
        )
        self.template_content = modified_content

    def insert_navbar(self, navbar_content):
        opening_body_tag_position = self.template_content.find('<body>') + len('<body>')
        modified_content = (
            self.template_content[:opening_body_tag_position]
            + '\n'
            + navbar_content
            + self.template_content[opening_body_tag_position:]
        )
        self.template_content = modified_content

    def insert_main_content_start(self, main_content_start):
        closing_navbar_div_tag = '</div><!-- navcloses-->'
        closing_navbar_div_position = (
            self.template_content.find(closing_navbar_div_tag)
            + len(closing_navbar_div_tag)
        )
        modified_content = (
            self.template_content[:closing_navbar_div_position]
            + '\n'
            + main_content_start
            + self.template_content[closing_navbar_div_position:]
        )
        self.template_content = modified_content

    def insert_main_content_end(self, main_content_end):
        closing_body_tag_position = self.template_content.rfind('</body>')
        modified_content = (
            self.template_content[:closing_body_tag_position]
            + '\n'
            + main_content_end
            + self.template_content[closing_body_tag_position:]
        )
        self.template_content = modified_content

'''

CONTENT STRINGS

'''
stylesheet_link = '<link rel="stylesheet" href="css/sidenav.css"/>'
navbar_content = '''
<div class="sidenav" style="background-image:linear-gradient( to bottom, #9acd32, #ffeb3b, #006400); padding: 10px 0;">
    <a href="index.html"> home </a>
    <br></br>
    <a href="ainsomnia.html"> adolescent insomnia study </a>
    <br></br>
    <a href="mentalhealth_mexicous.html">mental health data exploration</a>
    <br></br>
    <a href="classy1.html"> sentiment analysis (classifiers)</a>
    <br></br>
    <a href="martclassifier.html"> math text classification (ml)</a>
    <br></br>
    <a href="twittertalk.html"> twitter usage and age(ml)</a>
    <br></br>
</div><!-- nav bar div-->
'''
main_content_start = '<div class="main-content">'
main_content_end = '</div> <!-- main content closing -->'

modifier = HTMLTemplateModifier(template_content)

# Apply modifications
modifier.insert_custom_stylesheet(stylesheet_link)
modifier.insert_navbar(navbar_content)
modifier.insert_main_content_start(main_content_start)
modifier.insert_main_content_end(main_content_end)

# Print the modified content
print(modifier.template_content)

