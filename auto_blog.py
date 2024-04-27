from dependecies import get_first_and_second_letter,add_html_elements,tag_and_and_attribute_dic,create_blog_post_info,create_blog_post_link


start_line_number = 36
blog_post_file_path = "C:/Users/mona_gmg/Desktop/automate_post/text_init.txt"
source_file_path = "C:/Users/mona_gmg/Desktop/automate_post/model.txt"
post_info_path = "C:/Users/mona_gmg/Desktop/automate_post/post_info.txt"

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
tools_file_path = f"C:/Users/mona_gmg/Desktop/front-my-site/realworldprojectdev-front/src/blog_posts/{folder_name}.js"
post_blog_props = {
    "big_title" : '{' + f"{post_name.lower()}.title" + "}",
    "description" : '{' + f"{post_name.lower()}.description" + "}",
    "author_picture" : '{' + f"{post_name.lower()}.authorPicture" + "}",
    "author_name" : '{' + f"{post_name.lower()}.authorName" + "}",
    "post_date" : '{' + f"{post_name.lower()}.date" + "}",
    "author_present" : '{' + f"{post_name.lower()}.authorPresent" + "}",
    "relative_link" : '{' + f"{post_name.lower()}.relativeLink" + "}",

}

 

def get_first_and_second_letter(blog):
    first_and_second_letter = blog[0:2]

    return first_and_second_letter

def add_html_elements(first_and_second_letter,blog):
    modify_blog_line = blog[2:]
    tab = "\t" + "\t" +"\t" +"\t" +"\t" 
    new_blog_line = tab + tag_and_and_attribute_dic[first_and_second_letter]["open"] + modify_blog_line + tab  + tag_and_and_attribute_dic[first_and_second_letter]["close"] +"\n"

    return new_blog_line


model_list = []
blog_post_list = []
new_blog_post_list = []

# ------open files--------
with open(post_info_path,"r") as post_file, open(source_file_path,"r") as source_file, open(blog_post_file_path,"r") as blog_post_file: 
    post_info_list = post_file.readlines()
    model_list = source_file.readlines()
    blog_post_list = blog_post_file.readlines()
     
# --------create recup images and add post info in the file----------
post_images_recup = post_info_list[6:]
with open(tools_file_path,"a") as tools_file:
    tools_file.writelines(create_blog_post_info(post_name,create_blog_post_link(post_info_list[0]),post_info_list[0],post_info_list[1],post_info_list[2],post_info_list[3],post_info_list[4],post_info_list[5],post_images_recup))


# -------text-init modif and add tags-------
for blog in blog_post_list :

    first_and_second_letter = get_first_and_second_letter(blog)

    if first_and_second_letter == "pa" :  
        new_blog_line = add_html_elements(first_and_second_letter,blog,img_path)
    elif first_and_second_letter == "h2" :  
       
        new_blog_line = add_html_elements(first_and_second_letter,blog,img_path)
    elif first_and_second_letter == "h3" :  
       
        new_blog_line = add_html_elements(first_and_second_letter,blog,img_path)
    elif first_and_second_letter == "im" : 
        new_blog_line = add_html_elements(first_and_second_letter,blog,img_path)


    new_blog_post_list.append(new_blog_line)
    
# -------add blog into model-------
for new in new_blog_post_list : 
    model_list.insert(start_line_number - 1,new)
    start_line_number += 1

# -----------create file and add content---------
with open(destination_file_path,"w") as destination_file : 
    destination_file.writelines(model_list)



