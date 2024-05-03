from dependecies import get_first_and_second_letter,add_html_elements,tag_and_and_attribute_dic,create_blog_post_info,create_blog_post_link,html_entities

def main(): 

    start_line_number = 36
    blog_post_file_path = "C:/Users/mona_gmg/Desktop/automate_post/text_init.txt"
    model_file_path = "C:/Users/mona_gmg/Desktop/automate_post/model.txt"
    post_info_path = "C:/Users/mona_gmg/Desktop/automate_post/post_info.txt"

    print("choose the destination folder : \n 1.development\n 2.courses\n 3.news\n 4.projects \n" )
    destination_folder = input("destination : ")
    post_name = input("enter the post name : ")

    folder_name = ""
    if destination_folder == '1' or destination_folder == "development": 
        folder_name = "development"
    elif destination_folder == "2" or destination_folder == "courses": 
        folder_name = "courses"
    elif destination_folder == "3" or destination_folder == "news": 
        folder_name = "news"
    elif destination_folder == "4" or destination_folder == "projects": 
        folder_name = "projects"
    

    post_name_page = f"{post_name.capitalize()}Page"
    destination_file_path = f"C:/Users/mona_gmg/Desktop/front-my-site/realworldprojectdev-front/src/blog_posts/{folder_name}/{post_name_page}.js"
    tools_file_path = f"C:/Users/mona_gmg/Desktop/front-my-site/realworldprojectdev-front/src/tools/{folder_name}.js"
    app_file_path = "C:/Users/mona_gmg/Desktop/front-my-site/realworldprojectdev-front/src/App.js"

    seven_tab = "\t" + "\t" + "\t" + "\t" + "\t" +"\t" + "\t"
    new_line = "\n"
    post_blog_props = {
        "big_title" : seven_tab + '{' + f"{post_name}.title" + "}" + new_line,
        "description" : seven_tab + '{' + f"{post_name}.description" + "}" + new_line,
        "author_picture" :'{' + f"{post_name}.authorPicture" + "}",
        "author_name" : seven_tab + '{' + f"{post_name}.authorName" + "}" + new_line,
        "post_date" : seven_tab + '{' + f"{post_name}.date" + "}" + new_line,
        "author_present" : seven_tab + '{' + f"{post_name}.authorPresent" + "}" + new_line,
        "relative_link" : '{' + f"{post_name}.relativeLink" + "}",

    }


    model_list = []
    blog_post_list = []
    new_blog_post_list = []
    image_index = 0

    # ------open files--------
    with open(post_info_path,"r") as post_file, open(model_file_path,"r") as model_file, open(blog_post_file_path,"r") as blog_post_file,open(app_file_path,"r") as app_file: 
        post_info_list = post_file.readlines()
        model_list = model_file.readlines()
        blog_post_list = blog_post_file.readlines()
        app_file_list = app_file.readlines()

    # --------create recup images and add post info in the file----------
    post_image_recup_list = []
    for img in post_info_list[6:] : 
        post_image_recup_list.append(img[:-2])
    with open(tools_file_path,"a") as tools_file:
        tools_file.writelines(create_blog_post_info(post_name,create_blog_post_link(post_info_list[0][:-2]),post_info_list[0][:-2],post_info_list[1][:-2],post_info_list[2][:-2],post_info_list[3][:-2],post_info_list[4][:-2],post_info_list[5][:-2],post_image_recup_list))


    # -------text-init modif and add tags-------
    for blog in blog_post_list :
        #create html entities
        blog_with_html_ent = html_entities(blog)

        first_and_second_letter = get_first_and_second_letter(blog)
        new_blog_line = add_html_elements(first_and_second_letter,blog_with_html_ent,post_name,image_index)
        if first_and_second_letter == "im" :              
            image_index +=1

        new_blog_post_list.append(new_blog_line)
        print(blog_with_html_ent)
    # ---- add import post_info head into----
    model_list.insert(3,"import { " + post_name + ' } from "../../tools/' + folder_name +'";\n')
    # add blog title
    model_list.insert(20, post_blog_props["big_title"])
    # add authorpicture
    model_list.insert(25,seven_tab + f"<img src={post_blog_props['author_picture']} alt='' />")
    # add author name
    model_list.insert(29,post_blog_props["author_name"])
    # add date
    model_list.insert(32,post_blog_props["post_date"])
    # author name bottom
    model_list.insert(47,post_blog_props["author_name"])
    # author present
    model_list.insert(51,post_blog_props["author_present"])

    # -------add blog into model-------
    for new in new_blog_post_list : 
        model_list.insert(start_line_number - 1,new)
        start_line_number += 1

    # -----------create file and add content---------
    with open(destination_file_path,"w") as destination_file : 
        destination_file.writelines(model_list)

    # get import index
    for app in range(len(app_file_list)) : 
        if "function App()" in app_file_list[app]:
            import_index = app
        elif "{/* projects */}" in app_file_list[app] : 
            new_section_link_index = app 
        elif "{/* news */}" in app_file_list[app] : 
            dev_section_link_index = app 
        elif "{/* courses */}" in app_file_list[app] : 
            project_section_link_index = app 
        elif "</Routes>" in app_file_list[app] : 
            courses_section_link_index = app 

    # import file in the app.js and blog relative link
    app_file_list.insert(import_index-1,"import {"+post_name_page+ '}' + " from './blog_posts/" + folder_name + "/"+post_name_page+"';\n" + "import {" + post_name + "} from" + f"'./tools/{folder_name}';\n")
    
    # import route index

    # add link inside app file
    blog_link_app_file = "\t"+ "\t"+ "\t"+"<Route path = {`/$"+post_blog_props["relative_link"]+"`} element ={<" + post_name_page + "/>} />" + new_line 
    if folder_name == "development":
        app_file_list.insert(dev_section_link_index + 1 ,blog_link_app_file)
    elif folder_name == "courses" : 
        app_file_list.insert(courses_section_link_index + 1,blog_link_app_file)
    elif folder_name == "news": 
        app_file_list.insert(new_section_link_index + 1,blog_link_app_file)
    elif folder_name == "projects" : 
        app_file_list.insert(project_section_link_index + 1,blog_link_app_file)

    with open(app_file_path,"w") as destination_app_file:
        destination_app_file.writelines(app_file_list)


if __name__ == "__main__" :
    main() 