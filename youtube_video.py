#importing module to Connect with Youtube
from pytube import YouTube

def Download(link,File_path):
    url =YouTube(link)
    x=url.title
    print("VIDEO TITLE:")
    print('\n')
    print(x)
    print("\n")
    reso=input("Enter the resolution:")
    print("\n")
    video = url.streams.filter(res=reso).first().download(File_path)
    print("Video is downloaded.")

print("YOUTUBE VIDEO DOWNLOADER")
print('1.WANT TO DOWNLOAD VIDEO?')
print('2.Exit')
q=int(input("Enter the number (1/2):"))
while True:
    if q==1:
        #Taking Link of the video as input
        link=input("Enter the link of the video:")
        #Taking path to save video
        File_path=input("Enter the path where you want to download:")
        Download(link,File_path)
        m=input('Want to download another video(y/n):')
        if m in ['N','n']:
            break
        else:
            continue
    elif q==2:
        break
    else:
        print('PLEASE SELECT A CORRECT OPTION')