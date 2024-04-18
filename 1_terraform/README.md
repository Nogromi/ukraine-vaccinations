

### Execution
install [Terraform](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started)
Ensure GOOGLE_APPLICATION_CREDENTIALS env variable is set. 



```shell
export GOOGLE_APPLICATION_CREDENTIALS="/home/anatolii/credentials/vaccination/key.json" # change it to your path
```


```shell
# Optional
# Also verify that you use correct local project id in  Application Default Credentials file(/home/\<user\>/.config/gcloud/application_default_credentials.json)

gcloud config configurations list
gcloud config set project vaccinations-ukraine-1
gcloud auth application-default set-quota-project vaccinations-ukraine-1
```


```shell
# Login with this servidce account 
gcloud auth login
```

```shell
# Set current project if needed 
gcloud config set project vaccinations-ukraine-1
```

In  variables.tf change project id, region, and name of the GCS bucket with your details, build the required cloud resources using Terraform:

```shell
# Initialize state file (.tfstate)
terraform init

# Check changes to new infra plan
terraform plan 
```

```shell
# Create new infra
terraform apply 
```

```shell
# Delete infra after your work, to avoid costs on any running services
terraform destroy
```
