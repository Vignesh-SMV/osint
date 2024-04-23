def info_gathering():
	import instaloader, sys

	from instaloader import Instaloader

	def banner():
		print(""" 
	 ''~``
                            ( o o )
    +------------------.oooO--(_)--Oooo.------------------+
    |                                                     |
    |          INFORMATION GATHERING TOOL INSTAGRAM        |
    |                      [21BIT049]                     |
    |                                                     |
    |                    .oooO                            |
    |                    (   )   Oooo.                    |
    +---------------------\ (----(   )--------------------+
                           \_)    ) /
                                 (_/
                                 
\033[41m =[===> 21BIT049 | https://github.com/Vignesh-SMV <===]=\033[0m """)

	banner()

	x = Instaloader()

	try:
		uname = input("\033[36mEnter a username \033[0m: \033[36m")
		if uname == "":
			print("\033[33mUnknown command!")
			sys.exit()

		f = instaloader.Profile.from_username(x.context, uname)

		print("\033[32mUsername\033[0m :", f.username)
		print("\033[32mID\033[0m :", f.userid)
		print("\033[32mFull name\033[0m :", f.full_name)
		print("\033[32mBiography\033[0m :", f.biography)
		print("\033[32mBusiness Category Name\033[0m :", f.business_category_name)
		print("\033[32mExternal url\033[0m :", f.external_url)
		print("\033[32mFollowed by viewerg\033[0m :", f.followed_by_viewer)
		print("\033[32mfollowing\033[0m :", f.followees)
		print("\033[32mfollowers\033[0m :", f.followers)
		print("\033[32mFollows viewer\033[0m :", f.follows_viewer)
		print("\033[32mBlocked by Viewer\033[0m :", f.blocked_by_viewer)
		print("\033[32mHas blocked viewer\033[0m :", f.has_blocked_viewer)
		print("\033[32mHas highlight reels\033[0m :", f.has_highlight_reels)
		print("\033[32mHas public story\033[0m :", f.has_public_story)
		print("\033[32mHas requested viewer\033[0m :", f.has_requested_viewer)
		print("\033[32mRequested by viewer\033[0m :", f.requested_by_viewer)
		print("\033[32mHas viewable story\033[0m :", f.has_viewable_story)
		print("\033[32mIGTV\033[0m :", f.igtvcount)
		print("\033[32mIs business account ?\033[0m :", f.is_business_account)
		print("\033[32mIs private ?\033[0m :", f.is_private)
		print("\033[32mIs verified\033[0m :", f.is_verified)
		print("\033[32mmedia count\033[0m :", f.mediacount)
		print("\033[32mprofile pic url\033[0m :", f.profile_pic_url)

	except KeyboardInterrupt:
		print("\033[33mI understand!")

	except EOFError:
		print("\033[33mWhy?")

