from browser import document as doc, html
from browser import window, alert, console

def on_success(doc, global_vars):
    update_table(doc, global_vars)


def update_table(doc, global_vars):
    for row in doc["var_accordion"]:
        row.remove()
    for k,v in global_vars["editor_ns"].items():
        card_div = html.DIV(Class="card")
        card_header = html.DIV(id=f"h_{k}", Class="card-header", **{"data-toggle":"collapse", "data-target":f"#c_{k}", "aria-expanded":"false", "aria-controls":f"c_{k}"})
        
        card_header_varname = html.SPAN("", Class="card_header_inner")
        card_header_varvalue = html.SPAN("", Class="card_header_inner card_header_inner_value")
        
        card_header_varname <= html.P(k, Class="card_font card_header_text") 
        card_header_varvalue <= html.P(repr(v), Class="card_font card_header_text", **{"data-toggle":"collapse", "data-target":f"#c_{k}", "aria-expanded":"false", "aria-controls":f"c_{k}"}) 
        
        card_header <= card_header_varname
        card_header <= card_header_varvalue
        card_div <= card_header

        card_content = html.DIV(id=f"c_{k}", Class="collapse hide card_content_root", **{"aria-labelledby":f"h_{k}", "data-parent":"#var_accordion"})
        card_content <= html.DIV("[object information table to be added]", Class="card-body card_font")
        
        
        card_div <= card_content
        doc["var_accordion"] <= card_div