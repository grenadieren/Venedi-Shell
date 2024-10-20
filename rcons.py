import cmd
import datetime
import os
import shutil

class Console(cmd.Cmd):
    prompt = 'rcons@app >>> '
    intro = 'Version 0.3 Type "Help" for help'
    def do_help(self, line):
        print("-----")
        print("This console is designed to mimic the Windows Terminal more than Bash, however, it has some original functionality.")
        print("There are some bugs that have been found, they will be fixed soon")
        print("-----")
        print("Commands:")
        print("help > list of commands")
        print("quit > quit the console")
        print("time > get some information about the time")
        print("run > execute python code")
        print("echo > echo back your provided line")
        print("mkdir > make a directory in the chosen path")
        print("cdir > change your working directory")
        print("getcwd > get your working directory")
        print("osinfo > get information about your computer/os")
        print("rename > rename a directory/file")
        print("exec > execute a file")
        print("copy > copy the chosen file")
        print("rmdir > delete a directory")
        print("rmtr > instead of deleting a directory, delete an entire directory tree")
        print("mov > move a file to the chosen path")
        print("diskus > get the disk usage of a directory")
        print("archf > get the available archive formats for your system")
        print("archf_unpack > get the available archive formats for unpacking on your system")
        print("termsiz > get the terminal size")
        print("flagger > easily set flags to any path")
        print("scand > Return an iterator of os.DirEntry objects")
        print("-----")
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
            print("line executed")
        except Exception as e:
            print(f"Error: {e}")
            
    def do_echo(self, line):
         var1 = input("Enter line to echo:")
         print(var1)
         
    def do_mkdir(self, line):
        mkdir1 = input("Path?")
        os.mkdir(mkdir1)
        
    def do_cdir(self, line):
        path = input("Path?")
        os.chdir(path)    
        
    def do_getcwd(self, line):
        print(os.getcwd())
        print(os.getcwdb())
        print("(last is a bytestring)")
        
    def do_osinfo(self, line):
        print(os.listdrives())
        print(os.listvolumes())
    
    def do_rmdir(self, line):
        dir1 = input("Path?")
        os.rmdir(dir1)
    
    def do_rename(self, line):
        var1 = input("Src?")
        var2 = input ("Dst?")
        os.rename(var1, var2)
    
    def do_exec(self, line):
        var1 = input("Path?")
        os.system(var1)
    
    def do_copy(self, line):
        src1 = input("Src?")
        dst1 = input("Dst?")
        shutil.copyfile(src1, dst1)
    
    def do_rmtr(self, line):
        rm1 = input("Path?")
        shutil.rmtree(rm1)
    
    def do_mov(self, line):
        var1 = input("Src?")
        var2 = input("Dst?")
        shutil.move(var1, var2)
    
    def do_diskus(self, line):
        path1 = input("Path?")
        print(shutil.disk_usage(path1))
    
    def do_archf(self, line):
        print(shutil.get_archive_formats())
    
    def do_archf_unpack(self, line):
        print(shutil.get_unpack_formats())
    
    def do_termsiz(self, line):
        print(os.get_terminal_size())
    
    def do_flagger(self, line):
        var1 = input("Path?")
        var2 = input("Flags?")
        os.chflags(var1, var2)
    
    def do_scand(self, line):
        var1 = input("Path?")
        print(os.scandir(var1))
    
if __name__ == '__main__':
    Console().cmdloop()
