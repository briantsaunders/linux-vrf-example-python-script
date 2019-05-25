#!/usr/bin/python3

import argparse
import logging
import subprocess
import sys
from pyroute2 import IPDB

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logger.addHandler(console)


def create_vrf(vrf_name, vrf_table):
    """Creates a vrf.

    Parameters
    ----------
    vrf_name : str
        The name of the vrf.
    vrf_table : int
        The table associated with the vrf.
    
    Returns
    -------
    None

    """
    with IPDB() as ipdb:
        with ipdb.create(
            kind="vrf",
            ifname=args.vrf_name,
            vrf_table=args.vrf_table
        ) as vrf:
            vrf.up()
    logger.info(f"{args.vrf_name} created")


def manage_vrf_interfaces(args):
    """Add or removes interface from vrf

    Paramters
    ---------
    vrf_name : str
        The vrf name.
    interface : str
        The interface name.
    
    Returns
    -------
    None

    """
    with IPDB() as ipdb:
        with ipdb.interfaces[args.vrf_name] as vrf:
            if args.action == "add_interface":
                vrf.add_port(ipdb.interfaces[args.interface].index)
                logger.info(f"{args.interface} added to vrf {args.vrf_name}")
            if args.action == "remove_interface":
                subprocess.run(f"ip link set dev {args.interface} nomaster", shell=True)
                logger.info(f"{args.interface} removed from vrf {args.vrf_name}")


def delete_vrf(args):
    """Deletes a vrf.

    Parameters
    ----------
    vrf_name : str
        The vrf name.

    Returns
    -------
    None

    """
    with IPDB() as ipdb:
        with ipdb.interfaces[args.vrf_name] as vrf:
            vrf.remove()
    logger.info(f"vrf {args.vrf_name} removed")


def main(args):
    """
    """
    if args.action == "create":
        # validate vrf does not already exist
        vrf_exists = True
        try:
            with IPDB() as ipdb:
                ipdb.interfaces[args.vrf_name].index
        except KeyError:
            vrf_exists = False
        if vrf_exists:
            logger.error(f"{args.vrf_name} already exists")
            sys.exit()
        # validate vrf table passed
        if args.vrf_table == None:
            logger.error("missing vrf_table")
            sys.exit()
        create_vrf(args.vrf_name, args.vrf_table)
    if args.action == "delete":
        delete_vrf(args)
    if "interface" in args.action:
        # check if interface exists
        with IPDB() as ipdb:
            try:
                ipdb.interfaces[args.interface]
            except KeyError:
                logger.error(f"{args.interface} is invalid")
                sys.exit()
        manage_vrf_interfaces(args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Example script to manage vrfs")
    parser.add_argument(
        "--action", 
        required=True, 
        action="store",
        choices=["create", "delete", "add_interface", "remove_interface"],
        help="Vrf action"
    )
    parser.add_argument(
        "--vrf_name", 
        required=True, 
        action="store", 
        help="Vrf name"
    )
    parser.add_argument(
        "--vrf_table", 
        required=False, 
        action="store", 
        type=int,
        help="Vrf table"
    )
    parser.add_argument(
        "--interface", 
        required=False, 
        action="store", 
        help="Interface name"
    )
    args = parser.parse_args()
    sys.exit(main(args))
