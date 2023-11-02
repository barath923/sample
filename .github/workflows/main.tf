# Azure Provider
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.0.0"
    }
  }
}

# Configure the Microsoft Azure Provider
provider "azurerm" {
  features {
    #skip_provider_registration = true # This is only required when the User, Service Principal, or Identity running Terraform lacks the permissions to register Azure Resource Providers.
  }
}

# Vnet resource creation
resource "azurerm_virtual_network" "HT_Vnet" {
  name                = "ht-terraform-vnet"
  location            = "Central India"
  resource_group_name = "rg1"
  address_space       = ["10.10.0.0/16"]

  subnet {
    name           = "subnet1"
    address_prefix = "10.10.1.0/24"
  }

  subnet {
    name           = "subnet2"
    address_prefix = "10.10.2.0/24"
  }

  subnet {
    name           = "subnet3"
    address_prefix = "10.10.3.0/24"
  }
}


resource "azurerm_network_security_group" "HT_SG" {
  name                = "Terraform-security-group"
  location            = "Central India"
  resource_group_name = "rg1"
}
