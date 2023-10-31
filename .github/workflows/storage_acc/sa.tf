# Storage Account creation
resource "azurerm_storage_account" "ht_stgacc" {
  name                     = "mystorageaccountht"
  resource_group_name      = var.resource_group_name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}