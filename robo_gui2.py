
import speedtest

import subprocess
st = speedtest.Speedtest()


def net_speed():
    Download = st.download()
    Upload = st.upload()
    download = f'Download {Download / 1024 / 1024:.2f} Mbps'
    upload = f'Upload {Upload / 1024 / 1024:.2f} Mbps'
    return (download, upload)

def get_cpu_usage():
    # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
    cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell=True)
    return CPU

def get_gpu_usage():
    GPU = 0.0
    with open("/sys/devices/gpu.0/load", encoding="utf-8") as gpu_file:
        GPU = gpu_file.readline()
        GPU = int(GPU)/10
    return GPU

if __name__ == "__main__":
    print(get_cpu_usage())


