import myc
import my_parser
import pygame

def create_project():
    # arg may or may not set the project obj
    # so look at save_file_path set
    # if set than good
    # else see if quit or create new
    if not myc.project().save_file_path:
        print("no args proj file data")

        if os.path.exists("./Save_Project.xml"):
            r = myc.handy_cmd_prompt("local save project file found use this one")
            if r:
                # load local old save proj file
                myc.project().save_file_path = ".\\"
                my_parser.quick_cache_load()
        if not myc.project().save_file_path:
            r = myc.handy_cmd_prompt("begin new ?")
            if not r:
                print("exiting")
                exit(0)
            else:
                myc.create_new_project()

def main():
    run = True
    while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()

    pygame.quit()
    print("saving")
    my_parser.quick_cache_save()
    exit(0)

def init():
    pygame.init()
    screen = pygame.display.set_mode((640, 455))