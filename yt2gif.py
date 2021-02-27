import os
import re
import argparse
import subprocess


def validateArgs(args):
    if not args.target:
        print("[!] Target not set! Please select a target with '-t <target>'")
        return False
    elif not re.match("^[0-9]+$",args.fps):
        print(f"[!] Invalid value '{args.fps}' for fps")
    elif not re.match("^[0-9]+,[\-]*[0-9]+$",args.dim):
        print(f"[!] Invalid value '{args.dim} for dim")
    else:
        return True

def downloadVideo(target):
    # make temp directory
    tmp_success, tmp_dir = subprocess.getstatusoutput("mktemp -d")
    # download file to dir
    dl_success = os.system(f"youtube-dl {target} -o '{tmp_dir}/%(id)s.%(ext)s'")
    if dl_success == 0:
        tmp_file = tmp_dir+"/"+os.listdir(tmp_dir)[0]
    else:
        tmp_file = None
    return (tmp_success, dl_success, tmp_file)
    
def convertVideo(tmp_file, output, dim, fps):
    # definitely needs more command line arguments
    print(dim,fps)
    return os.system(f"ffmpeg \-i {tmp_file} -vf 'fps={fps},scale={dim[0]}:{dim[1]}' {output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
    Command line utility to download YouTube videos and convert
    them to a gif animation
    """)    
    parser.add_argument("-t", "--target", dest="target", default=None, help="URL of video to download")
    parser.add_argument("-o", "--output", dest="output", default="output.gif", help="Output filename")
    parser.add_argument("-d", "--dimension", dest="dim", default='320,-1', help="Dimension of output")
    parser.add_argument("-f", "--fps", dest="fps", default=10, help="Fps of output")

    args =  parser.parse_args()
    if not validateArgs(args):
        print("[!] Failed due to improper arguments.")
    
    print(f"[+] Downloading video from {args.target}")
    tmp_success, dl_success, tmp_file = downloadVideo(args.target)
    
    if tmp_success != 0 :
        print("[!] Error, Failed to Create Temp File")
    elif dl_success != 0:
        print("[!] Error, Failed to Download Video")
    
    if dl_success != 0 or tmp_success != 0:
        print("[!] Youtube2Gif Failed")
        exit(1)

    print(f"[+] File successfully downloaded, stored at {tmp_file}. Beginning Conversion... ")
    conv_success = convertVideo(tmp_file,args.output,args.dim.split(','),args.fps)
    if conv_success != 0:
        print(f"[!] Error, Failed to convert file")

    print(f'[+] Cleaning up temporary files.')
    os.remove(tmp_file)
    
    if conv_success == 0:
        print(f"[+] File Conversion Complete. Output located at {args.output}")
        exit(0)
    else:
        print("[!] Youtube2Gif Failed")
        exit(1)
