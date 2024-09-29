import speedtest

def test_internet_speed():
    st = speedtest.Speedtest()

    print("Finding best server...")
    st.get_best_server()

    print("Testing download speed...")
    download_speed = st.download()  # Speed in bits per second
    print("Testing upload speed...")
    upload_speed = st.upload()      # Speed in bits per second

    # Convert speeds to Mbps (megabits per second)
    download_speed_mbps = download_speed / 1_000_000
    upload_speed_mbps = upload_speed / 1_000_000

    print(f"Download speed: {download_speed_mbps:.2f} Mbps")
    print(f"Upload speed: {upload_speed_mbps:.2f} Mbps")

if __name__ == "__main__":
    test_internet_speed()
