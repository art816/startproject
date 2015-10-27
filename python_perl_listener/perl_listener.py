from subprocess import Popen, PIPE

if __name__ == "__main__":
    args = "arg1 arg2"

    proc = Popen(
        "perl perl_speaker.pl %s" % (args),
        shell=True
    )
    proc.wait()    # дождаться выполнения
    res = proc.communicate()  # получить tuple('stdout res', 'stderr res')

    if proc.returncode:
        print ("Return code: ", res[1])
