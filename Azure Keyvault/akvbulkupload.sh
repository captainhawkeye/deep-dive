#!/bin/bash

vault_name="$vault_name"
declare -A secrets
secrets=(
    ["Secret1"]="$Value1Variable"
)
for name in "${!secrets[@]}"; do
az keyvault secret set --vault-name "$vault_name" --name "$name" --value "${secrets[$name]}"
done