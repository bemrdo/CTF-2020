from subprocess import PIPE, Popen
import subprocess
import sys

def cmdline(command):?!?jedi=0, ?!?      (*_*args: _CMD*_*, bufsize: int=..., executable: Optional[_PATH]=..., stdin: Optional[_FILE]=..., stdout: Optional[_FILE]=..., stderr: Optional[_FILE]=..., preexec_fn: Optional[Callable[[], Any]]=..., close_fds: bool=..., shell: bool=..., cwd: Optional[_PATH]=..., env: Optional[_ENV]=..., universal_newlines: bool=..., startupinfo: Optional[Any]=..., creationflags: int=..., restore_signals: bool=..., start_new_session: bool=..., pass_fds: Any=..., encoding: Optional[str]=..., errors: Optional[str]=...) ?!?jedi?!?
    proc = subprocess.Popen(str(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=T$
    (out, err) = proc.communicate()
    return err

def main():
    words = [line.strip() for line in open('pass.lst')]
    print("\n")
    count=0

    for w in words:
        strcmd = "openssl rsa -in id_rsa.pem -out out.key -passin pass:"+w
        res=cmdline(strcmd)
        if res.startswith("writing"):
                print("\nThe key is: "+w)
                sys.exit()
        print(str(count)+"/"+str(w))
        count=count+1
    print("\n")

if __name__ == '__main__':
    main()
