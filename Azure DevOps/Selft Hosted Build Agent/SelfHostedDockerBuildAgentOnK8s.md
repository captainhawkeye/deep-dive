1. Creating a Build Agent Docker Image
	
	Download the Dockerfile and start.sh file from MS Docs (See below)
	Make sure to convert start.sh file into 'dos2unix'
	Keep the Dockerfile and start.sh file in same location where you'll execute the below commands
		docker build -t <dockerorganization/repo:tag> .
		docker push <dockerorganization/repo:tag>
	You can run the docker image to check if the agent is coming online or not
		docker run -e AZP_URL=<AzureDevOpsOrgURL> -e AZP_TOKEN=<AzureDevOpsPATToken> -e AZP_AGENT_NAME=<AnyAgentName> <FullDockerImage>
	Above command will add the Linux Based Agent in Default Agent Pool. If you want to create the agent in a custom defined Agent Pool, then create a new Agent Pool on Azure DevOps Portal and execute the below command
		docker run -e AZP_URL=<AzureDevOpsOrgURL> -e AZP_TOKEN=<AzureDevOpsPATToken> -e AZP_AGENT_NAME=<AnyAgentName> -e AZP_POOL=<AgentPoolName> <FullDockerImage>
		
2. Running the Build Agent Docker Image in AKS

	To run the above create docker image in an AKS cluster, do not run the docker image from the above steps, just build and push the docker image.
	Create a Namespace in AKS where build agent will run
		kubectl create ns <NamespaceName>
	Create a Kubesecret in the above namespace which will hold all the variables
		kubectl create secret generic <SecretName> --from-literal=AZP_URL=<AzureDevOpsOrgURL> --from-literal=AZP_TOKEN=<AzureDevOpsPATToken> --from-literal=AZP_POOL=<AgentPoolName> -n <NamespaceName>
	Download the Deployment YAML file from MS Docs and modify it according to the requirement and apply it
	The number of replicas you'll set in above YAML file, that number of agents will be added into Agent Pool.
	
	
MS Doc: https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/docker?view=azure-devops