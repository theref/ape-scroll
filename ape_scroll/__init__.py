from ape import plugins
from ape.api import NetworkAPI, create_network_type
from ape.api.networks import LOCAL_NETWORK_NAME
from ape_node import Node
from ape_test import LocalProvider

from .ecosystem import NETWORKS, Scroll, ScrollConfig


@plugins.register(plugins.Config)
def config_class():
    return ScrollConfig


@plugins.register(plugins.EcosystemPlugin)
def ecosystems():
    yield Scroll


@plugins.register(plugins.NetworkPlugin)
def networks():
    for network_name, network_params in NETWORKS.items():
        yield "scroll", network_name, create_network_type(*network_params)
        yield "scroll", f"{network_name}-fork", NetworkAPI

    # NOTE: This works for development providers, as they get chain_id from themselves
    yield "scroll", LOCAL_NETWORK_NAME, NetworkAPI


@plugins.register(plugins.ProviderPlugin)
def providers():
    for network_name in NETWORKS:
        yield "scroll", network_name, Node

    yield "scroll", LOCAL_NETWORK_NAME, LocalProvider
