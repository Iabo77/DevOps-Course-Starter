terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 2.92"
    }
  }
   backend "azurerm" {
        resource_group_name  = "OpenCohort21_IanBoorer_ProjectExercise"
        storage_account_name = "tfstate10ibtf"
        container_name       = "tfstate"
        key                  = "terraform.tfstate"
    }
  
}

provider "azurerm" {
  features {}
}

data "azurerm_resource_group" "main" {
  name = "OpenCohort21_IanBoorer_ProjectExercise"
}

resource "azurerm_service_plan" "main" { 
  name                = "${var.prefix}-terraformed-asp"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  os_type             = "Linux" 
  sku_name            = "B1" 
} 
 
resource "azurerm_linux_web_app" "main" { 
  name                = "${var.prefix}-todoapp"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  service_plan_id     = azurerm_service_plan.main.id
  
  site_config {
    application_stack {
      docker_image     = "${var.DOCKER_IMAGE}"
      docker_image_tag = "latest"
    }
  }

  app_settings = {    
    DOCKER_REGISTRY_SERVER_URL = "https://index.docker.io"
    DOCKER_REGISTRY_SERVER_USERNAME = "${var.DOCKER_REGISTRY_SERVER_USERNAME}"
    DOCKER_REGISTRY_SERVER_PASSWORD = "${var.DOCKER_REGISTRY_SERVER_PASSWORD}"   

    CLIENT_ID= "${var.CLIENT_ID}" 
    CLIENT_SECRET="${var.CLIENT_SECRET}"
    GITHUB_OAUTH_URL="https://github.com/login/oauth/authorize"
    REDIRECT_URI="https://${var.prefix}-todoapp.azurewebsites.net/login/callback"  

    CONNECTION_STRING=azurerm_cosmosdb_account.main.connection_strings[0]
    DATABASE="todo_app"
    COLLECTION="items"

    SECRET_KEY="${var.SECRET_KEY}"
    FLASK_APP="${var.FLASK_APP}"
    FLASK_ENV="${var.FLASK_ENV}"
    }
}


resource "azurerm_cosmosdb_account" "main" {
  name                = "${var.prefix}-mongodb-account"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  offer_type          = "Standard"
  kind                = "MongoDB"
  enable_automatic_failover = false

  capabilities {
    name = "EnableServerless"
  }  

  capabilities {
    name = "EnableMongo"
  }

    lifecycle { 
    prevent_destroy = true 
  }

  consistency_policy {
    consistency_level       = "Session"
    max_interval_in_seconds = 5
    max_staleness_prefix    = 100
  }

  geo_location {
    location          = "UK West"
    failover_priority = 0
  }
}


resource "azurerm_cosmosdb_mongo_database" "main" {
  name                = "${var.prefix}-todoapp-db"
  resource_group_name = azurerm_cosmosdb_account.main.resource_group_name
  account_name        = azurerm_cosmosdb_account.main.name
}