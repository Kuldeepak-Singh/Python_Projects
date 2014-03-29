Why This Script is Useful :

Sometimes After modifying several project files , We Want to create a "diff" Directory.This Script does just that.

What is "Diff" :

Let me take an example to better explain this.
I am working on a project and i have modified a few files.
Path to Modified file is : X:\Project\A\B\C\D\E...\Z\abc.c
After Modification I want to create a directory (the "Diff" Directory) which contains both "Modified abc.c" and "abc.c before modification".

Now If i just want to have old and new "abc.c" in a directory this script is not needed. 
But if i want to have new and old "abc.c" in the same way as it is in the project i.e. D:\Project\A\B...\z\abc.c
then this script is useful. Instead of manually creating complete directory strucutre in the "Diff" directory and then pasting both old and new files you can use this script to create the folder structure for you then all you have to do is to just copy the old and new files since complete hierarchy of directories is already created.
This Script will also explore both new and old directories for you to save your precious time to manually open these directories.


What this Script Does :

This script just finds the location of your file in the source directory (provided by you) and then create "diff" directory in the destination directory.


Inside "Diff" directory Two directories will be created "new" and "old". Both of them will have same hierarchy of Direcotries.

(In Windows)

let's say Source is X:\Project
file name : abc.c
Destination is : D:\Test (In Windows) 

Then After Execution of the script :

D:\Test\diff\new\A\B\C\...\Z

D:\Test\diff\old\A\B\C\...\Z

will be created.

Script can also be used in unix systems.

Same "diff" can be used for multiple files modified in the same project by entering same destination and source path with the respective file names for all modified files. 

Uses:

1) To compare changes between old and new files.

2) To keep track of the files modified for a specific task/feature and their Respective locations. So in future , if the developer is asked to revert back all his/her changes done for a particular feature, he/she can easily find out how many files were modified and their location so as to avoid any mistakes. 

