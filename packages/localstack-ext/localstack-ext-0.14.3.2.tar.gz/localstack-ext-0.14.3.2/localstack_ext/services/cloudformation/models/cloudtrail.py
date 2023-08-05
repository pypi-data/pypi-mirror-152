from localstack.services.cloudformation.service_models import REF_ID_ATTRS,GenericBaseModel
from localstack.utils.aws import aws_stack
class CloudTrail(GenericBaseModel):
 @staticmethod
 def cloudformation_type():
  return "AWS::CloudTrail::Trail"
 def fetch_state(self,stack_name,resources):
  client=aws_stack.connect_to_service("cloudtrail")
  result=[t for t in client.list_trails()["Trails"]if t["Name"]==self.props["TrailName"]]
  return(result or[None])[0]
 def get_physical_resource_id(self,attribute,**kwargs):
  if attribute in REF_ID_ATTRS:
   return self.props["TrailName"]
 @staticmethod
 def get_deploy_templates():
  def put_event_selectors(resource_id,resources,*args,**kwargs):
   resource=resources[resource_id]
   props=resource.get("Properties",{})
   selectors=props.get("EventSelectors",[])
   if selectors:
    cloudtrail=aws_stack.connect_to_service("cloudtrail")
    cloudtrail.put_event_selectors(TrailName=props["TrailName"],EventSelectors=selectors)
   return{}
  def start_logging(resource_id,resources,*args,**kwargs):
   resource=resources[resource_id]
   props=resource.get("Properties",{})
   if props.get("IsLogging"):
    cloudtrail=aws_stack.connect_to_service("cloudtrail")
    cloudtrail.start_logging(Name=props["TrailName"])
   return{}
  return{"create":[{"function":"create_trail","parameters":{"CloudWatchLogsLogGroupArn":"CloudWatchLogsLogGroupArn","CloudWatchLogsRoleArn":"CloudWatchLogsRoleArn","EnableLogFileValidation":"EnableLogFileValidation","IncludeGlobalServiceEvents":"IncludeGlobalServiceEvents","IsMultiRegionTrail":"IsMultiRegionTrail","KmsKeyId":"KMSKeyId","Name":"TrailName","S3BucketName":"S3BucketName","S3KeyPrefix":"S3KeyPrefix","SnsTopicName":"SnsTopicName","TagsList":"Tags"}},{"function":put_event_selectors},{"function":start_logging}],"delete":{"function":"delete_trail","parameters":{"Name":"TrailName"}}}
# Created by pyminifier (https://github.com/liftoff/pyminifier)
