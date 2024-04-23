import argparse
import pyfiglet
from Details import fake_details
from tempmail import mail
from face_generator import face
from insta_info import info_gathering
from response import main

parser = argparse.ArgumentParser(description="print")
parser.add_argument("operation",help='mail id , detail , image')
#parser.add_arguments("operation",help='value')
args = parser.parse_args()

if args.operation=="start":
   banner= pyfiglet.figlet_format('Welcome To OSINT Sock Puppet Tool')
   print(banner)

   while True:


      print('\n\033[32m ENTER A OPTION \n 1-TEMPORARY DETAILS \n 2-TEMPORARY MAIL \n 3-TEMPORARY FACE \n 4-INSTA INFO GATHERING \n 5-Web site code\033[0m')

      arg=input("\n >>")
      if arg=="1":
         fake_details()

      if arg=="2":
         mail()

      if arg=="3":
         face()

      if arg=="4":
         info_gathering()

      if arg=="5":
         main()
