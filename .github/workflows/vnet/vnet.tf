# Vnet resource creation
resource "azurerm_virtual_network" "HT_Vnet" {
  name                = "ht-terraform-vnet"
  location            = var.location
  resource_group_name = var.resource_group_name
  address_space       = [var.Vnet_cidr]

  subnet {
    name           = "subnet1"
    address_prefix = var.Sub1_CIDR
  }

  subnet {
    name           = "subnet2"
    address_prefix =  var.Sub2_CIDR
  }

  subnet {
    name           = "subnet3"
    address_prefix = var.Sub3_CIDR
  }
}