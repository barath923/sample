# Req is to create storage account in Azure using terraform

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

# Terraform Modules starts
module "resource_group" {
  source = "./resource_group"
  location = var.location
}

module "vnet" {
  source = "./vnet"
  location = var.location
  resource_group_name = module.resource_group.resource_group_name
  Vnet_cidr = var.Vnet_cidr
  Sub1_CIDR = var.Sub1_CIDR
  Sub2_CIDR = var.Sub2_CIDR
  Sub3_CIDR = var.Sub3_CIDR
}

module "sec_group" {
  source = "./sec_group"
  location = var.location
  resource_group_name = module.resource_group.resource_group_name
}

module "storage_acc" {
  source = "./storage_acc"
  location = var.location
  resource_group_name = module.resource_group.resource_group_name
}


