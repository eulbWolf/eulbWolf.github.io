def insert_custom_stylesheet(template_path, output_path, stylesheet_link):
    # Read the template content
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    # Find the position of the closing </head> tag
    closing_head_tag_position = template_content.rfind('</head>')

    # Insert the custom stylesheet link right above the </head> tag
    modified_content = template_content[:closing_head_tag_position] + stylesheet_link + '\n' + template_content[closing_head_tag_position:]

    # Write the modified content to the output file
    with open(output_path, 'w') as output_file:
        output_file.write(modified_content)

# Example usage
template_path = 'sample_template.html'
output_path = 'modified_output.html'
stylesheet_link = '<link rel="stylesheet" href="css/sidenav.css"/>'

insert_custom_stylesheet(template_path, output_path, stylesheet_link)
#
#
#
#def insert_navbar(template_path, output_path, navbar_content):
#    # Read the template content
#    with open(template_path, 'r') as template_file:
#        template_content = template_file.read()
#
#    # Find the position of the opening <body> tag
#    opening_body_tag_position = template_content.find('<body>') + len('<body>')
#
#    # Insert the custom navbar content right after the opening <body> tag
#    modified_content = template_content[:opening_body_tag_position] + '\n' + navbar_content + template_content[opening_body_tag_position:]
#
#    # Write the modified content to the output file
#    with open(output_path, 'w') as output_file:
#        output_file.write(modified_content)
#
## Example usage
#template_path = 'sample_template.html'
#output_path = 'modified_output.html'
#
#navbar_content = '''
#	<div class="sidenav" style="background-image:linear-gradient( to bottom, #9acd32, #ffeb3b, #006400); padding: 10px 0;">
#		<a href="index.html"> home </a>
#		<br></br>
#		<a href="ainsomnia.html"> adolescent insomnia study </a>
#		<br></br>
#		<a href="mentalhealth_mexicous.html">mental health data exploration</a>
#		<br></br>
#		<a href="classy1.html"> sentiment analysis (classifiers)</a>
#		<br></br>
#		<a href="martclassifier.html"> math text classification (ml)</a>
#		<br></br>
#		<a href="twittertalk.html"> twitter usage and age(ml)</a>
#		<br></br>
#	</div><!--navcloses-->
#'''
#
#insert_navbar(template_path, output_path, navbar_content)
#
#
#
#def insert_main_content(template_path, output_path, main_content_start):
#    # Read the template content
#    with open(template_path, 'r') as template_file:
#        template_content = template_file.read()
#
#    # Find the position of the closing </div> tag for the navbar
#    closing_navbar_div_tag = '</div> <!--navcloses-->'
#    closing_navbar_div_position = template_content.find(closing_navbar_div_tag) + len(closing_navbar_div_tag)
#
#    # Insert the custom main content start right after the closing </div> tag
#    modified_content = template_content[:closing_navbar_div_position] + '\n' + main_content_start + template_content[closing_navbar_div_position:]
#
#    # Write the modified content to the output file
#    with open(output_path, 'w') as output_file:
#        output_file.write(modified_content)
#
## Example usage
#template_path = 'sample_template.html'
#output_path = 'modified_output.html'
#
#main_content_start = '<div class="main-content">'
#insert_main_content(template_path, output_path, main_content_start)
#
#
#
#def insert_main_content_end(template_path, output_path, main_content_end):
#    # Read the template content
#    with open(template_path, 'r') as template_file:
#        template_content = template_file.read()
#
#    # Find the position of the closing </body> tag
#    closing_body_tag_position = template_content.rfind('</body>')
#
#    # Insert the custom main content end right before the closing </body> tag
#    modified_content = template_content[:closing_body_tag_position] + '\n' + main_content_end + template_content[closing_body_tag_position:]
#
#    # Write the modified content to the output file
#    with open(output_path, 'w') as output_file:
#        output_file.write(modified_content)
#
## Example usage
#template_path = 'sample_template.html'
#output_path = 'modified_output.html'
#
#main_content_end = '</div> <!-- main content closing -->'
#insert_main_content_end(template_path, output_path, main_content_end)
#
