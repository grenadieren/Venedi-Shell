import cmd
import datetime
import os

class CLI(cmd.Cmd):
    prompt = 'rcons@app >>>'
    intro = 'Type help for a list of commands'
    def do_help(self, line):
        print("Commands:")
        print("help > list of commands")
        print("quit > quit the console")
        print("time > get some information about the time")
        print("run > execute python code")
        print("echo > echo back your provided line")
        print("mkdir > make a directory in the chosen path")
        print("cpath > change your working directory")
        print("getcwd > get your working directory")

    def do_quit(self, line):
        return True
    
    def do_time(self, line):
        print(datetime.datetime.now())
    
    def do_dir(self, line):
        print(os.listdir())
        print("CDir:", os.getcwd())

    def do_run(self, line):
        try:
            exec(line)
        except Exception as e:
            print(f"Error: {e}")
            
    def do_echo(self, line):
         echoback = input("Enter line to echo:")
         print(echoback)
         
    def do_mkdir(self, line):
        mkdirr = input("Path?")
        os.mkdir(mkdirr)
        
    def do_cpath(self, line):
        path = input("Path?")
        os.chdir(path)    
        
    def do_getcwd(self, line):
        print(os.getcwd())
if __name__ == '__main__':
    CLI().cmdloop()
