import subprocess
sub=subprocess.Popen("./repf_pano_client.sh /home/lmf/tmp/repf_pano_client/1666520115/input.png.deep/input", shell=True, stdout=subprocess.PIPE)
sub.wait()
print(sub.stdout.read())
