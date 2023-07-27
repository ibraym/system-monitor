# System Resource Monitor

This is a simple Python script that provides a lightweight HTTP server for monitoring system resource usage. The server responds to GET requests with a JSON object containing information about CPU, memory, network, and disk usage.

## Requirements

- Python 3.x
- `psutil` library (can be installed via `pip`)

## Usage

1. Navigate into the source folder and run the following commands to initialize the virtual environment and install the required packages

    ```shell
    python3 -m venv .env
    . .env/bin/activate
    pip install -r requirements.txt
    ```

2. To start the server, run the following command from the command line:

    ```shell
    python3 server.py [address] [port]
    ```

    where `address` is the IP address or hostname to listen on (e.g., 'localhost'), and `port` is the port number to listen on (e.g., 8000).

    Example:

    ```shell
    python3 server.py localhost 8000
    ```

    Once the server is running, you can access it by opening a web browser and navigating to `http://[address]:[port]`, where `address` and `port` are the values you specified when starting the server.

3. To start the server at boot, execute the following steps:

    - Open the crontab file

        ```shell
        crontab -e
        ```

    - Add the following line at the end of the file:

        ```shell
        @reboot /path/to/python /path/to/server.py [address] [port]
        ```

        Replace `/path/to/python` with the path to the Python executable in the `.env` virtual environment directory, `/path/to/server.py` with the full path to the `server.py` script, `[address]` with the IP address or hostname to listen on (e.g., 'localhost'), and `[port]` with the port number to listen on (e.g., 8000).

    - Save the changes and exit the editor

## Output

This JSON object contains information about the device name, CPU usage, memory usage, network usage, and disk usage. The cpu dictionary contains the overall CPU usage percentage and the number of available CPUs. The memory dictionary contains information about the total, used, and available memory in bytes, as well as the overall memory usage percentage and the percentage of swap memory used. The network dictionary contains information about the number of bytes and packets sent and received, as well as the number of packets dropped. The disk list contains information about the usage of each mounted partition, including the name, total, used, and free space in bytes, and the overall usage percentage.

```json
{
    "device_name": "my-computer",
    "cpu": {
        "usage": 3.1, 
        "count": 4
    },
    "memory": {
        "total": 8589934592,
        "used": 4089446400,
        "available": 4490487296,
        "usage": 47.6,
        "swap_usage": 0.0
    },
    "network": {
        "bytes_sent": 123456789,
        "bytes_recv": 987654321,
        "packets_sent": 1234,
        "packets_recv": 5678,
        "packets_dropin": 0,
        "packets_dropout": 0
    },
    "disk": [
        {
            "name": "/",
            "total": 250790436096,
            "used": 150790436096,
            "free": 100000000000,
            "usage": 60.2
        },
        {
            "name": "/mnt/data",
            "total": 1000202273280,
            "used": 200202273280,
            "free": 800000000000,
            "usage": 20.0
        }
    ]
}
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project uses the `psutil` library, which is distributed under the BSD 3-Clause License. For more information, see the [psutil documentation ↗](https://psutil.readthedocs.io/en/latest/).
