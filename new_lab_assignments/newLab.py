import os
import glob
import shutil

downloads_folder = os.path.expanduser('~/Downloads')

desktop_path = os.path.expanduser('~/Desktop')

work_folder = "\\UNI\\2019\\Aup\\lab_darbi"

file_name = "AuPLa"

python_standart_code = """print("") #Vards

while True:

	atkartot = int(input("\\nVelies atkartot? Ja(1) , Ne(0)"))
	print("="*50 + "\\n")
	if atkartot == 0:
		break
"""

cpp_standart_code="""#include <bits/stdc++.h>

using namespace std;

int main(){
    int atkartot;
    cout<<""; //Vards
    do{

    	cout<<"Vai atkartot? Ja(1), Ne(0)\\n";
    	cin>>atkartot;
    	cout<<setw(50)<<setfill('*')<<"\\n";
    }while(atkartot == 1);
}

"""

print("Create the folder and file structure for a lab assignement!")

n = int(input("Number of the assignement : "))

correct = int(input("Is this the %i assignement?\nYES(1) NO(0): " % n))

if correct ==1:
	dir_path = os.getcwd()
	path = dir_path + work_folder
	os.chdir(path)
	path = path + "\\" + str(n)
	print("Current directory  is %s" % path)

	try:
		os.mkdir(path)

	except OSError:
		print("Failed to create folder %i!!" % n)

	else:
		print("Created folder %i successfully!" % n)
		os.chdir(path)

		if n < 10:
			file_name = file_name + "0" + str(n) + "0"

		else:
			file_name = file_name  + str(n) + "0"

		for i in range(1,5):
			full_file_name = file_name + str(i)

			if i%2 == 0:
				f = open(full_file_name + ".cpp", "a+")
				f.write(cpp_standart_code)
				print("Created file %s.cpp" % full_file_name)

			else:
				f = open(full_file_name + ".py", "a+")
				f.write(python_standart_code)
				print("Created file %s.py" % full_file_name)

			f.close();

		files_path = os.path.join(downloads_folder, "*")
		files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)

		d = int(input("Would you like to move: %s into the folder?\nYES(1), No(0)" % files[0]))

		if d == 1:
			print("Moving file\nfrom:\t" , files[0] , "\nto:\t" , path)
			shutil.move(files[0], path)

		else:
			print("Not moving anyting...")

		print("All done!")

else:
	print("Wrong assignement!!")

input("Press Enter to continue...")
