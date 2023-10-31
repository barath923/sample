# Security Group Creation
resource "azurerm_network_security_group" "HT_SG" {
  name                = "Terraform-security-group"
  location            = var.location
  resource_group_name = var.resource_group_name
}