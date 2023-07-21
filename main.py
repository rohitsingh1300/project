#  returns link to the profile picture
import instaloader

# Get instance
loader = instaloader.Instaloader()

# Login using the credentials
# loader.login(USER, PASSWORD)

# Use Profile class to access metadata of account
profile = instaloader.Profile.from_username(loader.context,
											'rohit_singh1313')

profile_pic = profile.profile_pic_url


print(profile_pic)
