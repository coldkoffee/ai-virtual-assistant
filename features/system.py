import os,signal
import subprocess
import cv2
import pyautogui
import time
import shutil
import schedule


def launch_app(app_name):
    try:
        os.system(app_name)
        return True
    except OSError as error:
        return error

def take_picture():
    cap=cv2.VideoCapture(0)
    while True:
        ret,img=cap.read()
        cv2.imshow('img',img)
        if cv2.waitKey(1) & 0xFF==ord('s'):
            cv2.imwrite('picture.png',img)
            break
        elif cv2.waitKey(1) & 0xFF==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    
def close_application(app_name):
    try:
        pid=os.popen(f"pidof {app_name}").read().strip()
        os.system(f"kill -9 {pid}")
        return True
    except OSError as error:
        return error
#close_application('texteditor')
def shutdown():
    try:
        os.system("shutdown now")
        return True
    except OSError as error:
        return error

def restart():
    try:
        os.system("reboot")
        return True
    except OSError as error:
        return error

def manual(command):
    output=os.popen(f"man {command}").read()
    return output
    
def createuser(username):
    output=os.popen(f"sudo useradd -m {username}").read()
    return output

def delete_user(username):
    output=os.popen(f'sudo userdel -rfRZ {username}').read()
    return output

def change_password(username,password):
    output=os.popen(f"echo '{username}:{password}'| sudo chpasswd").read()
    return output

def create_directories(dir_name):
    try:
        cwd=os.getcwd()
        user_dir=f"{cwd}/{dir_name}"
        os.makedirs(user_dir,exist_ok=True)
        return True
    except OSError as error:
        return error

def delete_directories(dir_name):
    try:
        cwd=os.getcwd()
        user_dir=f"{cwd}/{dir_name}"
        shutil.rmtree(user_dir)
        return True
    except:
        return f"directorie can't be deleted as it is not present"

def create_files(filename):
    try:
        cwd=os.getcwd()
        file_path=f"{cwd}/{filename}.txt"
        subprocess.run(["touch",file_path])
        return True
    except OSError as error:
        return error
        
def delete_files(filename):
    try:
        cwd=os.getcwd()
        file_path=f"{cwd}/{filename}.txt"
        os.system(f'rm {file_path}')
        return True
    except OSError as error:
        return error

def change_directories(dir_name):
    while True:
        cwd=os.getcwd()
        files_contents=os.popen("ls").read()
        if dir_name in files_contents:
            os.chdir(dir_name)
            print(os.getcwd())
            break
        else:
            os.chdir("..")
            cwd=os.getcwd()
            files_contents=os.popen("ls").read()
            if dir_name in files_contents:
                os.chdir(dir_name)
                print(os.getcwd())
                break              

def switch_window():
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.keyUp("alt")

def ip_address():
    try:
        routing_table=os.popen('ip route')
        for line in routing_table:
            if "default via" in line:
                default_route=line.strip().split()
        default_gateway=default_route[2]
        interface_config=os.popen('ip addr')
        for line in interface_config:
            if default_gateway in line:
                ip_add=line.strip().split()[1].split('/')[0]
        return ip_add
    except:
        return f"device is not connected to network"

def job_schedule():
    def job():
        print("Hello World")
    schedule.every().day.at("20:48").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

def take_note(query):
    message=query.replace("remember that","")
    message=message.replace("alan","")
    cwd=os.getcwd()
    remember=f"{cwd}/note.txt"
    subprocess.run(["touch",remember])
    remember_file=open("note.txt","w")
    remember_file.write(message)
    remember_file.close()

def read_note():
    remember_file=open("note.txt","r")
    message=remember_file.read()
    remember_file.close()
    os.remove("note.txt")
    return f"You tell me that {message}"

def change_permission(filename,mode):
    try:
        subprocess.run(['chmod',mode,filename],check=True)
    except CalledProcessError as error:
        return error

if __name__=="_main_":
    shutdown()
    restart()
    close_application(data)
    launch_app(data)
    manual("mkdir")
    change_directories()
    create_files()
    createuser()
    take_picture()
    switch_window()
    change_permission('test.txt','777')
