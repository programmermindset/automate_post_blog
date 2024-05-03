tag_and_and_attribute_dic ={
    "pa" : {
        "open" : '<p className="paragraph">',
        "close" : '</p>'
    },
    "h2" : {
        "open" : '<h2 className="h2-title">',
        "close" : "</h2>"
    },
    "h3" : {
        "open" : '<h3 className="h3-title">',
        "close" : "</h3>"
    },
    "ol" : {
        "open" : '<ol className="web-cat-list">',
        "close" : '</ol>'
    },
    "li" : {
        "open" : "<li>",
        "close" : "</li>"
    },
    "ul" : {
        "open" : '<ul className="web-comp-list">',
        "close" : '</ul>'
    },
    
}


def create_blog_post_info(post_name,relative_link,title,description,author_name,autho_picture,date,author_present,post_images):
    new_line_plus_tab = "\n" + "\t"
    return f"\nexport const {post_name} = " + '{' + new_line_plus_tab + f"relativeLink : '{relative_link}',"+ new_line_plus_tab + f"title : '{title}',"+ new_line_plus_tab + f"description : '{description}',"+ new_line_plus_tab + f"authorName : '{author_name}',"+ new_line_plus_tab + f"authorPicture : '{autho_picture}',"+ new_line_plus_tab + f"date : '{date}',"+ new_line_plus_tab + f"authorPresent : '{author_present}',"+ new_line_plus_tab + f"post_images : {post_images} "+ new_line_plus_tab + "}"
  
def create_blog_post_link(title):
    link = ""
    for t in title :
        if t == " " or t == "," or t =="'": 
            t = "_"
        link = link + t

    return link

def get_first_and_second_letter(blog):
    first_and_second_letter = blog[0:2]

    return first_and_second_letter

def add_html_elements(first_and_second_letter,blog,post_name,image_index):
    modify_blog_line = blog[2:]
    tab = "\t" + "\t" +"\t" +"\t" +"\t" 
    if first_and_second_letter != "im" : 
        new_blog_line = tab + tag_and_and_attribute_dic[first_and_second_letter]["open"] + modify_blog_line + tab  + tag_and_and_attribute_dic[first_and_second_letter]["close"] +"\n"
    else : 
        new_blog_line = tab + "<img src={"+ post_name + ".post_images["+str(image_index)+']} alt="" />'
    return new_blog_line

def html_entities(texts):
    
    new_text = ""
    if texts != "\n":
        for text in texts: 
            if text == "!" : 
                new_text += "&#33;"
            elif text == '"' : 
                new_text += "&#34;"
            elif text == '#' : 
                new_text += "&#35;"
            elif text == '$' : 
                new_text += "&#36;"
            elif text == '%' : 
                new_text += "&#37;"
            elif text == '&' : 
                new_text += "&#38;"
            elif text == "'" : 
                new_text += "&#39;"
            elif text == '(' : 
                new_text += "&#40;"
            elif text == ')' : 
                new_text += "&#41;"
            elif text == '*' : 
                new_text += "&#42;"
            elif text == '+' : 
                new_text += "&#43;"
            elif text == '-' : 
                new_text += "&#45;"
            elif text == '/' : 
                new_text += "&#47;"
            elif text == ':' : 
                new_text += "&#58;"
            elif text == ';' : 
                new_text += "&#59;"
            elif text == '=' : 
                new_text += "&#61;"
            elif text == '<' : 
                new_text += "&#60;"
            elif text == '?' : 
                new_text += "&#63;"
            elif text == '@' : 
                new_text += "&#64;"
            elif text == '[' : 
                new_text += "&#91;"
            elif text == ']' : 
                new_text += "&#93;"
            else : 
                new_text += text
        
    
    return new_text
