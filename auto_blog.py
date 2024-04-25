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
    }
}
tab = "\t" + "\t" +"\t" +"\t" +"\t" 
start_line_number = 32
blog_post_file_path = "C:/Users/mona_gmg/Desktop/automate_post/text_init.txt"
source_file_path = "C:/Users/mona_gmg/Desktop/automate_post/model.txt"

print("choose the destination folder : \n 1.development\n 2.courses\n 3.news\n 4.projects \n" )
destination_folder = input("destination : ")
post_name = input("enter the post name : ").capitalize()

folder_name = ""
if destination_folder == '1' or "development": 
    folder_name = "development"
elif destination_folder == "2" or "courses": 
    folder_name = "courses"
elif destination_folder == "3" or "news": 
    folder_name = "news"
elif destination_folder == "4" or "projects": 
    folder_name = "projects"

destination_file_path = f"C:/Users/mona_gmg/Desktop/front-my-site/realworldprojectdev-front/src/blog_posts/{folder_name}/{post_name}.js"

# with open(source_file_path,"r") as source_file,open(destination_file_path,"w") as destination_file : 
#     file_content = source_file.read()

#     destination_file.write(file_content)

#     print(f'the file {source_file_path} has been copied to {destination_file_path}.')

model_list = []
blog_post_list = []
new_blog_post_list = []

# ------open files--------
with open(source_file_path,"r") as source_file, open(blog_post_file_path,"r") as blog_post_file: 
    model_list = source_file.readlines()
    blog_post_list = blog_post_file.readlines()

# -------text-init modif and add tags-------
for blog in blog_post_list :
    get_first_and_second_letter = blog[0:2]
    if get_first_and_second_letter == "pa" :  
        modify_blog_line = blog[2:]
        new_blog_line = tab + tag_and_and_attribute_dic["pa"]["open"] + modify_blog_line + tab  + tag_and_and_attribute_dic["pa"]["close"] +"\n"
    elif get_first_and_second_letter == "h2" :  
        modify_blog_line = blog[2:]
        new_blog_line = tab + tag_and_and_attribute_dic["h2"]["open"] + modify_blog_line + tab  + tag_and_and_attribute_dic["h2"]["close"] + "\n"
    elif get_first_and_second_letter == "h3" :  
        modify_blog_line = blog[2:]
        new_blog_line = tab + tag_and_and_attribute_dic["h3"]["open"] + modify_blog_line + tab  + tag_and_and_attribute_dic["h3"]["close"]  +"\n"
    new_blog_post_list.append(new_blog_line)
    
# -------add blog into model-------
for new in new_blog_post_list : 
    model_list.insert(start_line_number - 1,new)
    start_line_number += 1

# -----------create file and add content---------
with open(destination_file_path,"w") as destination_file : 
    destination_file.writelines(model_list)