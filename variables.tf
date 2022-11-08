variable "prefix" {
    description = "The prefix used for all resources in this environment"
    default = "ibtf"
    }

variable "RESOURCE_GROUP_NAME" {
    type = string
    default = "OpenCohort21_IanBoorer_ProjectExercise"
}

variable "STORAGE_ACCOUNT_NAME" {
    type = string
    default = "tfstate10ibtf"
}

variable "CLIENT_ID" {
    type = string
    sensitive = true
}

variable "CLIENT_SECRET" {
    type = string
    sensitive = true

}

variable "GITHUB_OAUTH_URL" {
    type = string
    sensitive = true

}


variable "COLLECTION" {
    type = string
    sensitive = true
}

variable "DATABASE" {
    type = string
    sensitive = true

}

variable "SECRET_KEY" {
    type = string
    sensitive = true

}

variable "FLASK_APP" {
    type = string
    sensitive = true

}

variable "FLASK_ENV" {
    type = string
    sensitive = true

}

variable "DOCKER_IMAGE" {
    type = string
    sensitive = true

}

variable "DOCKER_REGISTRY_SERVER_URL" {
    type = string
    sensitive = true

}

variable "DOCKER_REGISTRY_SERVER_USERNAME" {
    type = string
    sensitive = true
}


variable "DOCKER_REGISTRY_SERVER_PASSWORD" {
    type = string
    sensitive = true
}


variable "location" {
  description = "The Azure location where all resources in this deployment should be created"
  default     = "uksouth"
}