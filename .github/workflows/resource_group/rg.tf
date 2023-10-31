resource "azurerm_resource_group" "ht_rg" {
  name     = "ht-terraform"
  location = var.location
}

output "resource_group_name" {
  value = azurerm_resource_group.ht_rg.name
}