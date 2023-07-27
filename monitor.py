# Copyright (C) 2023 Ibrahem Mouhamad
#
# SPDX-License-Identifier: MIT

"""
This module provides functions to retrieve system resource usage information
using the `psutil` library.
"""

import os
import psutil
import time

def getCPUUsage():
    """
    returns a dictionary with CPU usage information, including
    the overall usage percentage and the number of CPUs.
    """

    cpu_usage = {}
    # https://psutil.readthedocs.io/en/latest/index.html?highlight=cpu_percent#psutil.Process.cpu_percent
    psutil.cpu_percent()
    time.sleep(1)
    cpu_usage['usage'] = psutil.cpu_percent()
    cpu_usage['count'] = psutil.cpu_count()
    return cpu_usage

def getMemUsage():
    """
    returns a dictionary with memory usage information, including
    the total, used, and available memory in bytes, the overall memory usage percentage,
    and the percentage of swap memory used.
    """

    memory_usage = {}
    memory_usage['total']      = int(psutil.virtual_memory().total/(1024*1024)) # in MB
    memory_usage['used']       = int(psutil.virtual_memory().used/(1024*1024)) # in MB
    memory_usage['available']  = int(psutil.virtual_memory().available/(1024*1024)) # in MB
    memory_usage['usage']      = psutil.virtual_memory().percent
    memory_usage['swap_usage'] = psutil.swap_memory().percent
    return memory_usage

def getNetworkUsage():
    """
    returns a dictionary with network usage information, including
    the number of bytes and packets sent and received, as well as the number of packets
    dropped.
    """

    network_usage = {}
    network_usage['bytes_sent']      = int(psutil.net_io_counters().bytes_sent/(1024*1024)) # in MB
    network_usage['bytes_recv']      = int(psutil.net_io_counters().bytes_recv/(1024*1024)) # in MB
    network_usage['packets_sent']    = psutil.net_io_counters().packets_sent
    network_usage['packets_recv']    = psutil.net_io_counters().packets_recv
    network_usage['packets_dropin']  = psutil.net_io_counters().dropin
    network_usage['packets_dropout'] = psutil.net_io_counters().dropout
    return network_usage

def getDiskUsage():
    """
    returns a list of dictionaries with disk usage information
    for each mounted partition, including the name, total, used, and free space in bytes,
    and the overall usage percentage.
    """

    disk_usage = []
    for dp in psutil.disk_partitions():
        partition_usage = {}
        partition_usage['name'] = dp.mountpoint
        partition_usage['total'] = int(psutil.disk_usage(dp.mountpoint).total/(1024*1024))  # in MB
        partition_usage['used'] = int(psutil.disk_usage(dp.mountpoint).used/(1024*1024))  # in MB
        partition_usage['free'] = int(psutil.disk_usage(dp.mountpoint).free/(1024*1024))  # in MB
        partition_usage['usage'] = psutil.disk_usage(dp.mountpoint).percent
        disk_usage.append(partition_usage)
    return disk_usage

def getResourcesUsage():
    """
    returns a dictionary with system resource usage information,
    including the device name, CPU usage information, memory usage information,
    network usage information, and disk usage information.
    """

    resources_usage = {}
    resources_usage['device_name'] = os.uname().nodename
    resources_usage['cpu'] = getCPUUsage()
    resources_usage['memory'] = getMemUsage()
    resources_usage['network'] = getNetworkUsage()
    resources_usage['disk'] = getDiskUsage()
    return resources_usage
