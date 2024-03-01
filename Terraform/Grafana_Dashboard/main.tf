# versions.tf

terraform {
   required_providers {
      grafana = {
         source  = "grafana/grafana"
         version = ">= 2.9.0"
      }
   }
}

# main.tf 

provider "grafana" {
  url   = "http://localhost:3000/"
  auth = "glsa_91barVyBsZjreFuNpgg7zrXhEoRwPCzh_f0a089cf"
}

resource "grafana_folder" "create_folder_on_grafana" {
  title = "anurag Folder"
}

resource "grafana_dashboard" "deploy_dashboard" {
  folder = grafana_folder.create_folder_on_grafana.id
  config_json = jsonencode({
    "title" : "My Dashboard"
  })
}
