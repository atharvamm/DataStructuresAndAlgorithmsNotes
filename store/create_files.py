import os

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

store_dir = os.path.join(project_dir,"store")
html_dir = os.path.join(project_dir,"src","topics")
code_dir = os.path.join(html_dir,"code")



modes = {
    1 : "html_template",
    2 : "list_links"
}
MODE = 1

if MODE == 1:
    from string import Template
    template_path = os.path.join(store_dir, 'html_template.html')

    with open(template_path, 'r') as file:
        html_template = Template(file.read())

    values = {
        'title': "Valid Anagram",
        'link': "https://leetcode.com/problems/valid-anagram",
        'group' : "blind75"
    }

    values['fname'] = "".join(values['title'].split(" "))
    output_html = html_template.substitute(values)

    if os.path.exists(os.path.join(html_dir,f"{values['fname']}.html")) or os.path.exists(os.path.join(code_dir,f"{values['fname']}.py")):
        raise Exception("File already exist please confirm group once.")
    
    with open(os.path.join(html_dir,f"{values['fname']}.html"), 'w') as file:
        file.write(output_html)
    
    with open(os.path.join(code_dir,f"{values['fname']}.py"), 'w') as file:
        data = "\n\n"
        file.write(data)


elif MODE == 2:
    EXPECTED_GROUP = "blind75"
    import re
    directory = html_dir

    title_pattern = re.compile(r'title:\s*"([^"]+)"')
    previous_pattern = re.compile(r'previous:\s*"([^"]+)"')
    include_pattern = re.compile(r'{%\s*include\s+code.html\s+file="([^"]+)"\s*%}')

    # Function to extract details from a file
    def extract_details_from_file(filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        title_match = title_pattern.search(content)
        previous_match = previous_pattern.search(content)
        include_match = include_pattern.search(content)


        if title_match and previous_match and include_match:
            title = title_match.group(1)
            previous = previous_match.group(1)

            # Check if the previous contains "blind75"

            return {
                "file_name": os.path.basename(filepath),
                "title": title,
                "group": previous.split(r"/")[1],
                "fname": os.path.basename(filepath).split(".")[0]
            }

    results = []
    for filename in os.listdir(html_dir): 
        if filename.endswith('.html'):
            filepath = os.path.join(html_dir, filename)
            details = extract_details_from_file(filepath)
            if EXPECTED_GROUP == details["group"]:
                results.append(details)


    result_txt = ""
    for result in sorted(results, key = lambda x: x["fname"]):
        result_txt += '''<li><a href="../topics/{}/index.html">{}</a></li>'''.format(result["fname"], result["title"])
        result_txt += "\n"

    with open(os.path.join(store_dir,"links.txt"), 'w', encoding='utf-8') as f:
        f.write(result_txt)