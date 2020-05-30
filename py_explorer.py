from browser import document as doc, html
from browser import window, alert, console

def on_success(doc, global_vars):
    update_table(doc, global_vars)


def update_table(doc, global_vars):
    for row in doc["var_accordion"]:
        row.remove()
    for k,v in global_vars["editor_ns"].items():
        card_div = html.DIV(Class="card")
        card_header = html.DIV(id=f"h_{k}", Class="card-header")
        card_header <= html.BUTTON(k, Class="card_font btn btn-link btn-block text-left", **{"data-toggle":"collapse", "data-target":f"#c_{k}", "aria-expanded":"false", "aria-controls":f"c_{k}"}) 
        card_div <= card_header

        card_content = html.DIV(id=f"c_{k}", Class="collapse hide", **{"aria-labelledby":f"h_{k}", "data-parent":"#var_accordion"})
        card_content <= html.DIV(repr(v), Class="card-body card_font")
        card_div <= card_content
        doc["var_accordion"] <= card_div