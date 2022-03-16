from jinja2 import Environment, BaseLoader,Template
from base64 import b64encode
from weasyprint import HTML


jinja_config = {
            "block_start_string": "\BLOCK{",  # noqa: W605
            "block_end_string": "}",
            "variable_start_string": "\VAR{",  # noqa: W605
            "variable_end_string": "}",
            "comment_start_string": "\#{",  # noqa: W605
            "comment_end_string": "}",
            "line_statement_prefix": "%%",
            "line_comment_prefix": "%#",
            "trim_blocks": True,
            "autoescape": False,
            "loader": BaseLoader(),
            "cache_size": 0
}

data = {
    
}

while True:
    with open('index.html','r') as html:
        """
            nesse open ele lê o arquivo index.html que vai ser o template criado
        """
        html_string = html.read()
        env = Environment(**jinja_config)
        hmtl_template : Template = env.from_string(html_string)
        html_rendered = hmtl_template.render(data)

        pdf = HTML(string=html_rendered).write_pdf()
        with open('result.pdf','wb') as pdf_file:
            pdf_file.write(pdf)
    
    input("Press enter to update the pdf\n")