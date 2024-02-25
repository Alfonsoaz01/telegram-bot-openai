param location string = 'westeurope'

param containerGroups_test_bot_name string = 'test-bot'

resource containerRegistry 'Microsoft.ContainerRegistry/registries@2023-11-01-preview' = {
  name: 'myContainerRegistry'
  location: location
  sku: {
    name: 'Basic'
  }

  properties: {
    adminUserEnabled: true
  }

}

resource containerGroups_test_bot_name_resource 'Microsoft.ContainerInstance/containerGroups@2023-05-01' = {
  name: containerGroups_test_bot_name

  location: location
  properties: {
    sku: 'Standard'
    containers: [
      {
        name: containerGroups_test_bot_name
        properties: {
          image: '${containerRegistry.name}.azurecr.io/telegram-bot-openai-backend:latest'
          ports: []
          environmentVariables: []
          resources: {
            requests: {
              memoryInGB: 1
              cpu: 1
            }
          }
        }
      }
    ]
    initContainers: []
    imageRegistryCredentials: [
      {
        server: '${containerRegistry.name}.azurecr.io'
        username: containerRegistry.name
      }
    ]
    restartPolicy: 'Always'
    osType: 'Linux'
    priority: 'Spot'
  }
}
