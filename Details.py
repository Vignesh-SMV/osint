def fake_details():

     def banner():

          print(r'''
                                 ''~``
                                ( o o )
        +------------------.oooO--(_)--Oooo.------------------+
        |                                                     |
        |            TEMPORARY DETAIL GENERATION TOOL          |
        |                    [21BIT049]                       |
        |                                                     |
        |                    .oooO                            |
        |                    (   )   Oooo.                    |
        +---------------------\ (----(   )--------------------+
                               \_)    ) /
                                     (_/

        =[===> 21BIT049 | https://github.com/Vignesh-SMV <===]=
            ''')

     banner()

     from faker import Faker
     faker=Faker()

     name= faker.name()
     #boy=faker.first_name_male()
     #girl=faker.first_name_female()
     address=faker.address()
     company=faker.company()
     location=faker.latitude(),faker.longitude()
     job=faker.job()
     url=faker.url()
     dob=faker.date_of_birth()


     blood_group=['A+','A-','B+','B-','AB+','AB-','O+','O-']
     blood_group=faker.random_element(blood_group)
     try:

          print(f"---------------------------- | Details | ----------------------------\n")
          print('\033[32m name ',name)
          print('\033[32maddress\033[0m:',address)
          print('\033[32m Job \033[0m:',job)
          print('\033[32m company name \033[0m:',company)
          print('\033[32m location \033[0m :',location)
          print('\033[32m website location \033[0m :',url)
          print('\033[32m Date of Birth \033[0m :',dob)
          print('\033[32m Blood Group\033[0m :',blood_group)

     except KeyboardInterrupt:
          print("\033[33mI understand!")

     except EOFError:
          print("\033[33mWhy?")
