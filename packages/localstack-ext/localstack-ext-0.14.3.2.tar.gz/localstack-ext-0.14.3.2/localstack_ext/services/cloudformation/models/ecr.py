from localstack.services.cloudformation.service_models import GenericBaseModel
from localstack.utils.aws import aws_stack
from localstack_ext.utils.aws import aws_utils
class ECRRepository(GenericBaseModel):
 @staticmethod
 def cloudformation_type():
  return "AWS::ECR::Repository"
 def get_physical_resource_id(self,attribute=None,**kwargs):
  if attribute=="Arn":
   return self.get_cfn_attribute(attribute)
  return self.props.get("RepositoryName")
 def get_cfn_attribute(self,attribute_name):
  if attribute_name=="Arn":
   return aws_utils.get_ecr_repository_arn(self.props.get("RepositoryName"))
  if attribute_name=="RepositoryUri":
   return self.props.get("repositoryUri")
  return super(ECRRepository,self).get_cfn_attribute(attribute_name)
 def fetch_state(self,stack_name,resources):
  client=aws_stack.connect_to_service("ecr")
  props=self.props
  repo_name=props.get("RepositoryName")
  registry_id=props.get("LifecyclePolicy",{}).get("RegistryId")
  kwargs={"registryId":registry_id}if registry_id else{}
  result=client.describe_repositories(repositoryNames=[repo_name],**kwargs).get("repositories",[])
  return(result or[None])[0]
 @staticmethod
 def get_deploy_templates():
  def _create_params(params,**kwargs):
   encryption_type=params.get("EncryptionConfiguration",{}).get("EncryptionType","AES-256")
   response={"repositoryName":params["RepositoryName"],"tags":params.get("Tags",[]),"imageTagMutability":params.get("ImageTagMutability","MUTABLE"),"imageScanningConfiguration":{"scanOnPush":params.get("ImageScanningConfiguration",{}).get("ScanOnPush",False)},"encryptionConfiguration":{"encryptionType":encryption_type}}
   if(encryption_type=="KMS" and params.get("EncryptionConfiguration",{}).get("KmsKey")is not None):
    response["encryptionConfiguration"]["kmsKey"]=params["EncryptionConfiguration"]["KmsKey"]
   return response
  result={"create":{"function":"create_repository","parameters":_create_params},"delete":{"function":"delete_repository","parameters":{"repositoryName":"RepositoryName"}}}
  return result
# Created by pyminifier (https://github.com/liftoff/pyminifier)
